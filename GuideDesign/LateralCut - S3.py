import sys
sys.path.insert(0, 'C:\Users\jpuig005\Google Drive\UPF-Enginyeria Biomedica\TFG\Software\Meshmixer API\mm-api-master (1)\distrib\python')

import mmapi
from mmRemote import *

sys.path.insert(0, 'C:\Users\jpuig005\Google Drive\UPF-Enginyeria Biomedica\TFG\Software\Meshmixer API\mm-api-master (1)\python')

import mm
import os

# File

examples_dir = os.getcwd()
part_filename = os.path.join( examples_dir, "TubeShortFat.stl" )


# initialize connection

remote = mmRemote()
remote.connect()

#Put the pivots

    #Initialize "create pivot" tool:

mm.begin_tool(remote, "createPivot")

    #Wait for the user:

raw_input("Press Enter once the two 5 pairs of pivots are correctly placed")

#Hide the object

obj = mm.list_objects(remote)
mm.Hidde_object(remote,obj[2])

#Placing and alignment of the tube + holder

print "Place the 5 tubes and align them with each pivot"

for i in range(0,5):
    #Load the tubeHolder and rename it
    mm.scene.append_objects_from_file(remote, part_filename)
    #Beggin alignment tool
    mm.begin_tool(remote, "align")
    raw_input("Press enter when the tube is align to the pivot")
    #Beggin the translation tool
    mm.accept_tool(remote)
    mm.begin_tool(remote, "transform")
    raw_input("Press enter when the tube is aligned")
    mm.accept_tool(remote)

#Rename the tubes

obj_list = mm.list_objects(remote)
print obj_list

for i in range(6,11):
    print i
    print obj_list[i]
    mm.set_object_name(remote, obj_list[i+10], "Tube%d" %(i-5))


mm.scene.save_mix(remote, "C:\Users\jpuig005\Google Drive\UPF-Enginyeria Biomedica\TFG\Software\Meshmixer API\GuideDesign\LateralDesign.mix")

    
remote.shutdown()
print "Remote has been shuted down"


