#!/usr/bin/python
#
# times.py
#
# Get the times for the observations
#
#
import sys 
from optparse import OptionParser
import os,os.path
import glob
from astropy.io import fits as pyfits
#import pyfits
#
# ------------------------------------------------------------------------------
#
# MAIN PROGRAM
#
#
#
version='0.1a'
date='- Tue Jul 21 11:16:23 EDT 2015 -'
author='Javier Garcia'
#
ul=[]
ul.append("usage: %prog [options] PREFIX")
ul.append("")
ul.append("Get total counts in different bands for a given observation")
ul.append("PREFIX can be a single PHA file or a group (e.g. *.pha)")
usage=""
for u in ul: usage+=u+'\n'

parser=OptionParser(usage=usage)
parser.add_option("-v","--version",action="store_true",dest="version",default=False,help="show version number")

(options,args)=parser.parse_args()

if options.version:
  print 'times.py version:',version,date
  print 'Author:',author
  sys.exit()

if len(args) == 0:
  parser.print_help()
  sys.exit(0)

#-----

# Get current directory
currpath = os.getcwd()

# Observations path
obspath='/Users/javier/crab-hexte/rebinned-clean-observations/'

# Change dir to observations path
os.chdir(obspath)

# List of spectrum files
files=glob.glob(args[0])

#----- LOOP OVER OBSERVATIONS ---#
for specfile in files:

  # Change dir to observations path
  os.chdir(obspath)

  # Check if specfile exist
  if not os.path.isfile(specfile):
    print 'Warning: spectrum file',specfile,'does not exist!'
    print 'Skiping...'

  else:  # Here I need to discriminate between pcu, mjd, etc...

    # Go back to the working directory
    #os.chdir(currpath)

    # Read spectrum file
    hdulist = pyfits.open(specfile)

    # Get response file name if not supplied (or multiple files)
    dateobs=hdulist[1].header['DATE-OBS']
    print specfile,dateobs
    #if not os.path.isfile(respfile):
    #  print 'Error: response file',specfile,'does not exist!'
    #  print 'Aborting...'
    #  sys.exit()

# Output
#
#
sys.exit()
# ------------------------------------------------------------------------------
