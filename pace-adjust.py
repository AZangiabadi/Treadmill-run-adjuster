import re
file = open(os.path.expanduser("~/Downloads/Evening_Run1.tcx"), 'r')
for line in file:
    if re.match("            <DistanceMeters>", line):
        aa=re.findall(r'\d+\.\d+', line)
        bb=float(aa[0])*1.2
        print(bb)
        file.write(line = "            <DistanceMeters>"+str(bb)+"</DistanceMeters>")
    file.write(line)
#contents = file.read()

file.close()

with open(os.path.expanduser("~/Downloads/Evening_Run1.tcx"), 'r') as file :
  filedata = file.read()
print(filedata)
