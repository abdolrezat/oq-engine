Classical Hazard QA Test, Case 4
================================

gem-tstation:/home/michele/ssd/calc_22595.hdf5 updated Tue May 31 15:37:54 2016

num_sites = 1, sitecol = 739 B

Parameters
----------
============================ ===============================
calculation_mode             'classical'                    
number_of_logic_tree_samples 0                              
maximum_distance             {'active shallow crust': 200.0}
investigation_time           1.0                            
ses_per_logic_tree_path      1                              
truncation_level             0.0                            
rupture_mesh_spacing         0.01                           
complex_fault_mesh_spacing   0.01                           
width_of_mfd_bin             1.0                            
area_source_discretization   10.0                           
random_seed                  1066                           
master_seed                  0                              
sites_per_tile               10000                          
engine_version               '2.0.0-git4fb4450'             
============================ ===============================

Input files
-----------
======================= ============================================================
Name                    File                                                        
======================= ============================================================
gsim_logic_tree         `gsim_logic_tree.xml <gsim_logic_tree.xml>`_                
job_ini                 `job.ini <job.ini>`_                                        
source                  `source_model.xml <source_model.xml>`_                      
source_model_logic_tree `source_model_logic_tree.xml <source_model_logic_tree.xml>`_
======================= ============================================================

Composite source model
----------------------
========= ====== ====================================== =============== ================
smlt_path weight source_model_file                      gsim_logic_tree num_realizations
========= ====== ====================================== =============== ================
b1        1.000  `source_model.xml <source_model.xml>`_ trivial(1)      1/1             
========= ====== ====================================== =============== ================

Required parameters per tectonic region type
--------------------------------------------
====== ================ ========= ========== ==========
trt_id gsims            distances siteparams ruptparams
====== ================ ========= ========== ==========
0      SadighEtAl1997() rrup      vs30       rake mag  
====== ================ ========= ========== ==========

Realizations per (TRT, GSIM)
----------------------------

::

  <RlzsAssoc(size=1, rlzs=1)
  0,SadighEtAl1997(): ['<0,b1~b1,w=1.0>']>

Number of ruptures per tectonic region type
-------------------------------------------
================ ====== ==================== =========== ============ ======
source_model     trt_id trt                  num_sources eff_ruptures weight
================ ====== ==================== =========== ============ ======
source_model.xml 0      Active Shallow Crust 1           901          901   
================ ====== ==================== =========== ============ ======

Informational data
------------------
======================================== ============
count_eff_ruptures_max_received_per_task 2,565       
count_eff_ruptures_num_tasks             1           
count_eff_ruptures_sent.monitor          2,304       
count_eff_ruptures_sent.rlzs_assoc       740         
count_eff_ruptures_sent.sitecol          433         
count_eff_ruptures_sent.siteidx          5           
count_eff_ruptures_sent.sources          1,086       
count_eff_ruptures_tot_received          2,565       
hazard.input_weight                      901         
hazard.n_imts                            1           
hazard.n_levels                          3.000       
hazard.n_realizations                    1           
hazard.n_sites                           1           
hazard.n_sources                         0           
hazard.output_weight                     3.000       
hostname                                 gem-tstation
======================================== ============

Slowest sources
---------------
============ ========= ================= ====== ========= =========== ========== =========
src_group_id source_id source_class      weight split_num filter_time split_time calc_time
============ ========= ================= ====== ========= =========== ========== =========
0            1         SimpleFaultSource 901    1         0.001       0.504      0.0      
============ ========= ================= ====== ========= =========== ========== =========

Computation times by source typology
------------------------------------
================= =========== ========== ========= ======
source_class      filter_time split_time calc_time counts
================= =========== ========== ========= ======
SimpleFaultSource 0.001       0.504      0.0       1     
================= =========== ========== ========= ======

Information about the tasks
---------------------------
Not available

Slowest operations
------------------
============================== ========= ========= ======
operation                      time_sec  memory_mb counts
============================== ========= ========= ======
reading composite source model 0.520     0.0       1     
managing sources               0.508     0.0       1     
splitting sources              0.504     0.0       1     
store source_info              0.004     0.0       1     
filtering sources              0.001     0.0       1     
total count_eff_ruptures       1.900E-04 0.0       1     
reading site collection        2.599E-05 0.0       1     
aggregate curves               1.478E-05 0.0       1     
============================== ========= ========= ======