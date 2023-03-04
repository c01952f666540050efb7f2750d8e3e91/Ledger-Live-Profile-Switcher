ret_data = []
with open("cal_chains.txt", 'r') as openfile:
    data = openfile.read().replace(" ", "").replace("\n", "").replace("||", "|")
    splitdata = data.split("|")
    for cell in range(len(splitdata)):
        if splitdata[cell] == "YES":
            ret_data.append(splitdata[cell+1])
    
print(ret_data)