conversion_type =  str(input("Welcome to converting human numbers to computer numbers! Will you be giving a number with the 'decimal system' or in 'binary'? "))
#Politeness is always key, so always welcome the guest

if conversion_type == "decimal system":
    num = int(input("Gimme a number between 0 and 255 to convert into a byte, please: "))
        
    h = num % 2
    #I called this "h" because it goes with the "eighth" variable (since h is the 8th letter of the alphabet
    eighth = num // 2
    #I called this "eighth" because it's going to be the eigth digit in the final byte

    g = eighth % 2
    #As you can see, the letter/digit pair pattern continues
    seventh = eighth // 2

    f = seventh % 2
    #The percent sign (%) is used to find ONLY the remainder of a division problem, that's the important part for knowing if it's a 0 or a 1
    sixth = seventh // 2
    #The double slash (//) is used to to find the next digit. It'll soon be used as the dividend to find the next digit.

    e = sixth % 2
    fifth = sixth // 2

    d = fifth % 2
    fourth = fifth // 2

    c = fourth % 2
    third = fourth // 2

    b = third % 2
    second = third // 2

    a = second % 2
    first = second // 2

    print (a, b, c, d, e, f, g, h)
    #The way to convert I learned has you solve it backwards, so you'll find the 8th digit first then work your way up to the 1st digit. With this return statement, I'm putting each digit (bit) together to form the byte.

        
elif conversion_type == "binary":
    binary = str(input("What does your byte look like? "))

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
        
    
    #This'll turn binary numbers as strings into an integer.  All the calculations n' stuff for the conversion are in here.  It'll also show it to the user."""


    #this part will do all the heavy lifting.  It will do the work then show the whole byte at once."""
    


