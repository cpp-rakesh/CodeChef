'''
  Problem : Two vs Ten
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 27/01/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        if n % 10 == 0:
            print(0)
        elif n % 10 == 5:
            print(1)
        else:
            print(-1)

if __name__ == '__main__':
    solve()
