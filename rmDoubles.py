#!/usr/bin/python

import glob, os, filecmp, shutil


def getFiles(path):
    if path != '':
        os.chdir(path)
        a = glob.glob('*(1).*')
        for doubledFile in a:
            if doubledFile == doubledFile.replace(' (1)', ''):
                a.remove(doubledFile)
        global num
        num = len(a)
        print('\n')
        return a
    else:
        print('No input')
        return -1


def checkDuplicates(b):
    for f1 in b:
        if (('(1)' in f1) and os.path.exists(f1.replace(' (1)', ''))):
            print('Moved ' + f1)
            shutil.move(f1 , src2)

while(True):            
    src = input('Directory: ')      #get dir
    if(src == 'q'):
        break   
    if(src.startswith('\"') or src.startswith('\'')):
        src = src[1:]
    if(src.endswith('\"') or src.endswith('\'')):
        src = src[:-1]    
    
    temp = src.split('\\')
    src2 = src + '\\..' + '\\ATEMP - ' + temp[-1]    #temp dir

    if not os.path.isdir(src2):
        os.mkdir(src2)          #make dir for dublicates 
    fileDoublicates = getFiles(src)       #get doublicates in a list
    if fileDoublicates != -1:
        checkDuplicates(fileDoublicates)      #delete doublicates
        print('Moved ' + str(num) + ' doubled files')
    print('Finished \n')