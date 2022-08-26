# asks the user to input hours & checks if the value is a number
hrs = input('Enter Hours: ')
try:
    float_hrs = float(hrs)
except:
    print ('Error, please enter numeric input')
    exit()

# asks the user to input rate & checks if the value is a number
rate = input('Enter Rate: ')
try: 
    float_rate = float(rate)
except:
    print ('Error, please enter numeric input')
    exit()
    

# defines the 'computepay' function, calculates pay, adding overtime pay as half normal salary past 40 hours.
def computepay(x, y):
    # print('In computepay', x, y)

    if x > 40:
        regpay = x * y
        otpay = (x - 40) * (y * 0.5)
        pay = regpay + otpay
        # print('Returning', pay)
        return pay
    else:
        pay = x * y
        # print('Returning', pay)
        return pay

print('Pay', computepay(float_hrs, float_rate))