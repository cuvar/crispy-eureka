#!/usr/bin/python

import glob, os, filecmp, shutil

while(True):            
    temp_name = "AHALF - "  
    
    src = input('Directory: ')      #get dir
    
    if(src == 'q'):     #exit programm
        break   
    
    if(src.startswith('\"') or src.startswith('\'')):       #format string
        src = src[1:]
    if(src.endswith('\"') or src.endswith('\'')):
        src = src[:-1]    

    
    subdirs = [x[0] for x in os.walk(src)]          #get all subdirs of src
    subdirs.pop(0)

    for d in subdirs:
        os.chdir(d)
        os.chdir('..')
        temp = d.split('\\')
        src2 = d + '\\..' + '\\' + temp_name + temp[-1]    #create temp dir
    
        if not os.path.isdir(src2):
            os.mkdir(src2)          #make dir for dublicates 

        if d != '':
            os.chdir(d)
            liste = glob.glob('*.*')        #get all files
            j = 0
            for i in range(len(liste)):     #move every second
                if(i % 2):
                    j+= 1
                    print('Moved ' + liste[i]) 
                    shutil.move(liste[i] , src2)
        print('Moved ' + str(j) + ' files')
        print('Finished %s \n' %(d))
    



    temp = src.split('\\')      #create temp dir
    temp_src = src + '\\..' + '\\' + temp_name + temp[-1]
    if not os.path.isdir(temp_src):
        os.mkdir(temp_src)
    
    subdirs = [x[0] for x in os.walk(src)]  #move temp_dir in parent temp_dir
    subdirs.pop(0)

    print('Moving temp directories into %s...' % temp_src)
    for d in subdirs:
        if('AHALF' in d):
            shutil.move(d, temp_src)
            print('Moved ' + d) 

    print('Finished \n')
     