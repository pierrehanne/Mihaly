import bpy
import os

# Cleans all decimate modifiers


def cleanAllDecimateModifiers(obj):
    for m in obj.modifiers:
        if(m.type == "DECIMATE"):
            obj.modifiers.remove(modifier=m)


numberOfIteration = 2
decimateRatio = 0.3
modifierName = 'DecimateMod'

for i in range(0, numberOfIteration):
    objectList = bpy.data.objects
    for obj in objectList:
        if(obj.type == "MESH"):

            cleanAllDecimateModifiers(obj)

            modifier = obj.modifiers.new(modifierName, 'DECIMATE')
            modifier.ratio = 1-decimateRatio*(i+1)
            modifier.use_collapse_triangulate = True

    fileName = bpy.data.filepath
    fileName = os.path.splitext(fileName)[0]

    # Trim decimate version of file name
    indexOf_ = fileName.rfind('_')
    if(indexOf_ != -1 and fileName[indexOf_]+fileName[indexOf_+1] == "_d"):
        fileName = fileName.split("_d")[0]

    fileName = '{}{}{}{}'.format(fileName, "_d", str(i+2), ".blend")

    bpy.ops.wm.save_as_mainfile(filepath=fileName)

#Exporation au format .PLY
print("Exportation...") #VISIBLE DANS LE TERMINAL

bpy.ops.export_mesh.ply(filepath=r"C:\Mihaly_export\Simplified.ply", check_existing=True, axis_forward='Y', axis_up='Z', filter_glob="*.ply")

print("Exportation reussie !")