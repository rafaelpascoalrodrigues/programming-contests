#!/usr/bin/env python3
# https://www.urionlinejudge.com.br/judge/en/problems/view/1024


def main():
    N = int(input())

    for _ in range(N):
        PLAINTEXT = [ char for char in input() ]
        
        CYPHERTEXT = PLAINTEXT[::-1]

        for i in range(len(CYPHERTEXT)): 
            ascii = ord(CYPHERTEXT[i])
            if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
                CYPHERTEXT[i] = chr(ascii + 3)
        
        for i in range(len(CYPHERTEXT) // 2, len(CYPHERTEXT)):
            ascii = ord(CYPHERTEXT[i])
            CYPHERTEXT[i] = chr(ascii - 1)
        
        print(''.join(CYPHERTEXT))


# Start the execution if it's the main script
if __name__ == "__main__":
    main()
