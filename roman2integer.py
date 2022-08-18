# Contains method to convert a properly formatted roman numeral number
# into an integer

class Solution:
    def romanToInt(self, s: str) -> int:
        self.s = list(s)

        hashtable = {"I":1,
                     "V":5,
                     "X":10,
                     "L":50,
                     "C":100,
                     "D":500,
                     "M":1000}
        ### need to use a sliding window algorithm
        convertedValues = [hashtable.get(i) for i in self.s]
        print(convertedValues)

        if convertedValues[-1] > convertedValues[-2]:
            highestVal = convertedValues[-1]
            convertedValues.remove(highestVal)
            return highestVal - sum(convertedValues)
        else:
            return sum(convertedValues)

x = Solution().romanToInt("MDCCCLXXXXVIIII")
print(x)