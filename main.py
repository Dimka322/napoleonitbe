RomanDigits = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


class Solution:
    def romanToInt(self, s: str) -> int:
        romanDigitsList = list(s)
        sum = 0
        isBad = None  # случай, когда встречаться будут IV и т.д.
        for i in range(len(romanDigitsList) - 1):
            CurrentDigit = RomanDigits[romanDigitsList[i]]
            NextDigit = RomanDigits[romanDigitsList[i + 1]]

            if CurrentDigit >= NextDigit and isBad is None:
                sum += CurrentDigit
            elif CurrentDigit < NextDigit and isBad is None:
                isBad = CurrentDigit
            else:
                sum += CurrentDigit - isBad
                isBad = None
        if isBad is None:
            sum += RomanDigits[romanDigitsList[-1]]
        else:
            sum += RomanDigits[romanDigitsList[-1]] - isBad
        return sum


a = Solution()

print(a.romanToInt('ID'))
