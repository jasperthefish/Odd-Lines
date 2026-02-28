# Write a Python program to copy odd lines from one file to another.

file_r = open("Codingal.txt", "r")
file_w = open("Codingal_Odd.txt", "w")

file_r_n = file_r.readlines()

for i in range(1, len(file_r_n)+1, 2):
    file_w.write(file_r_n[i-1])