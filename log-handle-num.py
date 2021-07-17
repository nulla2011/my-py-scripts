# -*- coding: UTF-8 -*-
import psutil
import csv
import time

processNames = ["SwUSB.exe", "runSW.exe", "System", "explorer.exe"]
interval = 10


def getPid(name):
    pids = psutil.process_iter()
    for pid in pids:
        if pid.name() == name:
            print(f"{name} 's pid is: {pid.pid}")
            return pid.pid
    print("can't find process")
    return -1


def getHandleNum(id):
    try:
        num = psutil.Process(id).num_handles()
    except Exception:
        num = 0
    return num


if __name__ == "__main__":
    pids = []
    for process in processNames:
        pids.append(getPid(process))
    while 1:
        with open("handle-num-log.csv", 'a', newline='') as csvf:
            lineWriter = csv.writer(csvf, lineterminator='\r\n')
            lTime = time.localtime()
            strTime = time.strftime("%Y-%m-%d %H:%M:%S", lTime)
            line = [strTime]
            for pid in pids:
                handleNum = 0 if pid == -1 else getHandleNum(pid)
                line.append(handleNum)
            lineWriter.writerow(line)
            print(strTime)
            for i in range(len(line) - 1):
                print(f"{processNames[i]}: {line[i+1]}")
        time.sleep(60 * interval)
