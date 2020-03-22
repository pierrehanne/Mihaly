import bpy
import bmesh
import os

ob = bpy.context.object
me = ob.data

bm = bmesh.new()
bm.from_mesh(me)
stats = ["Faces: %d" % len(bm.faces), 
        "Verts: %d" % len(bm.verts), 
        "Edges: %d" % len(bm.edges)]

# triangulate 
bmesh.ops.triangulate(bm, faces=bm.faces[:])
stats.append("Tris: %d" % len(bm.faces))

# Ensure all folders of the path exist
path = "C:\\Users\\Pierr\\OneDrive\\Bureau\\Mihaly"
os.makedirs(path, exist_ok=True)

# Write in folder stats
with open(path + "file.txt", "w") as file:
    file.write(" | ".join(stats))