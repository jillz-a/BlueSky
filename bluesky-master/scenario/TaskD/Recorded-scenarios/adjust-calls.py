#this code is to replace commands in scn files with the call function

recording = input("What's the filename?\n")

file = open(recording+'.scn', 'r')
newfile = open(recording+'-adjusted.scn', 'w')

note = 0
for count, line in enumerate(file):
    if 'ADDWPT IAFNW' in line:
        newfile.write(line[:19] + line[16:-35] + "call taskD/iafnw \r")
        note = count + 4
    if 'ADDWPT IAFNE' in line:
        newfile.write(line[:19] + line[16:-35] + "call taskD/iafne \r")
        note = count + 7
    if 'ADDWPT IAFSW' in line:
        newfile.write(line[:19] + line[16:-35] + "call taskD/iafsw \r")
        note = count + 5
    if 'ADDWPT IAFSE' in line:
        newfile.write(line[:19] + line[16:-35] + "call taskD/iafse \r")
        note = count + 9
    if 'ADDWPT VLK02 120' in line:
        newfile.write(line[:19] + line[16:-35] + "call taskD/klu_inbound \r")
        note = count + 9
    if 'ADDWPT VKL03' in line:
        newfile.write(line[:19] + line[16:-35] + "call taskD/klu_outbound \r")
        note = count + 9
    if count > note or 'CRE' in line:
        newfile.write(line)