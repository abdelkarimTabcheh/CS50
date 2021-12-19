from cs50 import get_string

# Credit and Copy_Credit
credit = get_string("Number: ")

copy_credit = credit[::-1]

# Total 
total_sum = sum([(int(x) * 2) // 10 + ((int(x) * 2) % 10) for x in copy_credit[1::2]]) + sum([int(x) for x in copy_credit[0::2]])

# Conditions of card
if total_sum % 10 == 0:
    # Could
    if len(credit) == 15 and credit[0:2] in ['34', '37']:
        print('AMEX')
    elif len(credit) == 16 and 51 <= int(credit[0:2]) <= 55:
        print('MASTERCARD')
    elif len(credit) in [13, 16] and credit[0] == '4':
        print('VISA')
    else:
        print('INVALID')
else:
    print('INVALID')
