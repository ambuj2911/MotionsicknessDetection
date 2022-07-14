
# Take Videos from Dataset folder
# Call functionalities from different folders.
# Store Extracted Features in proper format in Features Folder.
from Saliency import saliency
from Velocity import velocity
from Disparity import Disparity
object = saliency.Saliency()
obj_velo = velocity.velocity()
obj_dis = Disparity.Disparity()
object.myfunc('Saliency\AirFighter_0.mp4')
#obj_velo.calc_velocity('Velocity\AirFighter_0.mp4')
#obj_dis.disparity('Disparity\AirFighter_0.mp4')

















