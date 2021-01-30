#先下载psutil 库
#pip install psutil
import psutil
import os,dataeime,time

def getMenCpu():
    data = psutil.virtual_memory()
    total = data.total
    free = data.available
    memory = "Memory usage:%d%"(int(rountd(data.percent)))+"%"+""
    cpu = "CPU:%0.2f"%psutil.cpu_percent(interval=1)+"%"
    return memory+cpu
def main():
    while True:
    info = getMenCpu()
    time.sleep(0.2)
    print(info+"\b"*(len(info)+1),

# if __name__=="__main__":

main()