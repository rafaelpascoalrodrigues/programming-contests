#!/usr/bin/env python3
# https://www.urionlinejudge.com.br/judge/en/problems/view/1016


def main():
    DISTANCE = int(input())
    
    TIME = int((DISTANCE / 30) * 60)

    print(TIME, "minutos")


# Start the execution if it's the main script
if __name__ == "__main__":
    main()
