Classical PSHA using Area Source
================================

gem-tstation:/home/michele/ssd/calc_22631.hdf5 updated Tue May 31 15:39:20 2016

num_sites = 6, sitecol = 969 B

Parameters
----------
============================ ===============================
calculation_mode             'classical'                    
number_of_logic_tree_samples 0                              
maximum_distance             {'Active Shallow Crust': 200.0}
investigation_time           50.0                           
ses_per_logic_tree_path      1                              
truncation_level             3.0                            
rupture_mesh_spacing         2.0                            
complex_fault_mesh_spacing   2.0                            
width_of_mfd_bin             0.2                            
area_source_discretization   5.0                            
random_seed                  23                             
master_seed                  0                              
sites_per_tile               1                              
engine_version               '2.0.0-git4fb4450'             
============================ ===============================

Input files
-----------
======================= ============================================================
Name                    File                                                        
======================= ============================================================
gsim_logic_tree         `gmpe_logic_tree.xml <gmpe_logic_tree.xml>`_                
job_ini                 `job.ini <job.ini>`_                                        
source                  `source_model.xml <source_model.xml>`_                      
source_model_logic_tree `source_model_logic_tree.xml <source_model_logic_tree.xml>`_
======================= ============================================================

Composite source model
----------------------
========= ====== ====================================== =============== ================
smlt_path weight source_model_file                      gsim_logic_tree num_realizations
========= ====== ====================================== =============== ================
b1        1.000  `source_model.xml <source_model.xml>`_ simple(2)       2/2             
========= ====== ====================================== =============== ================

Required parameters per tectonic region type
--------------------------------------------
====== ===================================== =========== ======================= =================
trt_id gsims                                 distances   siteparams              ruptparams       
====== ===================================== =========== ======================= =================
0      BooreAtkinson2008() ChiouYoungs2008() rx rjb rrup vs30measured z1pt0 vs30 ztor mag rake dip
====== ===================================== =========== ======================= =================

Realizations per (TRT, GSIM)
----------------------------

::

  <RlzsAssoc(size=2, rlzs=2)
  0,BooreAtkinson2008(): ['<0,b1~b1,w=0.6>']
  0,ChiouYoungs2008(): ['<1,b1~b2,w=0.4>']>

Number of ruptures per tectonic region type
-------------------------------------------
================ ====== ==================== =========== ============ ======
source_model     trt_id trt                  num_sources eff_ruptures weight
================ ====== ==================== =========== ============ ======
source_model.xml 0      Active Shallow Crust 1           1640         41    
================ ====== ==================== =========== ============ ======

Informational data
------------------
======================================== ============
count_eff_ruptures_max_received_per_task 3,436       
count_eff_ruptures_num_tasks             24          
count_eff_ruptures_sent.monitor          76,200      
count_eff_ruptures_sent.rlzs_assoc       22,584      
count_eff_ruptures_sent.sitecol          10,392      
count_eff_ruptures_sent.siteidx          120         
count_eff_ruptures_sent.sources          272,610     
count_eff_ruptures_tot_received          82,458      
hazard.input_weight                      41          
hazard.n_imts                            3           
hazard.n_levels                          19          
hazard.n_realizations                    2           
hazard.n_sites                           6           
hazard.n_sources                         0           
hazard.output_weight                     684         
hostname                                 gem-tstation
======================================== ============

Slowest sources
---------------
============ ========= ============ ====== ========= =========== ========== =========
src_group_id source_id source_class weight split_num filter_time split_time calc_time
============ ========= ============ ====== ========= =========== ========== =========
0            1         AreaSource   41     205       0.006       0.043      0.0      
============ ========= ============ ====== ========= =========== ========== =========

Computation times by source typology
------------------------------------
============ =========== ========== ========= ======
source_class filter_time split_time calc_time counts
============ =========== ========== ========= ======
AreaSource   0.006       0.043      0.0       1     
============ =========== ========== ========= ======

Information about the tasks
---------------------------
Not available

Slowest operations
------------------
============================== ========= ========= ======
operation                      time_sec  memory_mb counts
============================== ========= ========= ======
managing sources               0.095     0.0       1     
reading composite source model 0.044     0.0       1     
splitting sources              0.043     0.0       1     
total count_eff_ruptures       0.007     0.0       24    
filtering sources              0.006     0.0       6     
store source_info              0.004     0.0       1     
reading site collection        0.002     0.0       1     
aggregate curves               2.856E-04 0.0       24    
============================== ========= ========= ======