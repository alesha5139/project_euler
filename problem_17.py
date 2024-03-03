# number letter counts https://projecteuler.net/problem=17

ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundreds = ['', 'onehundred', 'twohundred', 'threehundred', 'fourhundred', 'fivehundred', 'sixhundred', 'sevenhundred', 'eighthundred', 'ninehundred']

total = 0
d={}

for i in range(1,1000):
    s = ''
    hundreds_digit = i % 1000 // 100
    tens_digit = i % 100 // 10
    ones_digit = i%10
    if hundreds_digit != 0:
        s += hundreds[hundreds_digit]
        if tens_digit != 0 or ones_digit != 0:
            s += 'and'
    if tens_digit == 1:
        s += teens[ones_digit]
    else:
        s += tens[tens_digit]
        s += ones[ones_digit]

    total += len(s)
    d[s]=len(s)

total += len('onethousand')
print(total)