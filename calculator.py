import CalcFunctions
import decimal

signs = ['1','2','3','4']
run_list = ["yes", "y", "agree"]

while True:
  print ("Choose your operation:")
  print ("1: Addition")
  print ("2: Subtraction")
  print ("3: Multiplication")
  print ("4: Division")
  signsInput = raw_input()
  if signsInput == signs[0]:
    while True:
      addInput1 = raw_input("Enter first number:")
      try:
        decimal.Decimal(addInput1)
        break
      except decimal.InvalidOperation:
        print ("Invalid input.")
    while True:
      addInput2 = raw_input("Enter second number:")
      try:
        decimal.Decimal(addInput2)
        break
      except decimal.InvalidOperation:
        print ("Invalid input.")
    print CalcFunctions.add(addInput1, addInput2)
    break
  elif signsInput == signs[1]:
    while True:
      subtractInput1 = raw_input("Enter first number:")
      try:
        decimal.Decimal(subtractInput1)
        break
      except decimal.InvalidOperation:
        print ("Invalid input.")
    while True:
      subtractInput2 = raw_input("Enter second number:")
      try:
        decimal.Decimal(subtractInput2)
        break
      except decimal.InvalidOperation:
        print ("Invalid input.")
    print CalcFunctions.subtract(subtractInput1, subtractInput2)
    break
  elif signsInput == signs[2]:
    while True:
      multiplyInput1 = raw_input("Enter first number:")
      try:
        decimal.Decimal(multiplyInput1)
        break
      except decimal.InvalidOperation:
        print ("Invalid input.")
    while True:
      multiplyInput2 = raw_input("Enter second number:")
      try:
        decimal.Decimal(multiplyInput2)
        break
      except decimal.InvalidOperation:
        print ("Invalid input.")
    print CalcFunctions.multiply(multiplyInput1, multiplyInput2)
    break
  elif signsInput == signs[3]:
    while True:
      divideInput1 = raw_input("Enter first number:")
      try:
        decimal.Decimal(divideInput1)
        break
      except decimal.InvalidOperation:
        print ("Invalid input.")
    while True:
      divideInput2 = raw_input("Enter second number:")
      try:
        decimal.Decimal(divideInput2)
        break
      except decimal.InvalidOperation:
        print ("Invalid input.")
    print CalcFunctions.divide(divideInput1, divideInput2)
    break
  else:
    print ("Invalid input. Try again:")
