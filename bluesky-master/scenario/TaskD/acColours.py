file = open('trafficSW.scn','r')
newFile = open('trafficSW_coloured.scn','w')

newLines = []
for line in file:
    # print(line[-10:])
    # break
    newFile.write(line)
    if 'DEST EHAM' in line:
        # Than we have toe define colour
        newFile.write(line[:-10] + "colour BLUE\r")

file.close()
newFile.close()