import sys
 
input = sys.stdin.readline
 
def main():
    # t = 1
    t = int(input())
    for _ in range(t):
        n = int(input())
        if (n-1)%3==0 or (n+1)%3==0:
            print("First")
        else:
            print("Second")
            
if __name__ == "__main__":
    main()