#!/bin/python3
# https://www.urionlinejudge.com.br/judge/en/problems/view/1002


def main():
    R = float(input())

    pi = 3.14159
    A = pi * R ** 2

    print("A=", format(A, '.4f'), sep = '')


# Start the execution if it's the main script
if __name__ == "__main__":
    main()
