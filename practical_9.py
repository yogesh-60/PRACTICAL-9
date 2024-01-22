file=open("practical-9.txt",'w')
number=int(input("number:"))
for i in range(1,11):
    multiplication=number*i
    file.write(f"{number} x {i}={multiplication}\n")