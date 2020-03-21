#Module reparation
import bpy
import bmesh

#selectionne l'objet
context = bpy.context
scene = context.scene

#active l'objet dans la scene
objectToSelect = bpy.context.active_object
objectToSelect.select_set(True) 

# cree le bmesh 
bm = bmesh.new()
for o in context.selected_objects:
    # charge bmesh
    bm.from_mesh(o.data)
    # trouve les frontieres
    bound_edges = set(e for e in bm.edges if e.is_boundary)
    zero_edges = set(e for e in bound_edges 
        if all(abs(v.co.x) < 0.001 for v in e.verts))
    right_edges = bound_edges - zero_edges
    # utilise bmesh tool
    result = bmesh.ops.contextual_create(bm, geom=list(bound_edges))
    # affiche le resultat
    bmesh.ops.poke(bm, faces=result["faces"])
    bm.to_mesh(o.data)
    o.data.update()
    bm.clear()
bm.free()
