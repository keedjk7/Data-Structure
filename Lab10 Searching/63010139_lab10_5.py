def candice(goods, weight, box):
    goodsitr = 0
    for i in range(box):
        weightinbox = 0
        while True:
            if goodsitr == len(goods):
                return True
            if weight >= goods[goodsitr] + weightinbox:
                weightinbox = weightinbox + goods[goodsitr]
                goodsitr+=1
            else:
                break
    return False

if __name__ == "__main__":
    inp = input("Enter Input : ").split("/")
    goods = []
    for i in inp[0].split(" "):
        goods.append(int(i))
    box = int(inp[1])
    weight = 0
    for i in goods:
        if i > weight:
            weight = i
    while candice(goods, weight, box) == False:
        weight += 1
    print("Minimum weigth for {} box(es) = {}".format(box, weight))