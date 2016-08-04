##This Script removes the UMI value from a FASTQ file and returns an Illumina approved header


inFile = "AB_Z15_4220_C1_S43_L004_R1_001.fastq"
outFile = "umiABZ154220C1_S43_L004_R1_001.fastq"

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
				outFile.write("@" + output_string + "\n")
			else:
				outFile.write(line)