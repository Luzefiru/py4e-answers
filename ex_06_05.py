text = "X-DSPAM-Confidence:    0.8475"

colon_pos = text.find(':')
extracted = text[(colon_pos + 1):]

# strip the white spaces
extracted = extracted.strip()

# test: print(extracted)

# convert str to float
float_converted = float(extracted)

print('%g' % float_converted)

print('The type is:', type(float_converted))