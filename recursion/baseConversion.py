def base_conversion(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return base_conversion(n // base, base) + convertString[n % base]


base_conversion(256, 16)