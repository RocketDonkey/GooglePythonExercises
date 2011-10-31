#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import urllib2

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

#Global URL variable
#puzzle_urls = []

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  f = open(filename, 'rU')
  log_contents = f.read()

  #Get the path of the hostname
  hostname = 'http://' + re.search(r'\_([\w\.]+)', filename).group(1)
  
  #Pull URLs with "puzzle" in the path
  puzzle_urls = re.findall(r'\"GET\s([^\s]+puzzle[^\s]+)\s*\w', log_contents)

  #Combine hostname and puzzle_urls
  for i in range(0, len(puzzle_urls)):
    puzzle_urls[i] = hostname + puzzle_urls[i]
    
  #Filter for uniques
  unique_urls = set(puzzle_urls)
  puzzle_urls = list(unique_urls)

  #Sort the URLs. Use a special sort if 'place_' file is specified
  if filename == 'animal_code.google.com':
    puzzle_urls.sort()
  elif filename == 'place_code.google.com':
    puzzle_urls = sorted(puzzle_urls, key=URL_sort)
    #sorttest = open('SORTTEST.txt', 'w')
    #sorttest.write('\n'.join(puzzle_urls))
            
  return puzzle_urls

def URL_sort(URL):
  #Look for the matching pattern
  key = re.search(r'\-\w+\-(\w+)\.jpg', URL)
  
  #If URL ends in '-words-words.jpg', use the second
  #'words' as the sort key. Otherwise, use the part before .jpg
  if key.group(1):
    URL_key = key.group(1)
  else:
    URL_key = re.search(r'\/([\w\-]+)\.jpg', URL).group(1)

  return URL_key

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """

  #If the directory doesn't exist, create it
  if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

  #Create HTML file
  image_file = open(dest_dir + '\\SecretImage.html', 'w')
  image_file.write('<html>')
  image_file.write('<body>')
  
  """
  Loop through each URL, downloading the image and appending
  the HTML output with the proper tag that calls the image
  """
  #Sentinel for img number
  i = 0
  
  for URL in img_urls:

    #Create the files
    filename = 'img' + str(i) + URL[-4:]
    filedirname = dest_dir + '\\' + filename

    #Print status
    print 'Retrieving: ' + filename

    #Download the image
    image_url = urllib.urlretrieve(URL, filedirname)

    #Add the proper HTML to the HTML file to create the full image
    image_file.write('<img src =\"' + filename + '\">')

    #Increment number in filename
    i += 1

def main():
  """
  Since pathing is all bamboozled on the work computer, reconfigure to just
  run off of the specified file.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)
  """
  #Read all URLs from the log file
  puzzle_urls = read_urls('place_code.google.com')

  #Combine them all into one image
  download_images(puzzle_urls, 'ImageFolder')
  
if __name__ == '__main__':
  main()
