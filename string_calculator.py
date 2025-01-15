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
           list_of_integers = value.split(",")
        else:
            return -1
        return sum([int(number) for number in list_of_integers])


if __name__ == "__main__":
   input_string = input("Enter string with comma seperate for calculate:")
   ins_calculator = StringCalculator()
   result = ins_calculator.add(input_string)
   print("sum of integers: {}".format(result)) # sum of numbers , -1 if not exists any
