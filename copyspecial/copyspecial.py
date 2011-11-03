#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

def findpaths(direct):
  #Find all special files in the passed directory
  filenames = os.listdir(direct)

  #Create the full path name for each file in the directory
  i = 0
  for files in filenames:
    filenames[i] = os.path.abspath(os.path.join(direct, files))
    i += 1

  #Find files with the __w__ pattern and add to new list
  special_files = []
  for files in filenames:
    if re.search(r'__\w+__\.', files):
      special_files.append(files)

  #Return the special files
  return special_files
    

def copyfiles(output_files, dest_dir):
  #output_files contains the full paths of all special files
 
  #Copy the files to the destination directory
  for files in output_files:
    shutil.copy(files, dest_dir)


def main():
  """
  Command line arguments don't work on Windows. Rewrite accordingly.
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  """
  # Call functions
  #Usual case is to run '.\\', but using the first one since it doens't require filer access
  directory = 'C:\Users\TBowland\Documents\Python\google-python-exercises\copyspecial'
  #directory = '..\\'

  #Get the destination directory
  #dest_dir = raw_input('Enter directory to which to copy: ')
  dest_dir = 'C:\Users\TBowland\Desktop'
  
  #Find the full path names of the special files in the directorey
  output_files = findpaths(directory)

  #Copy the files
  copyfiles(output_files, dest_dir)
  
if __name__ == "__main__":
  main()
