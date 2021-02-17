import re

unknownBlock1 = b'\x00\x00\x05\x91\x00\x00\x10\x0C\x00\x00\x00\x00'  #0x91 or 0x93 ?
unknownBlock2 = bytes.fromhex(
    "000000003F80000000000001000000003F80000000000002000000003F8000000000000B0000000100000000000000000000000000000000"
)
installPath = "E:\\\\Steinberg\\\\Vstplugins\\\\LM-4 MarkII"


def convertFxp(path):
    fxpContent = b""
    newFxpContent = b""
    with open(path, 'rb') as fr:
        fxpContent = fr.read()
        pattern = re.compile(br'HaSm(.|\n)*?(\\[\w ]*\\[\w ]*\.aif)')
        pos = 0
        count = 0
        while 1:
            m = pattern.search(fxpContent[pos:])
            if m is None:
                newFxpContent += insertUnknownBlock2(fxpContent[pos:],
                                                     br'Harp')
                break
            fileName = m.group(2).replace(b"\\", b"\\\\")
            repl = b'HaSm' + unknownBlock1 + bytes(
                (installPath + doubleBackslash("\\Processed Studio Kits")),
                'utf-8') + fileName
            block = re.sub(pattern,
                           repl,
                           fxpContent[pos:pos + m.end()],
                           count=1)
            if count > 0:
                block = insertUnknownBlock2(block, br'HaPa')
            newFxpContent += block
            pos += m.end()
            count += 1
    with open("t.fxp", 'wb') as fw:
        fw.write(newFxpContent)


def insertUnknownBlock2(bytes, reg):
    pattern = re.compile(reg)
    m = pattern.search(bytes)
    if m is None:
        print("can't find insert position")
        return bytes
    else:
        return (bytes[:m.start()] + unknownBlock2 + bytes[m.start():])


def doubleBackslash(str):
    str = str.replace("\\", "\\\\")
    str = str.replace("/", "\\\\")
    return str


if __name__ == "__main__":
    #installPath=input("Input your LM-4 MarkII install path:")
    convertFxp("C:/Users/n/Desktop/01 Gator Kit.fxp")
