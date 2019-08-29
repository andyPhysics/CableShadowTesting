from icecube import icetray,dataio, clsim , dataclasses
import sys, os
from I3Tray import * 
from icecube.simprod.util import *
import icecube.simclasses

class ReturnPhotonSeries(icetray.I3ConditionalModule):
    def __init__(self,context):
        super(ReturnPhotonSeries,self).__init__(context)
        self.AddParameter("Count" , "Variable that keeps the count")
        self.AddParameter("PhotonSeries","Photons to be counted")
    def Configure(self):
        self.count = self.GetParameter("Count")
        self.photons = self.GetParameter("PhotonSeries")

    def Physics(self,frame):
        self.count.append(len(frame[self.photons])) 
        self.PushFrame(frame)

def count_photons(x):
# x is what is returned from self.count in ReturnPhotonSeries
    return x
