#!/usr/bin/env python3
# https://www.urionlinejudge.com.br/judge/en/problems/view/1010


def maior_a_b(a, b):
    return (a + b + abs(a - b)) // 2


def main():
#   NUMBER, HOURS, PER_HOUR = int(input()), int(input()), float(input())
    A, B, C = map(int, input().split(' '))

    MAIOR = maior_a_b(maior_a_b(A, B), C)

    print(MAIOR, "eh o maior")


# Start the execution if it's the main script
if __name__ == "__main__":
    main()
