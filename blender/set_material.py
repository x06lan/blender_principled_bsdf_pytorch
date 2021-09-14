import bpy
import bmesh
import math
import random
import json

for i in range(0,1):

    bsdf=bpy.data.materials.new(name="python material")
    bsdf.use_nodes=True
    normal_node=bsdf.node_tree.nodes.get("Principled BSDF")
    arg=[]
    with  open("C:/Users/x065p/Desktop/test/python/PyTorch/blender/out.json",'r',encoding = 'utf-8') as f:
        arg=json.loads(f.read())

    # normal_node.inputs[0].default_value=(0,0,1,1)
    i=0
    for j in range(0,19):
        
        # normal_node.inputs[j].default_value=random.random()
        if j==0 or j==3 or j==17:
            normal_node.inputs[j].default_value=[arg[i],arg[i+1],arg[i+2],arg[i+3]]
            i+=4
        elif j==14:
            normal_node.inputs[j].default_value=arg[i]
            i+=1
        elif j!=2:
            normal_node.inputs[j].default_value=arg[i]
            i+=1
        # print(j)
        

