# String and numeric values can operate together with * 

a,b = 2,3
Text = "Pk"
print(a*Text*b)

# Output   [  PkPkPkPkPkPk  ]


# String & String can operate with + 

a, b = "2" , 3
txt = "@"

print((a+txt)*b)    # output  [  2@2@2@  ]

#  Numeric values can operate with all arthemetic operators

a,b = 2,3
c = 4 
print(a+b*c)   # output   [  14  ]



#  Arthemtic expression with integer and float with result in float

a,b = 10, 5.0
c = a*b
print(type(c) , c)    # output  [  50.0  ]


#  Result of division operator with 2 integers will be float

a,b = 1,2
c = a/b
print(type(c) , c)


#  Integer division with float and int will give int displayed as float

a,b = 1.5,3
d = a//b            # Just like in Maths , floor gives the closes integer, which is lesser than or equal to the float value.
                    # Here 1.5//3 = 0.5, (// : "Integer division")  will update the output as floor value,
                    # but will give the result as float value only
e = a/b
print(type(d), d , "Integer division || ", type(e) , e , "Normal division" )

# Output : [  'float'> 0.0 Integer division ||  <class 'float'> 0.5 Normal division   ]


c = -12//5   # -2.4 ==> -3
d = 12//5    # 2.4  ==> 2
print(type(c), c ,"and",  d, "Integer division")




# Remainder is negative when denominator is negative

c = 5%2
print(c)

c= 5%(-2)
print(c)