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
print(c)  