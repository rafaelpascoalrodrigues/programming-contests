#!/usr/bin/env python3
# https://www.urionlinejudge.com.br/judge/en/problems/view/1019


def decompose(total, value):
    decomposed = total // value
    return total - decomposed * value, decomposed


def main():
    SECONDS = int(input())
    
    SECONDS, HOURS = decompose(SECONDS, 60 * 60)
    SECONDS, MINUTES = decompose(SECONDS, 60)

    print(HOURS, ':', MINUTES, ':', SECONDS, sep = '')


# Start the execution if it's the main script
if __name__ == "__main__":
    main()
