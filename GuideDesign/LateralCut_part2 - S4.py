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

#Show and select the death bone that will become the lateral guide

obj = mm.list_objects(remote) 

mm.Show_object(remote,obj[3])
mm.select_object(remote, obj[3])

mm.begin_tool(remote, "select")

raw_input("Select the area and then press Enter to generate the guide base")

#Generate the guide

    #Invert Selection
mm.selection_utility_command(remote, "invert")
    #Delete surface
mm.begin_tool(remote, "discard")
    #Select All
mm.select_all(remote)
    #Smooth boundary
mm.begin_tool(remote, "smoothBoundary")
mm.accept_tool(remote)
    #Extrude
mm.begin_tool(remote, "extrude")
mm.set_toolparam(remote, "offset", 0.103)
mm.accept_tool(remote)

mm.scene.save_mix(remote, "C:\Users\jpuig005\Google Drive\UPF-Enginyeria Biomedica\TFG\Software\Meshmixer API\GuideDesign\LateralDesign.mix")


remote.shutdown()
print "Remote has been shuted down"


