import sys
input = sys.stdin.readline
def solve(d, st, final):
    diff = 0 ; l = 0 ; r = l + 1 ; min = 0
    min = (final - st[-1])*2
    if st[l]-0 > min:
        min = st[l] - 0
 
    while r <= len(st)-1:
 
        diff = st[r] - st[l]
        if diff > min:
            min = diff
            r += 1
            l += 1
        else:
            l += 1
            r += 1
    return min
 
def main():
    # t = 1
    t = int(input())
    for _ in range(t):
        d,final = map(int,input().split(" "))
        st = list(map(int,input().split(" ")))
        print(solve(d,st,final))
 
if __name__ == "__main__":
    main()
 