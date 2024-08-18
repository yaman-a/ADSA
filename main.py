def addSchoolMethod(I1, I2):
    num1 = int(I1, base)
    num2 = int(I2, base)
    sumResult = num1 + num2
    return sumResult

def karatsuba(x, y):
    num1 = int(x, base)
    num2 = int(y, base)

    if num1 < 10 or num2 < 10:
        return num1 * num2

    # Adjust the lengths
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)

    # Split x and y
    split_position = max_len // 2
    x1, x0 = x[:-split_position], x[-split_position:]
    y1, y0 = y[:-split_position], y[-split_position:]

    # Recursively calculate z2, z1, and z0
    z2 = karatsuba(x1, y1)
    z0 = karatsuba(x0, y0)
    z1 = karatsuba(addSchoolMethod(x1, x0), addSchoolMethod(y1, y0)) - z2 - z0

    # Combine results using base ** (half_length)
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
    inputLine = input("Enter I1, I2, and base separated by spaces: ").strip()
    I1Str, I2Str, baseStr = inputLine.split()

    global base
    base = int(baseStr)

    sumResult = addSchoolMethod(I1Str, I2Str)
    productResult = karatsuba(I1Str, I2Str)

    sumBaseB = convertToBase(sumResult, base)
    productBaseB = convertToBase(productResult, base)

    print(f"{sumBaseB} {productBaseB} 0")

if __name__ == "__main__":
    main()
