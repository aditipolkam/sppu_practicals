def calculate_time(atime,btime,ctime,ttime,wtime):
    #ctime.append(btime[0])
    etime = 0
    for i in range(0,len(atime)):
        if atime[i]<=etime:
            c = etime + btime[i]
            etime=c
        else:
            etime=atime[i]
            c=etime + btime[i]
            etime=c
        ctime.append(c)
        ttime.append(ctime[i]-atime[i])
        wtime.append(ttime[i]-btime[i])
        print(etime)
    print(ctime)
    print(ttime)
    print(wtime)

def avg_time(atime,ttime,wtime):
    st = 0
    sw = 0
    p = len(atime)
    for i in range(0,p):
        st+=ttime[i]
        sw+=wtime[i]
    print("Avg tat:",st/p)
    print("Avg wait time:",sw/p)
        
atime = []
btime = []
ctime = []
ttime = []
wtime = []

num = int(input("No of process?"))
for i in range(num):
    atime.append(int(input("Arrival time of p")))
    btime.append(int(input("Burst time of p")))
calculate_time(atime,btime,ctime,ttime,wtime)
avg_time(atime,ttime,wtime)