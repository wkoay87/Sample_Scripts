# ---------------------------------------------------------------------------
# CalculatePlyAcres.py
# Created on: Tue Jul 01 2014 10:14:02 AM
#   (generated by ArcGIS/ModelBuilder)
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting,cx_Oracle,argparse
from helpers.DB_helper import DB_Connection

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Load required toolboxes...
gp.AddToolbox("E:/Program Files (x86)/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")


parser = argparse.ArgumentParser(description = 'Recalculate polygon acres/grs acres daily')
parser.add_argument("-pw", required=True, help="QGIS pws", type = str, nargs = 1)
parser.add_argument("-db",required=True, help="QGIS database name", type = str, nargs = 1)
parser.add_argument("-u",required=True, help="QGIS database user", type = str, nargs = 1)
args = parser.parse_args()

# Local variables...
db = args.db[0]
dbuser = args.u[0]
dbpw = args.pw[0]

SQL_AGM = """UPDATE AAP_CALC_AREA AA SET GRS_ACRE = (SELECT ACRE_AMT FROM ACREAGES@SDE_TO_LAND AC WHERE AA.SOB_SYS_FK = AC.ARRG_KEY AND ACRE_TYPE_CODE = 'GRS')
WHERE EXISTS (SELECT 0 FROM ACREAGES@SDE_TO_LAND AC WHERE AA.SOB_SYS_FK = AC.ARRG_KEY AND ACRE_TYPE_CODE = 'GRS')"""

SQL_ARE = """UPDATE AAP_CALC_AREA AA SET GRS_ACRE = (SELECT ACRE_AMT FROM ACREAGES@SDE_TO_LAND AC WHERE AA.SOB_SYS_FK = AC.ARRG_KEY AND ACRE_TYPE_CODE = 'STA')
WHERE EXISTS (SELECT 0 FROM ACREAGES@SDE_TO_LAND AC WHERE AA.SOB_SYS_FK = AC.ARRG_KEY AND ACRE_TYPE_CODE = 'STA')"""


QGIS_ALL_AGREEMENTS_PLY_TEMP = "\\\\shares\\backups\\qgis-workspace\\temp.gdb\\ALL_AGREEMENTS_PLY"
QGIS_ALL_AGREEMENTS_PLY = "Database Connections\\"+dbuser+"@"+db+".sde\\QGIS.ALL_AGREEMENTS_PLY"
AAP_CALC_AREA = "\\\\shares\\backups\\qgis-workspace\\temp.gdb\\AAP_CALC_AREA"
QGIS_AAP_CALC_AREA = "Database Connections\\"+dbuser+"@"+db+".sde\\QGIS.AAP_CALC_AREA"

print 'Removing old features...'

# Process: Remove old feature classes
if gp.exists(QGIS_ALL_AGREEMENTS_PLY_TEMP):
    gp.Delete_management(QGIS_ALL_AGREEMENTS_PLY_TEMP, "FeatureClass")

if gp.exists(AAP_CALC_AREA):
    gp.Delete_management(AAP_CALC_AREA, "FeatureClass")

if gp.exists(QGIS_AAP_CALC_AREA):
    gp.Delete_management(QGIS_AAP_CALC_AREA, "FeatureClass")

print 'Copy...'    
# Process: Copy...    
gp.Copy_management(QGIS_ALL_AGREEMENTS_PLY, QGIS_ALL_AGREEMENTS_PLY_TEMP, "FeatureClass")

print 'Projecting...'
# Process: Project...
gp.Project_management(QGIS_ALL_AGREEMENTS_PLY_TEMP, AAP_CALC_AREA, "PROJCS['USA_Contiguous_Albers_Equal_Area_Conic',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Albers'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-96.0],PARAMETER['Standard_Parallel_1',29.5],PARAMETER['Standard_Parallel_2',45.5],PARAMETER['Latitude_Of_Origin',37.5],UNIT['Meter',1.0]]", "NAD_1927_To_NAD_1983_6", "GEOGCS['GCS_North_American_1927',DATUM['D_North_American_1927',SPHEROID['Clarke_1866',6378206.4,294.9786982]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")

# Process: Add Field...
gp.AddField_management(AAP_CALC_AREA, "PLY_ACRES", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

print 'Calculating Ply acres'
# Process: Calculate Field...
gp.CalculateField_management(AAP_CALC_AREA, "PLY_ACRES", "!shape.area@acres!", "PYTHON", "")

print 'Copying to db...'
# Process: Copy AAP_CALC_AREA to PRD database    
gp.Copy_management(AAP_CALC_AREA, QGIS_AAP_CALC_AREA, "FeatureClass")
print 'Calculate grs acres...'
# Calculate GRS acres
db_con = DB_Connection(db,dbuser,dbpw)
# check records before sending notification
db_con.ora_updt_sql(SQL_AGM)
db_con.ora_updt_sql(SQL_ARE)
print 'Complete'
