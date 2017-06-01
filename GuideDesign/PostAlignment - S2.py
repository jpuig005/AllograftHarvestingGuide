import sys
sys.path.insert(0, 'C:\Users\jpuig005\Google Drive\UPF-Enginyeria Biomedica\TFG\Software\Meshmixer API\mm-api-master (1)\distrib\python')

import mmapi
from mmRemote import *

sys.path.insert(0, 'C:\Users\jpuig005\Google Drive\UPF-Enginyeria Biomedica\TFG\Software\Meshmixer API\mm-api-master (1)\python')

import mm
import os

# initialize connection

remote = mmRemote()
remote.connect()

#Select both files and check that the who files are selected

selected_objects = mm.list_selected_objects(remote)

# Duplicate the files

# 1 - Count the numbers of objects 

objects = mm.list_objects(remote)
num_objects = len(objects)

print num_objects

#Check that there are just two objects
if len(objects) != 2:
    print "You must have just two objects on the scene"
    raw_input("Press Enter to exit...")
    os._exit(1)

# 2 - Select the current objects and duplicate them

mm.select_objects(remote, objects)
mm.begin_tool(remote, "duplicate")
mm.begin_tool(remote, "duplicate")

obj = mm.list_objects(remote)
print "List of the objects: ", obj

#Hide all the objects but one glenoid and rename the files

name_list = ['Glenoid', 'Ampelt', 'LateralCutPlane', 'Lateral_guide', 'TopCutPlane','Top_guide']

iteration = 0

for i in obj[0:len(obj)]:
    mm.scene.set_object_name(remote, i, name_list[iteration])
    mm.Hidde_object(remote,i)
    print i, iteration
    iteration = iteration + 1

#Starting with the lateral cut:
    #Show the glenoid that will be used to create the lateral cut:
mm.Show_object(remote,obj[2])
    #Select just that object:
mm.select_object(remote, obj[2])

#Instructions

print "Nice"

mm.scene.save_mix(remote, "C:\Users\jpuig005\Google Drive\UPF-Enginyeria Biomedica\TFG\Software\Meshmixer API\GuideDesign\LateralDesign.mix")


remote.shutdown()
print "Remote has been shuted down"
