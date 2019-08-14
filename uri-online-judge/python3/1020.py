#!/usr/bin/env python3
# https://www.urionlinejudge.com.br/judge/en/problems/view/1020


def decompose(total, value):
    decomposed = total // value
    return total - decomposed * value, decomposed


def main():
    DAYS = int(input())
    
    DAYS, YEARS = decompose(DAYS, 365)
    DAYS, MONTHS = decompose(DAYS, 30)

    print(YEARS, 'ano(s)')
    print(MONTHS, 'mes(es)')
    print(DAYS, 'dia(s)')


# Start the execution if it's the main script
if __name__ == "__main__":
    main()
