def
print("Welcome to computer language for us humans! I will convert a binary number into a form you humans use.")
binary = str(input("What is your byte? "))
#Welcomes users...

if binary[0] == "1":
    um = 2**7
else:
    um = 0

if binary[1] == "1":
    dois = 2**6
else:
    dois = 0

if binary[2] == "1":
    tres = 2**5
else:
    tres = 0

if binary[3] == "1":
    quatro = 2**4
else:
    quatro = 0

if binary[4] == "1":
    cinco = 2**3
else:
    cinco = 0

if binary[5] == "1":
    seis = 2**2
else:
    seis = 0

if binary[6] == "1":
    sete = 2**1
else:
    sete = 0

if binary[7] == "1":
    oito = 2**0
else:
    oito = 0

final_answer = um + dois + tres + quatro + cinco + seis + sete + oito
#Just so you/I know (AKA FY/MI), I'm using Portuguese numbers instead of English so I can differentate the variables from this conversion to the other numbers to binary one

print(final_answer)
    



                    
                    
