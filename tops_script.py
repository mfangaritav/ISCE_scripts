import glob
import os
'''
This script creates folders and xml input files for topsApp.py it makes all the posibles 
pairs for some Sentinel SAR scenes.

This script should be execute before tops_commands.py
'''
#Sentinel SAR scenes folder
SAR_images="/home/data/insar/sentinel/cerro_negro/"
#Folder where all the inteferograms will be storage
output="/home/mario/Desktop/Sentinel_insar/A120/"
#SAR scenes folders array
f1=glob.glob(SAR_imagenes+"*")
f=[]
for k in f1:
    f.append(k)
cont=0
pos=1
#The indexes i and j are the two SAR scenes for the interferogram
for i in f:
    for j in f[pos:]:
#This part choose which of the two scenes has the first date, and that scene is the master
        if int((os.path.basename(i).split('_')[5]).split('T')[0])<int((os.path.basename(j).split('_')[5]).split('T')[0]):
           m=i
           s=j
        else:
           m=j
           s=i
#pd is the name of the interferogram folder the format is '1st date'_'2nd date'
        pd=(os.path.basename(m).split('_')[5]).split('T')[0]+"_"+(os.path.basename(s).split('_')[5]).split('T')[0]
#The script makes all the posible interferograms on the three swaths
        for h in range(3):
            g=h+1
            d=output+"sub_"+str(g)+"/"+pd
            os.makedirs(d)
            d1=d+"/topsApp.xml"
            ar=open(d1,"w+")
            ar.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<topsApp>\n <component name=\"topsinsar\">\n    <property name=\"Sensor name\">SENTINEL1A</property>\n    <property name=\"do unwrap\">True</property>\n    <property name=\"unwrapper name\">snaphu_mcf</property>\n    <component name=\"master\">\n      <property name=\"orbit directory\">/home/data/ORBITS/sentinel-1/POEORB</property>\n      <property name=\"auxiliary data directory\">/home/data/ORBITS/sentinel-1/AUX_CAL</property>\n      <property name=\"output directory\">master</property>\n      <property name=\"swath number\">"+str(g)+"</property>\n      <property name=\"safe\">/home/data/insar/sentinel/cerro_negro/"+os.path.basename(m)+"</property>\n    </component>\n    <component name=\"slave\">\n      <property name=\"orbit directory\">/home/data/ORBITS/sentinel-1/POEORB</property>\n      <property name=\"auxiliary data directory\">/home/data/ORBITS/sentinel-1/AUX_CAL</property>\n      <property name=\"output directory\">slave</property>\n      <property name=\"swath number\">"+str(g)+"</property>\n      <property name=\"safe\">/home/data/insar/sentinel/cerro_negro/"+os.path.basename(s)+"</property>\n    </component>\n    <constant name=\'demdir\'>/home/data/dems/srtmGL1/colombia</constant>\n    <property name=\"demfilename\">$demdir$/demLat_S04_N12_Lon_W081_W070.dem.wgs84</property>\n  </component>\n</topsApp>")
            ar.close()
    pos+=1
