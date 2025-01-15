import re

class StringCalculator:
    """String calculator class"""

    def add(self, value: str)-> int:
        """
        calculate the integer value sum in string of comma seperated number
        value: input string
        return count of string
        """
        list_of_integers = [0]
        if value:
            if re.findall(r'[^0-9,]', value.replace("\\n", ",")): # check only contain integers with comma and \n seperated
               raise TypeError("Invalid input!, confirm input only contains integers that are comma or \\n seperated")
            else:
               value = value.replace('\\n', ',')
               list_of_integers = value.split(",")
        else:
            return -1
        return sum([int(number.strip()) for number in list_of_integers if number.isdigit()])


if __name__ == "__main__":
   input_string = input("Enter string with comma seperate for calculate:")
   ins_calculator = StringCalculator()
   result = ins_calculator.add(input_string)
   print("sum of integers: {}".format(result)) # sum of numbers , -1 if not exists any
