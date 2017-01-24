def str_rev(n):
    return int(str(n)[::-1])

def is_valid_day(x, k):
    return (abs(x - str_rev(x)) % k) is 0
    
def main():
    i, j, k = map(int, raw_input().split())
    return sum([1 for d in range(i, j+1) if is_valid_day(d, k)])
    
print main()
        