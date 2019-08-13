#!/bin/python3
# https://www.urionlinejudge.com.br/judge/en/problems/view/1008


def main():
    NUMBER, HOURS, PER_HOUR = int(input()), int(input()), float(input())

    SALARY = HOURS * PER_HOUR

    print("NUMBER =", NUMBER)
    print("SALARY = U$", format(SALARY, '.2f'))


# Start the execution if it's the main script
if __name__ == "__main__":
    main()
