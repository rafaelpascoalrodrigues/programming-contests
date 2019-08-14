#!/usr/bin/env python3
# https://www.urionlinejudge.com.br/judge/en/problems/view/1018


def decompose(total, value, rate = 1):
    decomposed = int(total * rate // value)
    return (total * rate - decomposed * value) / rate, decomposed


def main():
    MONEY = float(input())
    
    MONEY, NOTES_100 = decompose(MONEY, 100)
    MONEY, NOTES_050 = decompose(MONEY, 50)
    MONEY, NOTES_020 = decompose(MONEY, 20)
    MONEY, NOTES_010 = decompose(MONEY, 10)
    MONEY, NOTES_005 = decompose(MONEY, 5)
    MONEY, NOTES_002 = decompose(MONEY, 2)

    MONEY, COINS_100 = decompose(MONEY, 100, 100)
    MONEY, COINS_050 = decompose(MONEY, 50, 100)
    MONEY, COINS_025 = decompose(MONEY, 25, 100)
    MONEY, COINS_010 = decompose(MONEY, 10, 100)
    MONEY, COINS_005 = decompose(MONEY, 5, 100)
    MONEY, COINS_001 = decompose(MONEY, 1, 100)


    print("NOTAS:")
    print(NOTES_100, "nota(s) de R$ 100.00")
    print(NOTES_050, "nota(s) de R$ 50.00")
    print(NOTES_020, "nota(s) de R$ 20.00")
    print(NOTES_010, "nota(s) de R$ 10.00")
    print(NOTES_005, "nota(s) de R$ 5.00")
    print(NOTES_002, "nota(s) de R$ 2.00")

    print("MOEDAS:")
    print(COINS_100, "moeda(s) de R$ 1.00")
    print(COINS_050, "moeda(s) de R$ 0.50")
    print(COINS_025, "moeda(s) de R$ 0.25")
    print(COINS_010, "moeda(s) de R$ 0.10")
    print(COINS_005, "moeda(s) de R$ 0.05")
    print(COINS_001, "moeda(s) de R$ 0.01")


# Start the execution if it's the main script
if __name__ == "__main__":
    main()
