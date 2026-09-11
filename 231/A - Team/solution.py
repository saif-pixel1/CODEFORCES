import sys
 
input = sys.stdin.readline
 
def solve():
    count = 0 
    solver = list(map(int, input().split()))
    for i in range(len(solver)):
        if solver[i] == 1:
            count = count + 1 
        else:
            continue
    return 1 if count >=2 else 0
             
 
def main():
    # t = 1
    res =0 
    t = int(input())
    for _ in range(t):
        res = res + solve()
    print(res)
 
if __name__ == "__main__":
    main()