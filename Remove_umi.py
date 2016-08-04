#!/usr/bin/python
##This Script removes the UMI value from a FASTQ file and returns an Illumina approved header
import sys
import subprocess
import os.path

inFile = sys.argv[0]
outFile = sys.argv[1]

print ("The input file is %s") % inFile
print ("The output file is %s") % outFile

if os.path.isfile(inFile):
	pass
else:
	sys.exit("The file does not exist, you may want to use the absolute path")

print ("Removing UMI information...")

with open(inFile, 'r') as inFile:
	with open(outFile, 'a') as outFile:
		for line in inFile:
			if line.startswith("@"):
				new_line = line.strip('\n').split(':')
				remove_umi = new_line[7].split(' ')[1]
				remove_umi = ' ' + remove_umi
				updated_line = new_line[0:6]
				updated_line.append(remove_umi)
				updated_line = updated_line + new_line[8:len(new_line)]
				output_string = ":".join(updated_line)
				outFile.write(output_string + "\n")
			else:
				outFile.write(line)

print ("Success!")