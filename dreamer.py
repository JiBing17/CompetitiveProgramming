# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes
# Kattis Week-2

import sys


def main():
    n = int(sys.stdin.readline().strip())

    for i in range(n):
        temp = sys.stdin.readline().strip().split()
        print(temp[0])
    return
main()