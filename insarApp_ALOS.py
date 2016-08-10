import glob
import os
import math
ruta="/home/data/insar/alos/Galeras/track152"
f1=glob.glob(ruta+"/ALPSR*")
f=[]
for k in f1:
	if not k.endswith(".zip"):
		f.append(k)
cont=0
pos=1
bs_top = 'perp_baseline_top' # dummy word. you take it from input
bs_bottom ='perp_baseline_bottom'
fecha='sensing_start'
y1=0
y2=0
m1=0
m2=0
bs_1=0
bs_2=0
doit=False
for i in f:
	for j in f[pos:]:
        	d="/home/mario/Desktop/ALOS_insar/track152/"+`cont`
#		os.makedirs(d)
                if len(glob.glob(d+'/isceProc*')) is not 0:
                   with open(glob.glob(d+'/isceProc*')[0],'r') as fi:
    		        lines = fi.read().split("\n")
                   uno=False
                   for k,line in enumerate(lines):
                       if bs_top in line:
                          bs_1=(line.split('>')[1]).split('<')[0]
                       if bs_bottom in line:
                          bs_2=(line.split('>')[1]).split('<')[0]
                       if fecha in line and uno:
                          y2=(line.split('>')[1]).split('-')[0]
                          m2=(line.split('>')[1]).split('-')[1]
                       if fecha in line and not uno:
                          y1=(line.split('>')[1]).split('-')[0]
                          m1=(line.split('>')[1]).split('-')[1]
                          uno=True
                   tiempo1=float(y1)+float(m1)/12
                   tiempo2=float(y2)+float(m2)/12
                   tiempo=math.fabs(tiempo2-tiempo1)
                   if min([math.fabs(float(bs_1)),math.fabs(float(bs_2))])<300 and tiempo<2:
                      doit=True
                   else:
                      doit=False
                else:
                    doit=False    
                if doit:
        	   d1=d+"/insarApp.xml"
        	   ar=open(d1,"w+")
        	   ar.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<insarApp>\n<component name=\"insar\">\n<property name=\"Sensor Name\">\n<value>ALOS</value>\n</property>\n<property name=\"Unwrap\">\n<value>True</value>\n</property>\n<property name=\"unwrapper name\">\n<value>snaphu_mcf</value>\n</property>\n<property name=\"geocode bounding box\">\n<value>[0,2,-78,-76]</value>\n</property>\n<component name=\"Master\">\n<property name=\"IMAGEFILE\">\n<value>"+i+"/IMG-HH-"+(i.split("/")[7]).split("-")[0]+"-H1.0__A</value>\n</property>\n<property name=\"LEADERFILE\">\n<value>"+i+"/LED-"+(i.split("/")[7]).split("-")[0]+"-H1.0__A</value>\n</property>\n<property name=\"OUTPUT\">\n<value>master.raw</value>\n</property>\n</component>\n<component name=\"Slave\">\n<property name=\"IMAGEFILE\">\n<value>"+j+"/IMG-HH-"+(j.split("/")[7]).split("-")[0]+"-H1.0__A</value>\n</property>\n<property name=\"LEADERFILE\">\n<value>"+j+"/LED-"+(j.split("/")[7]).split("-")[0]+"-H1.0__A</value>\n</property>\n<property name=\"OUTPUT\">\n<value>slave.raw</value>\n</property>\n</component>\n<property name=\"range looks\">10</property>\n<property name=\"azimuth looks\">10</property>\n</component>\n</insarApp>")
		   ar.close()
                else:
                   print "no se hizo en la carpeta",cont  
                cont+=1
	pos+=1 		
