#!/usr/bin/env python 

from icecube import icetray,dataio, clsim , dataclasses,phys_services
import sys, os
from I3Tray import *
from icecube.simprod.util import *
import icecube.simclasses
from icecube.clsim.shadow import *
from icecube.simclasses import I3CylinderMap
from os.path import expandvars
from generateEvent import *

cable_map = I3CylinderMap()

outfile = sys.argv[1]
seed = int(sys.argv[2])

randomService = phys_services.I3SPRNGRandomService(
    seed = 1,
    nstreams = 100000,
    streamnum = seed)


gcd_file = "GeoCalibDetectorStatus_2013.56429_V1.i3.gz"

tray = I3Tray()

tray.AddModule("I3InfiniteSource" , "streams" , Prefix=expandvars(gcd_file),Stream = icetray.I3Frame.DAQ)

tray.Add(AddCylinders , Cable_map = cable_map ,Length_of_cylinder = 17.0, Radius_of_cylinder = 0.023)

tray.Add("Dump")

tray.AddModule("I3MCEventHeaderGenerator","gen_header",
               Year = 2009,
               DAQTime=158100000000000000,
               RunNumber=1,
               EventID=1,
               IncrementEventID=True)

tray.AddModule(generateEvent , "generateEvent",
               Type = dataclasses.I3Particle.ParticleType.EMinus,
               NEvents = 1,
               XCoord = 0,
               YCoord = 0,
               ZCoord = 0,
               Primary_direction = dataclasses.I3Direction(0 , 0 ,1),
               Daughter_direction = dataclasses.I3Direction(0 , 0 , 1),
               I3RandomService = randomService,
               Energy = 1000.0*I3Units.TeV )

photonSeriesName = "Photons"
MCTreeName = "I3MCTree"
MMCTrackListName= None


tray.AddSegment(clsim.I3CLSimMakePhotons,"MakePhotons",
                UseGPUs = False,
                UseCPUs = True,
                PhotonSeriesName = photonSeriesName,
                MCTreeName = MCTreeName,
                MMCTrackListName = MMCTrackListName,
                RandomService = randomService,
                IceModelLocation = expandvars("$I3_BUILD/ice-models/resources/models/spice_lea"),
                GCDFile = gcd_file
            )


tray.AddModule("I3ShadowedPhotonRemoverModule",
               "PhotonRemover",
               InputPhotonSeriesMapName = "Photons",
               OutputPhotonSeriesMapName = "ShadowedPhotons",
               Cable_Map = "CableMap",
               Distance = 125.0)


tray.AddModule("I3NullSplitter","physics")

tray.Add("I3Writer","writer",filename=outfile)

tray.Execute()
tray.Finish()
