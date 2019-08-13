#!/bin/python3
# https://www.urionlinejudge.com.br/judge/en/problems/view/1006


def main():
    A, B, C = float(input()), float(input()), float(input())

    wA = 2.0
    wB = 3.0
    wC = 5.0

    MEDIA = ((A * wA) + (B * wB) + (C * wC)) / (wA + wB + wC)

    print("MEDIA =", format(MEDIA, '.1f'))


# Start the execution if it's the main script
if __name__ == "__main__":
    main()
