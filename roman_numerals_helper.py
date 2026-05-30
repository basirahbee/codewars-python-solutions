class RomanNumerals:

    @staticmethod
    def to_roman(num):
        roman_table = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I") ]

        result = ""

        for value, symbol in roman_table:
            while num >= value:
                result += symbol
                num -= value

        return result

    @staticmethod
    def from_roman(roman_string):
        values = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1 }

        total = 0
        i = 0

        while i < len(roman_string):
            current = values[roman_string[i]]

            if i + 1 < len(roman_string):
                next_value = values[roman_string[i + 1]]

                if current < next_value:
                    total += next_value - current
                    i += 2
                    continue

            total += current
            i += 1

        return total
