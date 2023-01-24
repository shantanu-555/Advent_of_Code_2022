with open('input1.in') as file:
    data = [i for i in file.read().strip().split("\n")]
    
# print(data)

''' Traversing every string in our file '''
count = 0
lst = []

for item in data:
    if item == '':
        lst.append(count)
        count = 0
    else:
        num = int(item)
        count += num
        
print(f"Answer to part 1 is {sorted(lst)[-1]}")
print(f"Answer to part 2 is \
{sorted(lst)[-1] + sorted(lst)[-2] + sorted(lst)[-3]}")
