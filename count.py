from countPhotons import *
from icecube import icetray,dataio, clsim , dataclasses
import sys, os
from I3Tray import *
from icecube.simprod.util import *
import icecube.simclasses



file_directory = "/data/user/amedina/shadow/"
files = os.listdir(file_directory)
files_new = [file_directory+i for i in files]

x=[]
y=[]

tray2 = I3Tray()


tray2.Add("I3Reader" , "my_reader" , FileNameList =  files_new[0:10]  )
tray2.Add(ReturnPhotonSeries,Count=x,PhotonSeries="Photons")
tray2.Add(ReturnPhotonSeries,Count=y,PhotonSeries="ShadowedPhotons")

tray2.Execute()
tray2.Finish()

x1 = count_photons(x)

x2 = count_photons(y)

x3 = [i-j for i,j in zip(x1,x2)]

print(x3)
