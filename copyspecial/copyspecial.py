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
import subprocess

"""Copy Special exercise
"""
def find_special_files(dir):
  filenames = os.listdir(dir)
  special_files = []
  for filename in filenames:
    match = re.search('.*__\w+__.*', filename)
    if (match):
      absolute_file = os.path.abspath(os.path.join(dir, filename))
      special_files.append(absolute_file)
  return special_files
  
def copy_files_to(files, destination):
  for file in files:
    print('copying %s to %s' % (file, todir))
    if not os.path.exists(todir):
      os.mkdir(todir)
    shutil.copy(file, todir)

def zip_files_to(files, tozip):
  command = '"C:\\Program Files\\7-Zip\\7z.exe" a -tzip {zipfile} {files_to_zip}'.format(zipfile=tozip, files_to_zip=' '.join(files))
  print('executing ' + command)
  (status, output) = subprocess.getstatusoutput(command)
  if status:
    print('error: ' + output)
    sys.exit(1)
	
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]");
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
    print("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  files = find_special_files(args[0])
  
  if todir:
    copy_files_to(files, todir)
  elif tozip:
    zip_files_to(files, tozip)
  else:
    print('\n'.join(files))
  
if __name__ == "__main__":
  main()
