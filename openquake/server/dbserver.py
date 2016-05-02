#  -*- coding: utf-8 -*-
#  vim: tabstop=4 shiftwidth=4 softtabstop=4

#  Copyright (c) 2016, GEM Foundation

#  OpenQuake is free software: you can redistribute it and/or modify it
#  under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  OpenQuake is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU Affero General Public License
#  along with OpenQuake.  If not, see <http://www.gnu.org/licenses/>.

import logging
from Queue import Queue
from threading import Thread
from multiprocessing import Process
from multiprocessing.connection import Listener

from openquake.commonlib import sap
from openquake.commonlib.parallel import safely_call
from openquake.engine import config
from openquake.server.db import actions
from openquake.server.settings import DATABASE
from django.db import connection
import django
if hasattr(django, 'setup'):  # >= 1.7
    django.setup()

queue = Queue()


def run_command(cmd, args, conn):
    """
    Execute the received command. Errors are trapped and a pair
    (result, exctype) is sent back.
    `exctype` is None if there is no exception, otherwise it is an exception
    class and `result` is an error string containing the traceback.
    """
    try:
        func = getattr(actions, cmd)

        # execute the function by trapping any possible exception
        res, etype, _ = safely_call(func, args)
        if etype:
            logging.error(res)

        # send back the result and the exception class
        conn.send((res, etype))
    finally:
        conn.close()


def run_commands():
    """
    Execute the received commands in a queue.
    """
    connection.cursor()  # bind the db
    while True:
        conn, cmd, args = queue.get()
        if cmd == 'stop':
            conn.send((None, None))
            conn.close()
            break
        run_command(cmd, args, conn)


class DbServer(object):
    """
    A server collecting the received commands into a queue
    """
    def __init__(self, address, authkey):
        self.address = address
        self.authkey = authkey
        self.thread = Thread(target=run_commands)

    def loop(self):
        listener = Listener(self.address, backlog=5, authkey=self.authkey)
        logging.warn('DB server listening on %s:%d...' % self.address)
        self.thread.start()
        cmd = None
        try:
            while cmd != 'stop':
                try:
                    conn = listener.accept()
                except KeyboardInterrupt:
                    break
                except:
                    # unauthenticated connection, for instance by a port
                    # scanner such as the one in manage.py
                    continue
                cmd_ = conn.recv()  # a tuple (name, arg1, ... argN)
                cmd, args = cmd_[0], cmd_[1:]
                if cmd.startswith('@'):  # slow command, run in process
                    cmd = cmd[1:]  # strip @
                    proc = Process(
                        target=run_command, name=cmd, args=(cmd, args, conn))
                    proc.start()
                    logging.warn('Started %s%s in process %d',
                                 cmd, args, proc.pid)
                else:
                    queue.put((conn, cmd, args))
        finally:
            listener.close()
            self.thread.join()


def runserver(dbpathport=None, loglevel='WARN'):
    logging.basicConfig(level=getattr(logging, loglevel))
    if dbpathport:  # assume a string of the form "dbpath:port"
        dbpath, port = dbpathport.split(':')
        addr = (DATABASE['HOST'], int(port))
        DATABASE['NAME'] = dbpath
        DATABASE['PORT'] = int(port)
    else:
        addr = config.DBS_ADDRESS
    DbServer(addr, config.DBS_AUTHKEY).loop()

parser = sap.Parser(runserver)
parser.arg('dbpathport', 'dbpath:port')
parser.opt('loglevel', 'WARN or INFO')

if __name__ == '__main__':
    parser.callfunc()
