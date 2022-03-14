#this is an attempt to delete duplicate lines

import hashlib

completed_lines_hash = set()

#3
output_file = open('filtered-summedscen-daan.scn', "w")

#4
for line in open('summedscen_daan.scn', "r"):
  #5
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  #6
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
#7
output_file.close()