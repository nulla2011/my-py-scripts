# -*- coding: UTF-8 -*-
import re
import os
import sys

unknownBlock1 = b'\x00\x00\x05\x91\x00\x00\x10\x0C\x00\x00\x00\x00'  #0x91 or 0x93 ?
unknownBlock2 = bytes.fromhex(
    "000000003F80000000000001000000003F80000000000002000000003F8000000000000B0000000100000000000000000000000000000000"
)


def convertFxp(path):
    newFxpContent = b""
    fName = os.path.split(f)[1]
    with open(path, 'rb') as fr:
        fxpContent = fr.read()
        pattern = re.compile(br'HaSm(.|\n)*?(\\[\w ]*\\[\w ]*\.aif)')
        pos = 0
        count = 0
        while 1:
            m = pattern.search(fxpContent[pos:])
            if m is None:
                newFxpContent += insertUnknownBlock2(fxpContent[pos:],
                                                     b'Harp')
                break
            fNameWithParentDir = m.group(2).replace(b"\\", b"\\\\")
            repl = b'HaSm' + unknownBlock1 + bytes(
                (doubleBackslash(installPath + r"\Processed Studio Kits")),
                'utf-8') + fNameWithParentDir
            block = re.sub(pattern,
                           repl,
                           fxpContent[pos:pos + m.end()],
                           count=1)
            if count > 0:
                if "Reso" in fName:
                    block = insertUnknownBlock2(block, b'HaSm')
                else:
                    block = insertUnknownBlock2(block, b'HaPa')
            newFxpContent += block
            pos += m.end()
            count += 1
    with open(fName, 'wb') as fw:
        fw.write(newFxpContent)
        print("success!")


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
    installPath = input(
        "Input your LM-4 MarkII install path(ends with \"LM-4 MarkII\"):")
    if installPath.endswith("\\") or installPath.endswith("/"):
        installPath=installPath[:-1]
    try:
        fileList = os.listdir(installPath + "\\Processed Studio Kits\\")
    except FileNotFoundError:
        print("file not found")
        sys.exit(0)
    fxpList = []
    for f in fileList:
        if f.lower().endswith(".fxp"):
            fxpList.append(f)
    print(f"found {len(fxpList)} fxp files, processing...")
    for f in fxpList:
        print(f"converting {f} ...")
        convertFxp(installPath + "\\Processed Studio Kits\\" + f)
