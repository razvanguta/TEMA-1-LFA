f=open("automat.in","r")
w=f.readline()
tstr=int(f.readline())
strin=int(f.readline())
nrstrfin=int(f.readline())
sirstfin=f.readline()
stfin=[int(x) for x in sirstfin.split()]
nrtr=int(f.readline())
dir=[]*101
for x in range(101):
    dir.append([])
for i in range(nrtr):
    inp=f.readline()
    inp=inp.split()
    dir[int(inp[0])].append([int(inp[1]),inp[2]])
q=list()
q.append(strin)
ql=list()
ql.append(0)
start=0
last=len(q)
curent=0
possol=list()
nr=w.count("&")
tstr-=nr
w=w.replace("&","")
while(start!=last):
    x=q[start]
    litera=w[ql[start]]
    if litera=='\n':
        possol.append(x)
    for x in dir[x]:
        if x[1]==litera:
            q.append(x[0])
            ql.append(ql[start]+1)
            last+=1
    start+=1
ok=False
for x in possol:
    if ok==True:
        break
    for y in stfin:
        if x==y or tstr==0:
            ok=True
            print("Cuvant acceptat")
            break
if(ok==False):
    print("Cuvant neacceptat")
