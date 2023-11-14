class IntegerToRoman:
    def __init__(self):
        self.numeral_map = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

    def int_to_roman(self, num):
        if not (0 < num < 4000):
            raise ValueError("Input must be between 1 and 3999")

        result = ''
        for value, symbol in sorted(self.numeral_map.items(), reverse=True):
            while num >= value:
                result += symbol
                num -= value

        return result

converter = IntegerToRoman()
number = 3549
roman_numeral = converter.int_to_roman(number)
print(f"The Roman numeral representation of {number} is: {roman_numeral}")
