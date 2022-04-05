#---------------------------------Comments------------------------------------
#Print Hello World
print("Hello, World!")

print("Hello, World!") #This is a comment

#print("Hello, World!")
print("Cheers, Mate!")


"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")


#---------------------------------Functions------------------------------------
#Example One:
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Casting:
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


#---------------------------------Functions------------------------------------
#Example One:
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")

#Example Two: Arbitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")



#---------------------------------Sushi Bot------------------------------------

