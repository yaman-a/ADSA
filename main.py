def addSchoolMethod(I1, I2, base):

    num1 = int(I1, base)
    num2 = int(I2, base)

    sumResult = num1 + num2

    return convertToBase(sumResult, base)

def karatsuba(x, y, base):
    num1 = int(x, base)
    num2 = int(y, base)

    if num1 < base and num2 < base:
        return num1 * num2

    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)

    split_position = max_len // 2
    x1, x0 = x[:-split_position], x[-split_position:]
    y1, y0 = y[:-split_position], y[-split_position:]

    z2 = karatsuba(x1, y1, base)
    z0 = karatsuba(x0, y0, base)

    x1_plus_x0 = addSchoolMethod(x1, x0, base)
    y1_plus_y0 = addSchoolMethod(y1, y0, base)

    z1 = karatsuba(x1_plus_x0, y1_plus_y0, base) - z2 - z0

    return z2 * (base ** (2 * split_position)) + z1 * (base ** split_position) + z0

def convertToBase(number, base):
    if number == 0:
        return "0"
    
    result = ""
    while number > 0:
        remainder = number % base
        result = str(remainder) + result
        number = number // base

    return result

def main():
    inputLine = input().strip()
    I1Str, I2Str, baseStr = inputLine.split()

    base = int(baseStr)

    sumResult = addSchoolMethod(I1Str, I2Str, base)
    productResult = karatsuba(I1Str, I2Str, base)

    sumBaseB = convertToBase(int(sumResult, base), base)
    productBaseB = convertToBase(productResult, base)

    print(f"{sumBaseB} {productBaseB} 0")

if __name__ == "__main__":
    main()
