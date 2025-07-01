#!/usr/bin/python
#Purpose : Python is a dynamic typed language

#      #   1.static-Typed Languages
#         -first declare the variable, & then use them
#         - int a, float b #Declaration
#         -a = 10         #Initialization

#         2. Dynamic typed languages
#         - create when you need. No declaration needed
#             num1 =123
#         - line or block based execution

#     python code -> python byte code -> pythonInterpreter -> C compiler -> machine
# so, python is slower compared to python based languages


num1 = 100
type(num1)
print(type(num1))

print(num1)
print("num1")

print("num1 =", num1)
print("num1=", num1, "type=", type(num1)) #int

#works in both static and dynamic typing
num1 = 300                    
print("num1=", num1, "type=", type(num1))

#python is a dynamic typed language
num1 = 300.0                       #float
print("num1=", num1, "type=", type(num1))

num1 = 300.                       #float
print("num1=", num1, "type=", type(num1))

num1 = 300,                       #Tuple
print("num1=", num1, "type=", type(num1))

num1 = "300"                       #String
print("num1=", num1, "type=", type(num1))

num1 = "True"
print("num1=", num1, "type=", type(num1))

num1 = True
print("num1=", num1, "type=", type(num1))

num1 = None
print("num1=", num1, "type=", type(num1)) #none

num1 = "None"
print("num1=", num1, "type=", type(num1))