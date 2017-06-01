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

print "It is necessery to manualy eliminate the pivots"

raw_input("Remove the pivots")

objList = mm.list_objects(remote) 
Tubes_list = ["Tube1", "Tube2", "Tube3", "Tube4", "Tube5"]

for i, name in enumerate(Tubes_list):
    mm.select_object_by_name(remote, name)
    mm.begin_tool(remote, "transform")
    mm.tool_utility_command(remote, "coordinateSpace", 1)
    raw_input("Press enter when the object is positioned")
    mm.accept_tool(remote)

raw_input("Press enter if the tubes are in place")


for i, name in enumerate(Tubes_list):
    mm.select_object_by_name(remote, name)
    mm.begin_tool(remote, "separateShells")

Tubes = ["Tube1 (shell 1)", "Tube2 (shell 1)", "Tube3 (shell 1)", "Tube4 (shell 1)", "Tube5 (shell 1)"]
Shells = ["Tube1 (shell 2)", "Tube2 (shell 2)", "Tube3 (shell 2)", "Tube4 (shell 2)", "Tube5 (shell 2)"]

mm.select_objects_by_name(remote, Tubes) # -> Called Tube1 (shell 1)
mm.begin_tool(remote, "combine")

mm.select_objects_by_name(remote, Shells)# -> Called Tube1 (shell 2)
mm.begin_tool(remote, "combine")

#Make the boolean difference

mm.select_object_by_name(remote, "Tube1 (shell 1)")
mm.begin_tool(remote, "makeSolid")

raw_input("Put the good parameters and press Enter")

mm.select_objects_by_name(remote, ["Lateral_guide", "Tube1 (shell 1) (solid)"])
mm.begin_tool(remote, "difference")
mm.accept_tool(remote)

mm.select_object_by_name(remote, "Tube1 (shell 2)")
mm.begin_tool(remote, "makeSolid")

raw_input("Put the good parameters and press Enter")

mm.select_objects_by_name(remote, ["Lateral_guide", "Tube1 (shell 2) (solid)"])
mm.begin_tool(remote, "union")
mm.accept_tool(remote)

mm.scene.save_mix(remote, "C:\Users\jpuig005\Google Drive\UPF-Enginyeria Biomedica\TFG\Software\Meshmixer API\GuideDesign\LateralDesign.mix")


remote.shutdown()
print "Remote has been shuted down"


