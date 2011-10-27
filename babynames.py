#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

Suggested milestones for incremental development:
 -Extract the year and print it DONE
 -Extract the names and rank numbers and just print them DONE
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  #File contents
  filer = open(filename, 'rU')
  file_output = filer.read()

  #Year
  year_regex = re.search(r'<h3 align=\"center\">Popularity\s*in\s*(\d+)</h3>', file_output)
  
  #Names and rank: rank (group 1), Male (group 2), Female (group 3)
  re.findall(r'<tr align=\"right\"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', file_output)
  

  return


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
