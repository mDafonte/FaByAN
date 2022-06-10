
# Fetal brain model: In this demonstration, we base our simulations on
# segmented high-resolution anatomical MR images of the fetal brain that
# can be downloaded from:
# http://crl.med.harvard.edu/research/fetal_brain_atlas/
# Gholipour, A. et al. A normative spatiotemporal MRI atlas of the fetal
# brain for automatic segmentation and analysis of early brain growth.
# Scientific Reports 7, 476 (2017).
# https://doi.org/10.1038/s41598-017-00525-w
from fabian import *
Fetal_Brain_model_path = 'data/Simu_FSE/Atlas/CRL_FetalBrainAtlas_2017v3/'
# Gestational age (in weeks)
GA = 26;
# Resolution of the Fetal_Brain images (isotropic, in mm)
SimRes = 0.8;
# Introduce a shift variable to slightly shift the slice series between two
# simulations in the same orientation
shift_mm = 0;   #mm
# Choose the orientation plane of the acquisitions
# (0: sagittal, 1: coronal, 2: axial)
orientation = 2;
# Non-linear slowly-varying intensity non-uniformity (INU) fields (b1+) can
# be downloaded from BrainWeb database:
# https://brainweb.bic.mni.mcgill.ca/brainweb/about_sbd.html
inu = 'data/Simu_FSE/rf20_B.rawb';
# Define a sampling factor to subdivide the volume in the slice thickness
# orientation
sampling_factor = 1;
# Main magnetic field strength
B0 = 1.5;
# Acquisition parameters
ESP = 4.08;  #ms
ETL = 224;
# Geometry
PhaseOversampling = 0.803571000000000;
SliceThickness = 3.2; #mm
SliceGap = 0.3; #mm
# Resolution
FOVRead = 360;  #mm
FOVPhase = 360; #mm
BaseResolution = 327;   #voxels
PhaseResolution = 0.7;
# Contrast
TR = 4.08;  #ms
TEeff = 90; #ms
# Acceleration technique
ACF = 2;
RefLines = 42;
# Motion
motion_level = 3;   #little motion
# Scanner zero-interpolation filling (ZIP)
# (0: no ZIP; 1: Fermi filtering in k-space and ZIP)
zippy = 0;
reconMatrix = BaseResolution;
# SNR
std_noise = 0;
output_folder= "lorem ipsum"
HASTE_Images = FaBiAN_main(Fetal_Brain_model_path,
                                               GA, 
                                           SimRes, 
                                         shift_mm, 
                                      orientation,
                                              inu,
                                  sampling_factor, 
                                               B0,
                                              ESP, 
                                              ETL,
                                PhaseOversampling, 
                                   SliceThickness,
                                         SliceGap, 
                                          FOVRead, 
                                         FOVPhase,
                                   BaseResolution, 
                                  PhaseResolution, 
                                               TR, 
                                            TEeff, 
                                              ACF, 
                                         RefLines, 
                                     motion_level, 
                                              zippy, 
                                      reconMatrix, 
                                        std_noise, 
                                    output_folder);
