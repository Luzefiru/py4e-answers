hrs = input('Enter Hours: ')
rate = input('Enter Rate: ')

float_hrs = float(hrs)
float_rate = float(rate)
# print (float_hrs, "and", float_rate)

if float_hrs > 40:
    regpay = float_hrs * float_rate
    otpay = (float_hrs - 40) * (float_rate * 0.5)
    pay = regpay + otpay
else :
    pay = float_hrs * float_rate

print('Pay:', pay)