#### module mise a plat
import bpy

bpy.ops.object.duplicate(linked=False, mode='TRANSLATION')

me = bpy.context.object.data
uv_layer = me.uv_layers.active.data

bpy.ops.object.shape_key_add(from_mix=True)
print("Added Base shapekey")

for poly in me.polygons:
    for loop_index in poly.loop_indices:
        i = me.loops[loop_index].vertex_index
        co = uv_layer[loop_index].uv
        me.vertices[i].co[0] = co[0] * 2    ## To resize result of UV mesh,
        me.vertices[i].co[1] = co[1] * 2    ## change the multiplied ammount
        me.vertices[i].co[2] = 0
print("Flattened Based on UV")

bpy.ops.object.shape_key_add(from_mix=False)
print("Added Morphed shapekey")