import Operations
mistakes=1
print()
print("Jet the text calculator")
print("By __UniqueD__")
print()
print("Press Ctrl + C to exit the program")
print()
while True:
  try:
    mistakes=mistakes+1
    if mistakes>10:
     print()
     print("You just entered a wrong value", mistakes, "times")
     print()
    num1=(float(input("First number: ")))
    print()
    num2=(float(input("Second number: ")))
    break
  except ValueError:
     print()
     print("That's not a number")
     print()
  except KeyboardInterrupt:
     print()
     print()
     print("You killed the program :(")
     exit()
try:
  print()
  print("Enter the number of the operation you need")
  print("---(1) Addition, (2) Multiplication, (3) Substraction or (4) Division----")
  print()
  operation=input()
  print()
  if operation=="Addition" or operation=="2":
      print("The answer is: ", Operations.Addition(num1,num2))
  elif operation=="Substraction" or operation=="3":
      print("The answer is: ", Operations.Substraction(num1,num2))
  elif operation=="Multiplication" or operation=="1":
      print("The answer is: ", Operations.Multiplication(num1,num2))
  elif operation=="Division" or operation=="4":
    try:
      print("The answer is: ", Operations.Division(num1,num2))
    except ZeroDivisionError:
      print("You can't divide by zero")
  else:
    print("Wrong operation")
except KeyboardInterrupt:
         print()
         print("You killed the program :(")
print()
print("Program ended")
