#this code is to replace commands in scn files with the call function

file = open('eham-jilles-03.scn', 'r')
newfile = open('eham-jilles-03-adjusted.scn', 'w')

note = 0
for count, line in enumerate(file):
    if 'ADDWPT IAFNW' in line:
        newfile.write(line[:19] + line[16:-35] + "call taskD/iafnw \r")
        note = count + 9
    if 'ADDWPT IAFNE' in line:
        newfile.write(line[:19] + line[16:-35] + "call taskD/iafne \r")
        note = count + 9
    if 'ADDWPT IAFSW' in line:
        newfile.write(line[:19] + line[16:-35] + "call taskD/iafsw \r")
        note = count + 9
    if 'ADDWPT IAFSE' in line:
        newfile.write(line[:19] + line[16:-35] + "call taskD/iafse \r")
        note = count + 9
    if count > note or 'CRE' in line:
        newfile.write(line)