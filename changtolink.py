path = r"D:\Python\tangview\\youtube2.txt"
path2 = r"D:\Python\tangview\\list.txt"
file = open(path,"r",encoding='UTF8')
file2 = open(path2,"r+")
while True:
    line = file.readline()    
    if not line:
        break
    if line.find("/watch?v") >0:
        line = line[116:129]
        line = "https://www.youtube.com/watch?"+line
        file2.write(line+"\n")
        print(line)

file.close
file2.close