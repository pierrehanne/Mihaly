#Module reparation
import bpy
import bmesh
context = bpy.context
scene = context.scene
# completely remove cube if in scene
cube = scene.objects.get("Cube")
if cube:
    bpy.data.objects.remove(cube, do_unlink=True)
bm = bmesh.new()
# import from obj file here, only imported objects will be 
# in context.selected_objects after import.    
for o in context.selected_objects:
    # test here to continue if not mesh, can obj import other???
    # load bmesh
    bm.from_mesh(o.data)
    # find boundaries
    bound_edges = set(e for e in bm.edges if e.is_boundary)
    # used sets, may not be required.
    zero_edges = set(e for e in bound_edges 
        if all(abs(v.co.x) < 0.001 for v in e.verts))
    right_edges = bound_edges - zero_edges
    # use bmesh "F" tool
    result = bmesh.ops.contextual_create(bm, geom=list(bound_edges))
    # poke the resulting faces to make triangular fan.
    bmesh.ops.poke(bm, faces=result["faces"])
    bm.to_mesh(o.data)
    o.data.update() # mainly only need for UI really
    bm.clear()
bm.free()