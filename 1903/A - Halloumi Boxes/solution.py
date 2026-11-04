import sys
 
input = sys.stdin.readline
 
def solve():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    if k>=2:
        return "YES"
    else:
        if l==sorted(l):
            return "YES"
        return"NO"
 
 
def main():
    # t = 1
    t = int(input())
    for _ in range(t):
        print(solve())
 
if __name__ == "__main__":
    main()