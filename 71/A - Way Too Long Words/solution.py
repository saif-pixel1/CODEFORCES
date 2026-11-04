import sys
 
input = sys.stdin.readline
 
def solve():
    # localization
    s =str(input()).strip()
    if len(s) <= 10:
        print(s)
        return
    temp = len(s)-2
    print(s[0] + str(temp) + s[-1])
 
def main():
    # t = 1
    t = int(input())
    for _ in range(t):
        solve()
 
if __name__ == "__main__":
    main()
 