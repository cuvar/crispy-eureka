import os

src = input('Directory: ')      #get dir
if(src.startswith('\"') or src.startswith('\'')):
    src = src[1:]
if(src.endswith('\"') or src.endswith('\'')):
    src = src[:-1] 



subdirs = [os.path.join(src, o) for o in os.listdir(src) if os.path.isdir(os.path.join(src,o))]

subdirs2 = [x[0] for x in os.walk(src)]

print(subdirs)
print(subdirs2)