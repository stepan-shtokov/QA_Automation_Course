def digit_root(num):
    while num > 9:
        num_str = str(num)
        sum_digits = 0
        for digit in num_str:
            sum_digits += int(digit)
        num = sum_digits
    return num
print(digit_root(4851))
print(digit_root(97569))
print(digit_root(889987))