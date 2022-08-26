hrs = input('Enter Hours: ')
try:
    float_hrs = float(hrs)
except:
    print ('Error, please enter numeric input')
    exit()

rate = input('Enter Rate: ')
try: 
    float_rate = float(rate)
except:
    print ('Error, please enter numeric input')
    exit()
    
# print (float_hrs, "and", float_rate)

if float_hrs > 40:
    regpay = float_hrs * float_rate
    otpay = (float_hrs - 40) * (float_rate * 0.5)
    pay = regpay + otpay
else :
    pay = float_hrs * float_rate

print('Pay:', pay)