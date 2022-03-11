file = open('trafficSW_coloured.scn','r')
newFile = open('trafficSW_coloured_sid.scn','w')

newLines = []
for line in file:
    # print(line[-10:])
    # break
    newFile.write(line)
    if '52.3045649 4.77753518' in line:
        # Than we have toe define colour
        newFile.write(line[:12] + line[16:-35] + "call taskD/SIDkaag \r")

    if '52.316237886827594 4.779730245101439' in line:
        # Than we have toe define colour
        newFile.write(line[:12] + line[16:-35] + "call taskD/SIDkaag \r")

file.close()
newFile.close()