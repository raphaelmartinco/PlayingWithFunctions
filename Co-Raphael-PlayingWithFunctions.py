#ID Number: 205833
#Surname: Co
#Year and Course: 2 BS ITE

#Problem 1
def problem_1(number):
    factorial = 1
    if number == 0 or number == 1:
        return 1
    for i in range(1, number+1):
        factorial *= i

    return factorial
try:
    number = int(input("Enter the number: "))
except:
    print("please enter positive number")
output = problem_1(number)

print("Problem_1(",number,")","=>",output)

#Problem 2
def problem_2(passphrase):
    count = 1
    guess = input ("Input password: ")
    
    if guess == passphrase:
        return ("1")
    
    while guess != passphrase:
        guess_2 = input ("try again: ")
        if guess_2 == passphrase:
            return ("1")
        else:
            count += 1 
            if count == 3:
                return ("0")
                         
problem_2("rapha") 

#Problem 3
def problem_3(temp,original_format, new_format):
    
    if original_format == "fahrenheit" and new_format == "fahrenheit":
        return (temp)
    elif original_format == "fahrenheit" and new_format == "kelvin":
        return (((temp - 32)*(5/9) + 273.15))
    elif original_format == "fahrenheit" and new_format == "celsius":
        return ((temp - 32)* (5/9))
    
    elif original_format == "celsius" and new_format == "celsius":
        return(temp)
    elif original_format == "celsius" and new_format == "fahrenheit":
        return ((temp * 9/5) + 32)
    elif original_format == "celsius" and new_format == "kelvin":
        return (temp + 273)
    
    elif original_format == "kelvin" and new_format == "kelvin":
        return (temp)
    elif original_format == "kelvin" and new_format == "fahrenheit":
        return ((((temp - 273.15) * (9/5)) + 32))
    elif original_format == "kelvin" and new_format == "celsius":
        return (temp - 273.15)
                     
temp = float(input("Temperature is: "))
                     
original_format = str(input("What is the temperature currently recorded in: "))
                            
new_format = str(input("What would you like it to be converted to: "))    
                     
output = problem_3(temp, original_format, new_format)
                     
print("problem_3(" , temp , ",", original_format , "," , new_format , ")" , "=>" , output)            

#Problem 4
def problem_4(amount):
    piso = amount // 100
    quarters = (amount % 100) // 25
    tens = amount%25 // 10
    fives = amount % 25 % 10 // 5
    ones = amount % 5 
    
    output = print("1P:" , str(piso) , "/" , "25C:" , str(quarters) , "/" , "10C:" , str(tens) , "/" , "5C:" , str (fives) , "/" , "1C:" , str(ones))
    
    return (output)
    
#Problem 5
def problem_5(message):
    l = []
    for i in message:
        if ord(i) >= 65 and ord(i) <= 90:
            x = chr(ord(i) + 32)
        else:
            x = chr(ord(i) - 32)
        l.append(x)
        a = "".join(l)
    return a
        
problem_5(input("Input word: "))