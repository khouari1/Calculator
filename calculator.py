import CalcFunctions

signs = ['+','-','*','/']
while True:
    userInput = raw_input("Enter a number:")
    try:
        myValue = int(userInput)
        break
    except ValueError:
        print ("Invaid input. Try again:")
signsInput = raw_input("Choose your operation (+, -, *, /)")
if signsInput == signs[0]:
  while True:
      addInput = raw_input("Enter a second number:")
      try:
          myValue2 = int(addInput)
          break
      except ValueError:
          print ("Invaid input. Try again:")
  print CalcFunctions.add(myValue, myValue2)
elif signsInput == signs[1]:
  while True:
      subtractInput = raw_input("Enter a second number:")
      try:
          myValue3 = int(subtractInput)
          break
      except ValueError:
          print ("Invaid input. Try again:")
  print CalcFunctions.subtract(myValue, myValue3)
elif signsInput == signs[2]:
  while True:
      multiplyInput = raw_input("Enter a second number:")
      try:
          myValue4 = int(multiplyInput)
          break
      except ValueError:
          print ("Invaid input. Try again:")
  print CalcFunctions.multiply(myValue, myValue4)
elif signsInput == signs[3]:
  while True:
      divideInput = raw_input("Enter a second number:")
      try:
          myValue5 = int(divideInput)
          break
      except ValueError:
          print ("Invaid input. Try again:")
  print CalcFunctions.divide(myValue, myValue5)
else:
  while signsInput not in signs:
      print ("Invalid input. Try again:")
      signsInput = raw_input()
