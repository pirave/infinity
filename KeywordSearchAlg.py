import os

def rec_search(path):
    for f in os.listdir(path):
        if f.endswith(".py"):
            r = open(path + "/"+f).read()
            if keyword in r.lower():
                print path + "/" + f
                lines = r.split("\n")
                lineNum = [str(i + 1) for i in range(len(lines)) if keyword in lines[i]]
                print "\tLines: " + ", ".join(lineNum)+ "\n"
        elif (os.path.isdir(path + "/" + f)):
            rec_search(path + "/" + f)

keyword = "HAHA"
while keyword != "":
    print
    keyword = raw_input("Enter the keyword to search for: ").lower()
    rec_search("matplotlib")