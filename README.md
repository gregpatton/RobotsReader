RobotsReader
============

A quick and dirty rewrite of Parsero for Python 2.7 that evaluates the Disallow entries of a robots.txt file for a given website.

Usage
=====
$ python robotsreader.py http://www.google.com

Output
======
A printed list of HTTP status codes from get requests to each disallow directory
