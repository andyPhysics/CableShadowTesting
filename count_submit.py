from countPhotons import *
from icecube import icetray,dataio, clsim , dataclasses
import sys, os
from I3Tray import *
from icecube.simprod.util import *
import icecube.simclasses



input_file = raw_input("What file: ")

x=[]
y=[]

tray2 = I3Tray()


tray2.Add("I3Reader" , "my_reader" , FileNameList =  [input_file]  )
tray2.Add(ReturnPhotonSeries,Count=x,PhotonSeries="Photons")
tray2.Add(ReturnPhotonSeries,Count=y,PhotonSeries="ShadowedPhotons")

tray2.Execute()
tray2.Finish()

x1 = count_photons(x)

x2 = count_photons(y)

print(x1)
print(x2)
