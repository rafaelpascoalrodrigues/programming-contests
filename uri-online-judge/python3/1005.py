#!/bin/python3
# https://www.urionlinejudge.com.br/judge/en/problems/view/1005


def main():
    A, B = float(input()), float(input())

    wA = 3.5
    wB = 7.5

    MEDIA = ((A * wA) + (B * wB)) / (wA + wB)

    print("MEDIA =", format(MEDIA, '.5f'))


# Start the execution if it's the main script
if __name__ == "__main__":
    main()
