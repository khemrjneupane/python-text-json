import json

with open('text.txt','r') as fh:
    
    for line in fh:
        line = line.replace(' ',' ')
        line = line.replace('*','')
        line = line.replace('-','')
        line = line.strip()
        makefile = open("newFile.txt","a")   
        makefile.writelines(line+"\n")


with open("newFile.txt", "r") as inp, open('out.txt', 'w') as out:
    for line in inp:
        if line.strip():
            out.write(line)

 
dict1 = {} 
 
with open('out.txt',"r") as fh: 

	for line in fh:  
		command, description = line.strip().split(None, 1)
		dict1[command] = description.strip() 
out_file = open("finalJson.json", "w") 
json.dump(dict1, out_file, indent = 4, sort_keys = False) 
out_file.close()