inp = input('Enter Input : ').split('/')
left,right = list(map(int, inp[0].split())), list(map(int, inp[1].split()))
for i in right:
    result = 99999999
    for j in left:
        if j > i and j < result:
            result = j

    if result == 99999999:
        print("No First Greater Value")
    else:
        print(result)