import bpy
import bmesh
import math
import random
import json

random.seed=10



vertices=[(1,1,-1),(1,-1,-1),(-1,-1,-1),(-1,1,-1),(1,1,1),(1,-1,1),(-1,-1,1),(-1,1,1)]
edges=[]
faces=[(0,1,2,3),(4,5,6,7),(0,4,7,3),(0,1,5,4),(1,2,6,5),(7,6,2,3)]
#scene.objects.link(ob)

# mesh
new_mesh=bpy.data.meshes.new("new_mesh")
sp = bmesh.new()
bmesh.ops.create_uvsphere(sp, u_segments=32, v_segments=16, diameter=1)
sp.to_mesh(new_mesh)
# cam
cam_data = bpy.data.cameras.new('camera')
cam = bpy.data.objects.new('camera', cam_data)
bpy.context.collection.objects.link(cam)
# add camera to scene
scene = bpy.context.scene
scene.camera=cam
cam.location=(-3.71321 , 3.18657 , 1.05654 )
pi=math.pi
# rotation
cam.rotation_euler[0] = 78.6 * (pi / 180.0)
cam.rotation_euler[1] = 0 * (pi / 180.0)
cam.rotation_euler[2] = -130 * (pi / 180.0)

# upload mesh
new_object = bpy.data.objects.new("new_object", new_mesh)
view_layer=bpy.context.view_layer
view_layer.active_layer_collection.collection.objects.link(new_object)
test=bpy.data.objects["new_object"]
test.select_set(True)
bpy.ops.object.shade_smooth()


# render settings
scene = bpy.context.scene
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = "C:/Users/x065p/Desktop/blender/result/image/python/img.png"
bpy.context.scene.render.resolution_x =100 #perhaps set resolution in code
bpy.context.scene.render.resolution_y =100
# bpy.ops.render.render(write_still = 1)

# bpy.ops.object.delete()
save_value=[]
for i in range(0,1):
    print(i)
    save_value.append([])

    bsdf=bpy.data.materials.new(name="python material end in tr")
    bsdf.use_nodes=True
    normal_node=bsdf.node_tree.nodes.get("Principled BSDF")
#    print(normal_node.input)

    # normal_node.inputs[0].default_value=(0,0,1,1)
    # to trantion roughtloss
    for j ,o in  enumerate(normal_node.inputs):
        if j>16:
            break
        print(o.name)
        save_value[i].append([])
        # normal_node.inputs[j].default_value=random.random()
        if j==0 or j==3 or j==17:
            print("r\ng\nba")
            save_value[i][j]=([random.random(),random.random(),random.random(), 1])
            normal_node.inputs[j].default_value=save_value[i][j]
        elif j==14:
            save_value[i][j]=(random.random()*2)
            normal_node.inputs[j].default_value=save_value[i][j]

        elif j!=2:
            save_value[i][j]=(random.random())
            normal_node.inputs[j].default_value=save_value[i][j]

        # print(j)
        # print(save_value[i][j])

    # test.data.materials.append(bsdf)
    if test.data.materials:
        test.data.materials[0]=bsdf
    else:
        test.data.materials.append(bsdf)
    scene.render.filepath = "C:/Users/x065p/Desktop/blender/result/image/python/{}.png".format(i)
    bpy.ops.render.render(write_still = 1)
    with open("C:/Users/x065p/Desktop/blender/result/image/python/save_value.txt","w") as f:
        f.write(json.dumps(save_value))
        f.close()

#with open("C:/Users/x065p/Desktop/blender/result/image/python/save_value.txt","w") as f:
#    f.write(json.dumps(save_value))
#    f.close()
# f.close()
# material
# bsdf=bpy.data.materials.new(name="python material")
# bsdf.use_nodes=True
# normal_node=bsdf.node_tree.nodes.get("Principled BSDF")
# normal_node.inputs[0].default_value=(0,0,1,1)
# test.data.materials.append(bsdf)
