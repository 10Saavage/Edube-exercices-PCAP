from os import strerror
import time

srcname = input("Enter the source filename: ")

try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)

dstname = input("Enter the destination file name: ")
start_time = time.time()
try:
    dst = open(dstname, 'wb')
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)

buffer = bytearray(65536)
total = 0
nbrItteration = 0

try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
        print(readin)
        nbrItteration += 1
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)

print(total, 'byte(s) succesfully written')
print("nombre d'itteration:", nbrItteration)
print("--- {} seconds ---".format(round(time.time() - start_time, 10)))
src.close()
dst.close()
