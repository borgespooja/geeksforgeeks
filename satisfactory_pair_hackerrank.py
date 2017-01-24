def main():
    n = int(raw_input())
    lst_pair = []
	a_lim = (n/2) if (n&1) else (n/2)+1 
    for a in range(1,a_lim):
        for b in range(2,n):
            for x in range(1,n-1):
                y = (n - (a*x))/b
                if (a<b) and ((a*x)+(b*y) is n) and (y>0) and ((a,b) not in lst_pair):
                    lst_pair.append((a,b))
                    
    print len(lst_pair)
main()    
                