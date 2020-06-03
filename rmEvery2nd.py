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

    
    os.chdir(src)
    os.chdir('..')
    temp = src.split('\\')
    src2 = src + '\\..' + '\\' + temp_name + temp[-1]    #create temp dir
    
    if not os.path.isdir(src2):
        os.mkdir(src2)          #make dir for dublicates 

    if src != '':
        os.chdir(src)
        liste = glob.glob('*.*')        #get all files
        j = 0
        for i in range(len(liste)):     #move every second
            if(i % 2):
                j+= 1
                print('Moved ' + liste[i]) 
                shutil.move(liste[i] , src2)
    
    print('Moved ' + str(j) + ' files')
    print('Finished \n')
     