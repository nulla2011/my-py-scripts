# -*- coding: UTF-8 -*-
import os
import pyperclip
import time
offset = 5
path = "C:/Users/n/Desktop/prot/"
log = "C:/Users/n/Desktop/prot_log/House.log"
with open(log, 'a+', encoding='utf-8') as l:
    l.write(f"offset:{0-offset}\n\n")
List = os.listdir(path)
list_with_t = []
for fpath in List:
    os.chdir(path)
    ctime = time.mktime(time.localtime(os.stat(fpath).st_ctime))
    list_with_t.append([fpath, ctime])
list_sorted = sorted(list_with_t, key=(lambda x: x[1]))
for td in list_sorted:
    fullname = os.path.split(td[0])[1]
    (name, ext) = os.path.splitext(fullname)
    newname = ""
    for ch in name:
        if ch == " ":
            newname += ch
            continue
        else:
            ch = chr(ord(ch) - offset)
            newname += ch
    print(name)
    print(newname + "\n")
    pyperclip.copy(newname)
    with open(log, 'a+', encoding='utf-8') as l:
        l.write(name + "\n")
        l.write(newname + "\n\n")
