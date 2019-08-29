# file name: job.condor
Executable = /home/amedina/ShadowTest/test_shadow.py
output = test.out
error = test.err
log = job.log
notification = never
request_cpus = 10

arguments = $(Item)

# use the current metaproject environment
getenv = True


queue 1 Item from arguments.txt
