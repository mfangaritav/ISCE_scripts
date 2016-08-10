import os
import glob

'''
Script to make Sentinel interferogram
'''
d="/home/mario/Desktop/Sentinel_insar/A120/sub_1/"
d1="/home/mario/Desktop/Sentinel_insar/A120/sub_2/"
d2="/home/mario/Desktop/Sentinel_insar/A120/sub_3/"
f1=glob.glob(d+"*")
f2=glob.glob(d1+"*")
f3=glob.glob(d3+"*")
f=[]
for k in f1:
    f.append(k)
for k in f2:
    f.append(k)
for k in f3:
    f.append(k)
for k in f:
    os.system("cd "+os.path.abspath(k)+"; topsApp.py --steps | tee topsApp.log; cd ..")
