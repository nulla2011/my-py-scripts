import re
#installPath=input("Input your LM-4 MarkII install path:")
blank=b'\x00\x00\x05\x91\x00\x00\x10\x0C\x00\x00\x00\x00'
installPath="E:\\\\Steinberg\\\\Vstplugins\\\\LM-4 MarkII"
def convertFxp(path):
    fxpContent=b""
    newFxpContent=b""
    with open(path,'rb') as fr:
        fxpContent=fr.read()
        pattern=re.compile(br'HaSm(.|\n)*?\\([\w ]*\\[\w ]*\.aif)')
        pos=0
        while 1:
            m=pattern.search(fxpContent[pos:])
            if m is None:
                newFxpContent+=fxpContent[pos:]
                break
            fileName=m.group(2).replace(b"\\",b"\\\\")
            repl=b'HaSm'+blank+bytes((installPath+"\\\\Processed Studio Kits\\\\"),'utf-8')+fileName
            newFxpContent+=re.sub(pattern,repl,fxpContent[pos:pos+m.end()],count=1)
            pos+=m.end()
    with open("t.fxp",'wb') as fw:
        fw.write(newFxpContent)
if __name__=="__main__":
    convertFxp("C:/Users/n/Desktop/01 Gator Kit.fxp")
    