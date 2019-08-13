#!/usr/bin/env python3
# https://www.urionlinejudge.com.br/judge/en/problems/view/1011


def main():
    R = float(input())

    pi = 3.14159
    V = 4/3 * pi * R ** 3

    print("VOLUME =", format(V, '.3f'))


# Start the execution if it's the main script
if __name__ == "__main__":
    main()
