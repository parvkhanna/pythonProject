# Arithmetic operators are used with numeric values to perform common mathematical operations:
""" 
  Operator	  Name	                  Example
     
     +	      Addition	              x + y	
     -	      Subtraction	          x - y	
     *	      Multiplication	      x * y	
     /	      Division	              x / y	
     %	      Modulus	              x % y	
     **	      Exponentiation	      x ** y	
     //	      Floor division	      x // y
"""



'''
3) Multiplication
'''
# String and numeric values can operate together with * 

a,b = 2,3
Text = "Pk"
print(a*Text*b , "( n * String : Prints the string n times)")

# Output   [  PkPkPkPkPkPk  ]


# String & String can operate with + {[Addition]}

name = "Parv"
lastName = "Khanna"
print (name+lastName , "(String + String = CombinedString)")

a, b = "2" , 3
txt = "@"

print((a+txt)*b, "((String+String) will be printed n number of times")    # output  [  2@2@2@  ]



#  Numeric values can operate with all arthemetic operators

a,b = 2,3
c = 4 
print(a+b*c , "All operators for numeric value")   # output   [  14  ]



#  Arthemtic expression {["""Multiplication"""]}with integer and float with result in float

a,b = 10, 5.0
c = a*b
print(type(c) , c , "(int * float = float)")    # output  [  50.0  ]





'''
4) Division
'''
#  Result of {[division]} operator with 2 integers will be float

a,b = 4,2
c = a/b
print(type(c) , c , "(int / int = float)")



'''
5) Modulo/Modulus
'''
# Remainder is negative when denominator is negative

c = 5%2
print(c , "remainder is (+)ve when denominator is positive")  # Output : 1

c= 5%(-2)
print(c, 'remainder is (-)ve when denominator is negative')  # Output : -1

'''
6)  Exponentiation
'''




"""
7) Floor/Integer Division
"""

#  float//int will give integer value as float value

a,b = 1.5,3
d = a//b            # Output 0.0  with floor division '//'
""" Just like in Maths , floor gives the closest lower end value, i.e output is lesser than or equal to the float value.
    Here 1.5//3 = 0.5, (// : "floor division")  will update the output as floor value,
   but will give the result as float value only."""
                    
e = a/b  # Output 0.5 with normal division '/'
print(d , "floor division || ", type(e) , e , "Normal division" )
print("float//int = {Floor Integer} which is represented as float value")



# Foor division when numerator is negative

c = -12//5   # Result :-2.4 But Output: ==> -3
d = 12//5    # Result : 2.4 But Output: ==>  2
print( c , "(-2.4 is shown as -3 )",  d, "(2.4 is shown as 2)")




