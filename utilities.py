# -*- coding: utf-8 -*-
"""
Adaptation of the "utilities" folder of matlab to Python. 

miguel Díaz-Cacho
"""

import nibabel as nib 
import numpy as np

def FOV_shift(Fetal_Brain, shift, orientation):
    
    # Resize the fetal brain volume to allow shifting in any direction
    fetal_shape=Fetal_Brain.shape
    k=np.ceil(abs(shift)).astype("int16")
    
    Fetal_Brain_FOV = np.array([[k,(fetal_shape[0]-k)], [k,(fetal_shape[1]-k)], [k,(fetal_shape[2]-k)]])
    Fetal_Brain_FOV[orientation,:]=Fetal_Brain_FOV[orientation,:]+1

     
    # Mask the fetal brain after having shifted the slice slab

    Fetal_Brain_shift = Fetal_Brain[Fetal_Brain_FOV[0,0]:Fetal_Brain_FOV[0,1],
                                    Fetal_Brain_FOV[1,0]:Fetal_Brain_FOV[1,1],
                                    Fetal_Brain_FOV[2,0]:Fetal_Brain_FOV[2,1]]

    return Fetal_Brain_shift
def  Resize_Volume(I,sz):
    ##i have no idea if the else are working. 
    size=np.shape(I)
    if size[0]!=sz[0] or size[1]!=sz[1] or size[2]!=sz[2]:

        
        if len(sz)==1:
            sz=[sz,sz]
        
        if size[0]>=sz[0]:
            y=int(np.ceil((size[0]-sz[0])/2))

            I=I[y:y+sz[0],:,:]
            
        else:
            p1=sz[0]-size[0]
            I=np.concatenate(1,np.zeros(np.floor(0.5*p1),size[1],size[2]),I,np.zeros(np.ceil(0.5*p1),size[1],size[2]))
        
        
        
        if size[1]>=sz[1]:
            x=int(np.ceil((size[1]-sz[1])/2))
            I=I[:,x:x+sz[1],:]
        else:
            p2=sz[1]-size[1];
            I=np.concatenate(2,np.zeros(size[0],np.floor(0.5*p2),size[2]),I,np.zeros(size[0],np.ceil(0.5*p2),size[2],size[3]))
        
        
        if size[2]>1:
            if size[2]>=sz[2]:
                z=int(np.ceil((size[2]-sz[2])/2))
                I=I[:,:,z:z+sz[2]]
            else:
                p3=sz[2]-size[2]
                I=np.concatenate(3,np.zeros(size[0],size[1],np.floor(0.5*p3),size[3]),I,np.zeros(size[0],size[1],np.ceil(0.5*p3),size[3]))
    return I
        
def  brainWeb_inu(inu, Fetal_Brain):
    
    # x, y and z are the dimensions of the simulated intensity non-uniformity
    # fields from the BrainWeb database
    z = 181
    y = 217
    x = 181    
    # Read BrainWeb intensity non-uniformity fields (3D)
    volume = np.reshape(np.fromfile(inu,dtype="int8"),[x,y,z])

    
    # Resize the intensity non-uniformity fields to match the fetal brain
    # volume dimensions
    b1map_res = Resize_Volume(volume, Fetal_Brain.shape)
    
    # Normalize the intensity non-uniformity fields by 1.2 (i.e., level of 40%)

    b1map = b1map_res/ np.max(b1map_res) * 1.2

    return b1map


