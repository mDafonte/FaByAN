# -*- coding: utf-8 -*-
"""
Created on Thu May 26 12:37:47 2022

@author: mddaf
"""
import nibabel as nib
from utilities import *

def FaBiAN_main(brain_path,
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
                output_folder):
    brain=nib.read(brain_path+ "STA"+GA+"_tissue_nii.gz")
    shift = shift_mm / SimRes
    Fetal_Brain = FOV_shift(Fetal_Brain, shift, orientation)

