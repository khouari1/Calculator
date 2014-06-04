import decimal

def add(x, n):
  total = 0
  total = x + n
  return total
def subtract(x, n):
  total = 0
  total = x - n
  return total
def multiply(x, n):
  total = 0
  total = x * n
  return total
def divide(x, n):
  total = 0
  total = x / n
  return total
def runAgain():
  runAgain = raw_input("Run again?")
  if runAgain == ("yes"):
    runAgain = True
  else:
    runAgain = False
