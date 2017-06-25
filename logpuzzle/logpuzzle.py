#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def secondWorIfPresent(url):
  matches = re.search('(\w+)-(\w+)\.\w+', url)
  second_word = matches.groups()[1:]
  if second_word:
    return second_word
  else:
    return url

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  file = open(filename)
  text = file.read()
  file.close()
 
  urls = re.findall('GET\s(\S+puzzle\S+)\s', text)
  
  host = filename.split('_')[1]  
  urls = [host + url for url in urls]
  urls = sorted(set(urls), key=secondWorIfPresent)
  return urls


  
def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
	
  indexhtml = setup_indexhtml(dest_dir)
  
  urls = list(enumerate(img_urls))
  for (index, img_url) in urls:
    img_name = 'img{}'.format(index)
    download_image_to(img_url, dest_dir, img_name)
    add_img_ref_to_file(indexhtml, img_name)
	
  finish_and_close_indexhtml(indexhtml)
	
def setup_indexhtml(dest_dir):
  indexhtml_path = os.path.join(os.path.abspath(dest_dir), 'index.html')
  indexhtml = open(indexhtml_path, 'w')
  indexhtml.write('<html><body>')
  return indexhtml
  
def download_image_to(url, dir, filename):
  path = os.path.join(os.path.abspath(dir), filename)
  print('downloading to file ' + path + ' from http://' + url)
  urllib.request.urlretrieve('http://' + url, path)

def add_img_ref_to_file(file, ref):
  file.write('<img src="{}">'.format(ref))
	
def finish_and_close_indexhtml(indexhtml):
  indexhtml.write('</body></html>')
  indexhtml.close()
	
def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print('\n'.join(img_urls))

if __name__ == '__main__':
  main()
