import sys
 
input = sys.stdin.readline
 
def solve():
    t = int(input())
    x = 0
    for _ in range(t):
        s = str(input())
        if "++" in s:
            x += 1
        else:
            x -= 1
    print(x)
 
def main():
    solve()
 
if __name__ == "__main__":
    main()