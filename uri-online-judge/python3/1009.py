#!/bin/python3
# https://www.urionlinejudge.com.br/judge/en/problems/view/1009


def main():
    _, SALARY, SALES = input(), float(input()), float(input())

    TOTAL = SALARY + (SALES * 0.15)

    print("TOTAL = R$", format(TOTAL, '.2f'))


# Start the execution if it's the main script
if __name__ == "__main__":
    main()
