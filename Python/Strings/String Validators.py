#!/bin/python3
# Easy
# https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':

    def showAllAttrs(strr):
        hasAlpha = False
        hasLower=False
        hasUpper=False
        hasAlphaNum=False
        hasDigit=False
        for i in strr:
            if ( not hasAlphaNum ) and i.isalnum():
                hasAlphaNum = True
            if ( not hasAlpha ) and i.isalpha():
                hasAlpha = True
            if ( not hasDigit ) and i.isdigit():
                hasDigit = True
            if ( not hasLower ) and i.islower():
                hasLower = True
            if ( not hasUpper ) and i.isupper():
                hasUpper = True
            if hasAlphaNum and hasAlpha and hasDigit and hasLower and hasUpper:
                break
        print(hasAlphaNum)
        print(hasAlpha)
        print(hasDigit)
        print(hasLower)
        print(hasUpper)




    x = input()
    showAllAttrs(x)

