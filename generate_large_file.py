#! \usr\bin\python3

file = open("2.txt", "r")
f = open("3.txt", "w")

s = file.read()

for i in range(1):
    f.write(s)

file.close()
f.close()

