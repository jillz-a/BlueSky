#this is an attempt to delete duplicate lines

import hashlib

completed_lines_hash = set()

#3
output_file = open('final-merge.scn', "w") #OUTPUT file

#4
for line in open('taskD-total-daan-05-adjusted.scn', "r"): #INPUT file
  #5
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  #6
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
#7
output_file.close()
