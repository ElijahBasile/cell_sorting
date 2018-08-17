
from PySteppables import *
import CompuCell
import sys
class cell_sortingSteppable(SteppableBasePy):

    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    def start(self):
        for cell in self.cellList:
            cell.targetVolume = 20.0
            cell.lambdaVolume = 10.0
#     def step(self,mcs):        
#         #type here the code that will run every _frequency MCS
# #         for cell in self.cellList:
# #             print "cell.id=",cell.id
    def finish(self):
        # Finish Function gets called after the last MCS
        pass
        