#!/usr/bin/env python3
# https://www.urionlinejudge.com.br/judge/en/problems/view/1018


def decompose(total, value):
    decomposed = total // value
    return total - decomposed * value, decomposed


def main():
    MONEY = int(input())
    
    print(MONEY)

    MONEY, NOTES_100 = decompose(MONEY, 100)
    MONEY, NOTES_050 = decompose(MONEY, 50)
    MONEY, NOTES_020 = decompose(MONEY, 20)
    MONEY, NOTES_010 = decompose(MONEY, 10)
    MONEY, NOTES_005 = decompose(MONEY, 5)
    MONEY, NOTES_002 = decompose(MONEY, 2)
    MONEY, NOTES_001 = decompose(MONEY, 1)

    print(NOTES_100, "nota(s) de R$ 100,00")
    print(NOTES_050, "nota(s) de R$ 50,00")
    print(NOTES_020, "nota(s) de R$ 20,00")
    print(NOTES_010, "nota(s) de R$ 10,00")
    print(NOTES_005, "nota(s) de R$ 5,00")
    print(NOTES_002, "nota(s) de R$ 2,00")
    print(NOTES_001, "nota(s) de R$ 1,00")
    

# Start the execution if it's the main script
if __name__ == "__main__":
    main()
