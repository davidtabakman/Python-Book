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


"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
    try:
        with open(filename, 'r') as log_file:
            url_list = []
            for line in log_file:
                if not get_url(line) is None:
                    url_list.append(get_url(line))
            url_list = remove_duplicates(url_list)
            url_list.sort(key=sort_filename_key)
            return url_list
    except Exception, e:
        print e


def get_url(line):
    """Returns the url as a string
    Args:
        line - a string of a line in a log file
    Return value:
        String of the full url (with added host), or if there is no url in line return None
    """
    url_start = line.find('GET')
    url_end = line.find('.jpg')
    if url_start == -1 or url_end == -1:
        return None
    url_start += 4
    url_end += 4
    return "http://data.cyber.org.il" + line[url_start:url_end]


def remove_duplicates(list_from):
    """Removes all duplicates in list and returns the new list
    """
    i = 0
    while i < len(list_from)-1:
        y = i + 1
        while y < len(list_from):
            if list_from[y] == list_from[i]:
                list_from.pop(y)
            else:
                y += 1
        i += 1
    return list_from


def sort_filename_key(url):
    """Sort by filename key
    """
    url = str(url)
    filename_from = url.rfind('/')
    filename_to = url.rfind('.')
    return url[filename_from:filename_to+1]


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
    img_names = []
    counter = 0
    for url in img_urls:
        try:
            #Download the image and add it to a list with its new name
            path = dest_dir + '\\' + str(counter) + '.jpg'
            urllib.urlretrieve(url, path)
            img_names.append(str(counter) + '.jpg')
            counter += 1
        except Exception, e:
            print e
    create_html_file(img_names, dest_dir)


def create_html_file(img_names, dest_dir):
    """Creates an index.html file in the specified directory (creates it if
    it doesn't exist)
    Args:
        img_names - names of all the images in this folder that should be shown
        dest_dir - the path to this folder"""
    #If the directory doesn't exist, create it
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    full_path = dest_dir + r'\index.html'

    with open(full_path, 'w+') as index_file:
        #Writes the HTML code in the file (manually)
        index_file.write('<verbatim>\n<html>\n<body>\n')
        for img_name in img_names:
            index_file.write('<img src="')
            index_file.write(str(img_name))
            index_file.write('">')
        index_file.write('\n</body>\n</html>')


def main():
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


if __name__ == '__main__':
    main()
