#!/usr/bin/python

import os
import urllib
import urllib2
import xml.etree.ElementTree as ET


site_url = 'http://github-windows.s3.amazonaws.com/'
main_url = ''
manifest_path = ''
file_path = ''
suffix = '.deploy'

f = open('list.txt', 'w')


# Get & Parse Github.application
print 'Getting Github.application ...'
f.write(site_url + 'GitHub.application\n')
urllib.urlretrieve(site_url + 'GitHub.application', 'application')
tree = ET.parse('application')
root = tree.getroot()
for e in root.findall('.//*[@codebase]'):
	manifest_path = e.attrib['codebase'].replace('\\', '/')


# Get & Parse Manifest
print 'Getting GitHub.exe.manifest ...'
f.write(site_url + manifest_path + '\n')
urllib.urlretrieve(site_url + manifest_path, 'manifest')
tree = ET.parse('manifest')
root = tree.getroot()
main_url = site_url + os.path.dirname(manifest_path)
for e in root.findall('.//*[@size]'):
	try:
		file_path = main_url + '/' + e.attrib['codebase'].replace('\\', '/') + suffix
	except:
		file_path = main_url + '/' + e.attrib['name'].replace('\\', '/') + suffix
	f.write(file_path + '\n')
	
f.close()
os.remove('application')
os.remove('manifest')

print 'Done!'