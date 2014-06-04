import decimal

run_list = ["yes", "y", "agree"]

#def verify(x):
#  while True:
#    try:
#      decimal.Decimal(x)
#      break
#    except decimal.InvalidOperation:
#      print ("Invalid input.")
def add(x, n):
  total = 0
  x = decimal.Decimal(x)
  n = decimal.Decimal(n)
  total = x + n
  return total
def subtract(x, n):
  total = 0
  x = decimal.Decimal(x)
  n = decimal.Decimal(n)
  total = x - n
  return total
def multiply(x, n):
  total = 0
  x = decimal.Decimal(x)
  n = decimal.Decimal(n)
  total = x * n
  return total
def divide(x, n):
  total = 0
  x = decimal.Decimal(x)
  n = decimal.Decimal(n)
  total = x / n
  return total
#def runAgain():
#  runAgain = raw_input("Run again?").lower()
#  if runAgain not in run_list:
#    start = False
