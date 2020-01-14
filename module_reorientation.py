#Module Reorientation
import bpy

#selectionne un objet
context = bpy.context
objet = context.object

#fixe valeur location et rotation
loc,rot = 0,0
loc_x = loc_y = loc_z = loc
rot_x = rot_y = rot_z = rot

#effectue sur l'objet la location et rotation
objet.location = (loc_x, loc_y, loc_z)
objet.rotation_euler = (rot_x, rot_y, rot_z)