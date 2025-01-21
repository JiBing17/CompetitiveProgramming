import sys


def main():
    n = int(sys.stdin.readline().strip())

    for i in range(n):
        temp = sys.stdin.readline().strip().split()
        print(temp[0])
    return
main()