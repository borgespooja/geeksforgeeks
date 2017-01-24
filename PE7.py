import time
start_time = time.time()
lim = 460300
b = {u:0 for u in range(0,(lim>>1)+100)}
p = [0] * 50050

def precompute():
    for i in range(3,9258,2):
        if not b[(i-3)>>1]:
            for j in range(i*i,lim,i):
                if j & 1:
                    b[(j-3) >> 1] = 1
    p[0] = 2
    cnt = 1
    i = 0
    while 2*i < lim:
        if not b[i]:
            p[cnt] = (2*i)+3
            cnt += 1
        i += 1
        
def main():
    precompute()
    #for _ in range(int(raw_input())):
		#n = int(raw_input().strip())
		#print p[n-1]
    print p[10001]
main()        
print("--- %s seconds ---" % (time.time() - start_time))