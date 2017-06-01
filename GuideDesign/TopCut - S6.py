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

#Iterate over the holder + Tube and positionate them

#Tubes_list = ["Tube1", "Tube2", "Tube3", "Tube4", "Tube5"]
#mm.select_objects_by_name(remote, Tubes_list)

#obj_list = mm.list_objects(remote)
#out = mm.find_object_by_name(remote, Tubes_list[0])

#print obj_list
#print out[1]

#for i, val in enumerate(Tubes_list):
#    print i, val

#mm.select_object_by_name(remote, Tubes_list[0])
#mm.set_object_namename(remote, "Tube1_shell", "Tube1")

mm.select_object_by_name(remote, "Tube ")

raw_input("Press enter to exit...")

mm.scene.save_mix(remote, "C:\Users\jpuig005\Google Drive\UPF-Enginyeria Biomedica\TFG\Software\Meshmixer API\GuideDesign\LateralDesign.mix")


remote.shutdown()
print "Remote has been shuted down"


