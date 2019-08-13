#!/usr/bin/env python3
# https://www.urionlinejudge.com.br/judge/en/problems/view/1015


def main():
    X1, Y1 = map(float, input().split(' '))
    X2, Y2 = map(float, input().split(' '))

    DISTANCE = ((X2 - X1) ** 2 + (Y2 - Y1) ** 2) ** (1 / 2)

    print(format(DISTANCE, '.4f'))


# Start the execution if it's the main script
if __name__ == "__main__":
    main()
