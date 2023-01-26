with open('input3.in') as file:
    data = [i for i in file.read().strip().split("\n")]

# print(data)

from string import ascii_letters

total = 0

for rucksack in data:
    half = len(rucksack)//2
    
    left = set(rucksack[:half])
    right = set(rucksack[half:])
    
    for priority, char in enumerate(ascii_letters):
        if char in left and char in right:
            total += priority + 1
            
print(f"Answer for part 1 is {total}")

# === Part 2 ===

j = 3
total = 0
for i in range(0, len(data), 3):
    rucksacks = data[i:j]
    j += 3
    
    for priority, char in enumerate(ascii_letters):
        if  char in rucksacks[0] and\
            char in rucksacks[1] and\
            char in rucksacks[2]:
                total += priority + 1

print(f"Answer for part 2 is {total}")

                
            
        
    
    
    