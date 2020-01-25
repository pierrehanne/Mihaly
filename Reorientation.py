#Module Reorientation
import bpy
import math
import os
# place l'origine de notre figure
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
# selectionne l'objet
context = bpy.context
objet = context.object
# fixe valeurs location
loc = 0 
loc_x = loc_y = loc_z = loc
# fixe valeurs rotation
rot_y = 0
rot_x = rot_z = ((math.pi)/2)
# effectue sur l'objet la location et rotation
objet.location = (loc_x, loc_y, loc_z)
objet.rotation_euler = (rot_x, rot_y, rot_z)
# sauvegarde fichier .ply
fileName=bpy.data.filepath
fileName=os.path.splitext(fileName)[0]
indexOf_=fileName.rfind('_')
if(indexOf_!=-1 and fileName[indexOf_]+fileName[indexOf_+1]=="_r"):
    fileName=fileName.split("_rr")[0]
    fileName='{}{}{}{}'.format(fileName, "_r",str(i+2),".ply")
    bpy.ops.wm.save_as_mainfile(filepath=fileName)
