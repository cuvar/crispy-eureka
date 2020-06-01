#!/usr/bin/python3

import exifread, imghdr, os, glob, sys, shutil, keyboard, sys, time


def checkDir(dir):
    if(dir[0] == "&"):
        dir = dir[1:]
    if(dir[0] == " "):
        dir = dir[1:]
    if(dir[0] == "\"") or (dir[0] == "\'"):     #remove front "
        dir = dir[1:]
    if(dir[len(dir) - 1] == "\"") or (dir[len(dir) - 1] == "\'"):  #remove back "
        dir = dir[:-1]
    
    return dir


#get dates of images	
def getDate(image):
    f = open(image, 'rb')
    tags = exifread.process_file(f, stop_tag='EXIF DateTimeOriginal')   #get tags until date & time
    try:
        dateTacken = str(tags['EXIF DateTimeOriginal'])[:10]            #only take date
    except KeyError:                                                    #if no date -> 0
        dateTacken = '0'
    return (image, dateTacken)


def convertDates(list):
    Dates = []
    for i in list:
        temp = i[1][:4] + i[1][5:7] + i[1][8:]           #re-arrange date yyyy:mm:dd
        Dates.append((i[0], temp))
    return Dates


def sortList(list):                     #sort list [min to max]
    for i in range(len(list)): 
        min_idx = i						#Find minimum in remaining unsorted array 
        for j in range(i+1, len(list)): 
            if int(list[min_idx][1]) > int(list[j][1]): 
                min_idx = j 

        tempa = list[i]          		#Swap found minimum with first element
        list[i] = list[min_idx]     
        list[min_idx] = tempa

    return list


def createDirs(list, src):
    for a in list:
        if not a[1] == "0":                         #if image has date data
            title = str(a[1][:4]+ "-"+ a[1][4:6])   #get dir name according to year & month
        
            if not os.path.exists(title):           #if dir not exists -> make it & move file
                os.mkdir(title)
                shutil.move(src + "\\" + str(a[0]), title)
            else:
                if os.path.exists(str(title) + "\\" + str(a[0])):   #replace exiting files
                    os.remove(str(title) + "\\" + str(a[0]))
                shutil.move(src + "\\" + str(a[0]), title)          #move file in existing dir
        
        
    if os.listdir(src) == []:   #remove dir if empty
        os.rmdir(src)
    else:
        dst = "sortDatepy unsorted"     #if !empty
        if not os.path.exists(dst):     #if "unsorted" !exists
            os.rename(src, dst)         #rename start dir
        else:
            for files in src:            #if "unsorted" exists
                print("\n\n" + str(file) + "\n\n")
                shutil.move(src + "\\" + str(files), dst + "\\" + str(files))  #move files in "unsorted"




#----------------------MAIN----------------------#
while True:
    os.system('cls')
    print("---------------------sortDate.py----------------------\n")
    
    dates = []              #list for unconverted dates
    
    #preparation
    src = input('Dir: ')	#get dir
    if src == "q":
        print("Exiting program")    #exit if 'q'
        break
    dir = checkDir(src)             #remove " at s[0] & s[len(s) -1]
    os.chdir(dir)                   #change to selected dir
    
    a = glob.glob('*')		                    #get all files
    elements = len(a)
    print("%d elements must be sorted" % elements) #print msg
    if elements == 0:
        print("Exiting program")        #exit if 0 elements
        break
    

    #getting dates
    print('Getting data')               #getting dates
    pBwidth = 40
    n = int(elements / pBwidth)         #n = 1% for progressbar
    if(n < 1):
	    n = 1

    sys.stdout.write("[%s]" % (" " * int(elements / n )))  #create progress bar
    sys.stdout.flush()
    sys.stdout.write("\b" * int((elements / n) +1))

    i = 0
    for file in a:
        if imghdr.what(file) != 'None':		#check if file is image
            dates.append(getDate(file))     #get date of every file
            i+=1
            if ((i % n) == 0):
                sys.stdout.write("-")       #update progress bar
                sys.stdout.flush()
    sys.stdout.write("\n")                  #ends the progress bar
            

    #converting dates
    convertedDates = convertDates(dates)	#convert list in right format
    print('Converted')

    #sorting dates
    sortedList = sortList(convertedDates)   #sort list from min to max
    print('Sorted')
    
    #move files
    os.chdir(dir + '\..')
    createDirs(sortedList, dir)             #create dirs for each month
    print('Moved data')
    print('Finish\n')                       #finish programm
    time.sleep(3.0)