#!/usr/bin/env python3
# https://www.urionlinejudge.com.br/judge/en/problems/view/1022


def mdc(v1, v2):
    
    for i in range(((v1 + v2 + abs(v1 - v2)) // 2) + 1, 1, -1):
        if (v1 % i) == 0 and (v2 % i) == 0:
            return i
    return 1


def main():
    N = int(input())

    for _ in range(N):
        EXPRESSION = input().split(' ')
        N1, D1, OP, N2, D2, = (
            int(EXPRESSION[0]),
            int(EXPRESSION[2]),
                EXPRESSION[3],
            int(EXPRESSION[4]),
            int(EXPRESSION[6])
        )

        if OP == '+':
            NR = int(N1) * int(D2) + int(N2) * int(D1)
            DR = int(D1) * int(D2)
        elif OP == '-':
            NR = int(N1) * int(D2) - int(N2) * int(D1)
            DR = int(D1) * int(D2)
        elif OP == '*':
            NR = int(N1) * int(N2)
            DR = int(D1) * int(D2)
        elif OP == '/':
            NR = int(N1) * int(D2)
            DR = int(D1) * int(N2)

        D = mdc(NR, DR)

        print(NR, '/', DR, ' = ',NR // D, '/',DR // D, sep='')


# Start the execution if it's the main script
if __name__ == "__main__":
    main()
