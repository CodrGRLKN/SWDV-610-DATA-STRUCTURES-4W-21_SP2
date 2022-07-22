def minDigit(number):
        if len(number) == 0:
                return None
        if len(number) == 1:
                return number[0]
        return min(number[0], minDigit(number[1:]))

def maxDigit(number):
        if len(number) == 0:
                return None
        if len(number) == 1:
                return number[0]
        return max(number[0], maxDigit(number[1:]))


print(minDigit([1, 3, 5, 7, 9, 11]))
print(maxDigit([2, 4, 6, 8, 10, 12]))



