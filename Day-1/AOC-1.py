with open('input1.in') as file:
    data = [i for i in file.read().strip().split("\n")]
    
# print(data)

''' Traversing every string in data and appending to lst '''
count = 0
lst = []

for item in data:
    if item == '':          # Before new elf begins:
        lst.append(count)   # Append previous elf's calories
        count = 0           # Reset count
        
    else:                   # For the same elf:
        num = int(item)         
        count += num        # Sum calories

sorted_lst = sorted(lst)    # Sort lst in ascending order

print(f"Answer to part 1 is {sorted_lst[-1]}")
print(f"Answer to part 2 is \
{sorted_lst[-1] + sorted_lst[-2] + sorted_lst[-3]}")
