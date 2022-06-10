# -*- coding: utf-8 -*-
"""
Created on Thu May 26 12:37:47 2022

@author: mddaf
"""
import nibabel as nib
from utilities import *
import os


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
    #to get the current working directory

    brain=nib.load(brain_path+ "STA"+str(GA)+"_tissue.nii.gz")
    brain = np.array(brain.dataobj)
    shift = int(shift_mm / SimRes)
    Fetal_Brain = FOV_shift(brain, shift, orientation)
    
    # Load the intensity non-uniformity fields
    b1map = brainWeb_inu(inu, Fetal_Brain);
    if orientation >=0: 
        Fetal_Brain=np.moveaxis(Fetal_Brain, orientation-1, 2)
        
    SubunitRes = SimRes / sampling_factor

    Fetal_Brain_upsampled = sampling_OoP(    Fetal_Brain, sampling_factor, 'nearest')

    b1map_upsampled = sampling_OoP(b1map, sampling_factor, 'linear')
    return Fetal_Brain 
