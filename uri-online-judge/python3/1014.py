#!/usr/bin/env python3
# https://www.urionlinejudge.com.br/judge/en/problems/view/1014


def main():
    X = int(input())
    Y = float(input())

    CONSUMPTION = X / Y

    print(format(CONSUMPTION, '.3f'), "km/l")


# Start the execution if it's the main script
if __name__ == "__main__":
    main()
