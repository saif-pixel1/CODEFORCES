import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
 
    for _ in range(t):
        n = int(input())
        s = input().strip()
 
        dots = s.count('.')
 
        if '...' in s:
            print(2)
        else:
            print(dots)
 
if __name__ == "__main__":
    main()