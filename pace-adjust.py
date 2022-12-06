import re
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
temp_file_path = file_path.replace(".tcx", "_corrected.tcx")

correct_distance = float(input('What is the shown distance on your treadmill (the correct one)?\n'))
wrong_distance = float(input('What is the shown distance on your smartwatch (the wrong one)?\n'))

correction_ratio = correct_distance / wrong_distance

file1 = open(file_path, 'r')
file2 = open(temp_file_path, 'w')

for line in file1:
    if re.match("            <DistanceMeters>", line):
        distance=re.findall(r'\d+\.\d+', line)
        distance1=str(float(distance[0]))
        distance_corrected=float(distance[0])*correction_ratio
        distance2=str(distance_corrected)
        file2.write(line.replace(distance1, distance2))
    else:
        file2.write(line)

file1.close()
file2.close()
