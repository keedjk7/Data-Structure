def recursive(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num*recursive(num-1)

if __name__ == "__main__":
    inp = int(input("Enter Number : "))
    print("{}! = {}".format(inp,recursive(inp)))