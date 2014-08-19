import arcpy,os

directory = r"I:\Wkoay\TEST CONNECTION"
os.chdir(directory)
mxd = arcpy.mapping.MapDocument(directory+r'\BaseMap.mxd')
layers = arcpy.mapping.ListLayers(mxd,"")

layer_xref = []

for layer in layers:
        name = layer.name.replace(".","").replace(":","-")
        layer_name = name.replace("(","").replace("-","").replace(")","").replace("&","")
        xref = [layer_name,name]
        converted = ['QRA Wells','Well Borehole Path','Dry Hole','Bottom Hole Location','Abandoned Well','Active Wells Surface']
        print name, layer_name
        
        layer_xref.append(xref)
        if layer.isFeatureLayer and layer_name not in converted:
                arcpy.FeatureClassToFeatureClass_conversion(layer, directory, layer_name + ".shp")

files = os.listdir(directory)

for i in range(0,len(layer_xref)):
        for file in files:
                if file[0:file.index(".")] == lyr_xref[i][0]:
                        print 'renaming ' + file + ' to ' + lyr_xref[i][1]
                        os.rename(file,lyr_xref[i][1] + file[file.index("."):])
