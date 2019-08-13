#!/usr/bin/env python3
# https://www.urionlinejudge.com.br/judge/en/problems/view/1017


def main():
    TIME = int(input())
    SPEED = int(input())
    
    SPENT = SPEED * TIME / 12.0

    print(format(SPENT, '.3f'))
    

# Start the execution if it's the main script
if __name__ == "__main__":
    main()
