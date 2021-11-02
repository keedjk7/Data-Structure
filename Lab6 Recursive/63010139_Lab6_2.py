def recursive(word):
    if len(word) < 2: 
        return True
    if word[0] != word[-1]:
        return False
    
    return recursive(word[1:-1])


if __name__ == "__main__":
    inp = input("Enter Input : ")
    check = recursive(inp)
    if check == False:
        print("'{}' is not palindrome".format(inp))
    else:
         print("'{}' is palindrome".format(inp))