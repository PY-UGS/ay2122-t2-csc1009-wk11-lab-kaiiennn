class Calculator:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def adder(self):
        result = self.input1 + self.input2
        return result

    def subtractor(self):
        result = self.input1 - self.input2
        return result

    def multiplier(self):
        result = self.input1 * self.input2
        return result

    def divider(self):
        result = self.input1 / self.input2
        return result

    def clear(self):
        self.input1 = 0 #Both input values cleared to zero
        self.input2 = 0

input1 = int(input("Please enter the first number: "))
input2 = int(input("Please enter the second number: "))
calc = Calculator(input1, input2)

add_result = calc.adder()
print("The result of adding " + str(calc.input1) + " and " + str(calc.input2) + " is " + str(add_result))
subtract_result = calc.subtractor()
print("The result of subtracting " + str(calc.input2) + " from " + str(calc.input1) + " is " + str(subtract_result))
multiply_result = calc.multiplier()
print("The result of multiplying " + str(calc.input1) + " and " + str(calc.input2) + " is " + str(multiply_result))
divide_result = calc.divider()
print("The result of dividing " + str(calc.input1) + " and " + str(calc.input2) + " is " + str(divide_result))
clear_result = calc.clear()
print("Input 1's value after clear() is " + str(calc.input1))
print("Input 2's value after clear() is " + str(calc.input2))

