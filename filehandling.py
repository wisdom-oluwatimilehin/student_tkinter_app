import os

new_dir = 'C:\\Users\\HP\\newdir'
os.chdir(new_dir)

namelist = open('names.txt','w')

namelist.write('Reuben \n')

namelist.close()

namelist = open('names.txt','a')

namelist.write('Root')

namelist.close()

f =  open('names.txt','r')
content = f.read()
print(content)

