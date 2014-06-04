import CalcFunctions
import decimal

signs = ['+','-','*','/']
runAgain = True

while runAgain == True:
    userInput = decimal.Decimal(raw_input("Enter number:"))
    signsInput = raw_input("Choose your operation (+, -, *, /)")
    if signsInput == signs[0]:
      while True:
        addInput = decimal.Decimal(raw_input("Enter number:"))
        break
      print CalcFunctions.add(userInput, addInput)
      runAgain()
    elif signsInput == signs[1]:
      while True:
        subtractInput = decimal.Decimal(raw_input("Enter number:"))
        break
      print CalcFunctions.subtract(userInput, subtractInput)
      runAgain()
    elif signsInput == signs[2]:
      while True:
        multiplyInput = decimal.Decimal(raw_input("Enter number:"))
        break
      print CalcFunctions.multiply(userInput, multiplyInput)
      runAgain()
    elif signsInput == signs[3]:
      while True:
        divideInput = decimal.Decimal(raw_input("Enter number:"))
        break
      print CalcFunctions.divide(userInput, divideInput)
      runAgain()
    else:
      print ("Invalid input. Try again:")
