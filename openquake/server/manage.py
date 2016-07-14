#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright (C) 2014-2016 GEM Foundation
#
# OpenQuake is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with OpenQuake. If not, see <http://www.gnu.org/licenses/>.
from __future__ import print_function
import os
import sys
import sqlite3
from django.core.management import execute_from_command_line
from openquake.server.db import actions
from openquake.server.dbapi import Db
from openquake.server.settings import DATABASE
from openquake.server import executor
from openquake.engine import logs


# this is used in test mode
db = Db(sqlite3.connect, DATABASE['NAME'], isolation_level=None,
        detect_types=sqlite3.PARSE_DECLTYPES)


# in test mode: bypass the DbServer and run the action directly
def dbcmd(action, *args):
    """
    Direct dispatcher to the database, used in the tests

    :param action: database action to perform
    :param args: arguments
    """
    return getattr(actions, action)(db, *args)


def parse_args(argv):
    # manages the argument "tmpdb=XXX" used in the functional tests
    args = []
    dbname = None
    for arg in argv:
        if arg.startswith('tmpdb='):
            dbname = arg[6:]
        else:
            args.append(arg)
    return args, dbname

# the code here is run in development mode; for instance
# $ python manage.py runserver 0.0.0.0:8800
if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "openquake.server.settings")
    argv, tmpfile = parse_args(sys.argv)
    if tmpfile:  # this is used in the functional tests
        DATABASE['NAME'] = tmpfile
        logs.dbcmd = dbcmd
        dbcmd('upgrade_db')
    else:
        # check the database version
        logs.dbcmd('check_outdated')
        # reset is_running
        logs.dbcmd('reset_is_running')
    with executor:
        execute_from_command_line(argv)
