import sys
sys.path.insert(0, 'C:\Users\jpuig005\Google Drive\UPF-Enginyeria Biomedica\TFG\Software\Meshmixer API\mm-api-master (1)\distrib\python')

import mmapi
from mmRemote import *

sys.path.insert(0, 'C:\Users\jpuig005\Google Drive\UPF-Enginyeria Biomedica\TFG\Software\Meshmixer API\mm-api-master (1)\python')

import mm
import os

# Names of the files to use:

# - Fractured bone name:

fr_bone = "Glenoid.stl"

# - Death bone nema:

dt_bone = "Pilo.stl"

# File

examples_dir = os.getcwd()
part_filename_1 = os.path.join( examples_dir, fr_bone )
part_filename_2 = os.path.join( examples_dir, dt_bone )


# initialize connection

remote = mmRemote()
remote.connect()

#Loading file

print "Loading ", fr_bone
mm.scene.append_objects_from_file(remote, part_filename_1)
print "Loading ", dt_bone
mm.scene.append_objects_from_file(remote, part_filename_2)

#Instructions

print "To cliniciant: Align the two bones so as they fit together"



mm.scene.save_mix(remote, "C:\Users\jpuig005\Google Drive\UPF-Enginyeria Biomedica\TFG\Software\Meshmixer API\GuideDesign\LateralDesign.mix")
remote.shutdown()
print "Remote has been shuted down"


