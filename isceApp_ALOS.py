import glob
import os
ruta="/home/data/insar/alos/Galeras/track152"
f1=glob.glob(ruta+"/ALPSR*")
f=[]
for k in f1:
	if not k.endswith(".zip"):
		f.append(k)
cont=0
pos=1
for i in f:
        d="/home/mario/Desktop/ALOS_insar/track152/"+`cont`
	os.makedirs(d)
        d1=d+"/isceApp.xml"
        ar=open(d1,"w+")
        ar.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<isceApp>\n<component name=\"isce\">\n<constant name=\"topdir\">/home/data/insar/alos/Galeras/track152</constant>\n<component name=\"stack\">\n<component name=\"Scene1\">\n<constant name=\"dir1\">$topdir$/"+i.split("/")[7]+"</constant>\n<property name=\"id\">alos1</property>\n<property name=\"hh\">$dir1$/IMG-HH-"+(i.split("/")[7]).split("-")[0]+"-H1.0__A</property>\n<property name=\"leaderfile\">$dir1$/LED-"+(i.split("/")[7]).split("-")[0]+"-H1.0__A</property>\n</component>\n</component>\n<property name=\"output directory\">.</property>\n<property name=\"selectScenes\">alos1</property>\n<property name=\"sensor name\">ALOS</property>\n<property name=\"number of patches\">1</property>\n<property name=\"slc offset method\">offsetprf</property> <!--offsetprf, ampcor-->\n<property name=\"do preprocess\">True</property>\n</component>\n</isceApp>")
	ar.close()
	cont+=1
	pos+=1
