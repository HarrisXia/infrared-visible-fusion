# -*- coding=utf-8 -*- 
import os
import pdb
import re
import sys


def main(path):
    #pdb.set_trace()##############
    for root, dirs, files in os.walk(path):
        #os.path.join(dirpath, dirnames)
        print(root)
        #print(dirs)
        files.sort()
        print(files)
        #os.system('cd '+path)
        
        for file in files:
            with open(path+'/'+file, "r+") as f:
                p = re.compile("MI")
                lines = [line for line in f.readlines() if p.search(line) is None]
                f.seek(0)
                f.truncate(0)
                f.writelines(lines)

            with open(path+'/'+file, "r+") as f:
                lines = f.readlines()
                line_list =['' for n in range(len(lines))]
                #pdb.set_trace()
                count = 0
                for line in lines:
                    line = line.replace('    ',',')
                    line = line.replace('   ',',')
                    line = line.replace('\n','')
                    line_list[count]=line
                    count +=1
                #pdb.set_trace()
                line_list[0]=line_list[0].lstrip(',')
                f.seek(0)
                f.truncate(0)
                f.writelines(line_list)
            with open(path+'/'+file, "r+") as f:
                line_list = f.readlines()  
                insert_list=[i.start() for i in re.finditer(',', line_list[0])]
                print(insert_list)
                #pdb.set_trace()
                list_i = list(line_list[0])
                #print(list_i)
                #pdb.set_trace()
                count = 0
                for num in range(34):
                    list_i.insert(insert_list[5+6*count]+count+1, '\n')
                    count +=1                     
                line_list[0] = ''.join(list_i)
                #line_list
                f.seek(0)
                f.truncate(0)
                f.writelines(line_list)  


path = './test'
main(path)
