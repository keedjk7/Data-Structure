def gcd (max,min):
    if min == 0:
        return max
    if max == 0:
        return min

    if max % min == 0:
        return min
    

    return gcd(min,max%min)

if __name__ == "__main__":
    num1,num2 = (input("Enter Input : ").split(" "))
    temp_num1 = int(num1)
    temp_num2 = int(num2)

    if temp_num1 < 0:
        temp_num1 *= -1
    if temp_num2 < 0:
        temp_num2 *= -1

    if temp_num1 == 0 and temp_num2 == 0:
        print("Error! must be not all zero.")
    elif temp_num1>temp_num2 or (int(num1) == 0 and int(num2)<0) :
        print("The gcd of {} and {} is : {}".format(num1,num2,gcd(temp_num1,temp_num2)))
    else:
        print("The gcd of {} and {} is : {}".format(num2,num1,gcd(temp_num2,temp_num1)))