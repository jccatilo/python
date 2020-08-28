import os

def funca():
    name = input("enter name: ")
    age= input ("enter age: ")

    return name, age

def funcb(pangalan, edad): 
    print("your name is ")
    print(pangalan)
    print("with age of ")
    print(edad)

def main():
    name, age = funca()
    funcb(name, age)

main()
