i = int(input("What index is 'i' raised to: "))
result = {
    0: '1',
    1: 'i',
    2: '-1',
    3: '-i',
    4: '1'
}

remainder = i%4
ans = result[remainder]
print(f"i^{i} is : {ans}".format())
