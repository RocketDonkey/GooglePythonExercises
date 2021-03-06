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
 -Get the names data into a dict and print it DONE
 -Build the [year, 'name rank', ... ] list and print it DONE
 -Fix main() to use the extract_names list DONE
 -Practice posting this to GitHub! SWEET.
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

  if year_regex:year = year_regex.group(1)
  else: year = 'No year found.'
  
  #Names and rank: rank (group 1), Male (group 2), Female (group 3)
  names_ranks = re.findall(r'<tr align=\"right\"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', file_output)
  
  
  #Create a dictionary of ranks and names
  names_dict = {}
  for items in names_ranks:
    names_dict[items[2]] = items[0]

  #Sort the dictionary and add to a list
  names_list = [year] #Create the list and pre-populate with year
  for key in sorted(names_dict.keys()):
    names_list.append(key + ' ' + names_dict[key])

  text = '\n'.join(names_list) + '\n'

  print text

  return


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  """
  args = sys.argv[1:]
  #Don't have Python in the path, so I can't pass arguments (sweet)
  #Changing it to accept a filename on input

  args = None
  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
  """

  #Accept input (sys.argv doesn't work due to a path issue)
  file_input = raw_input('Enter filename: ')
  #file_input = 'baby1990.html'
  
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  extract_names(file_input)
  
if __name__ == '__main__':
  main()
