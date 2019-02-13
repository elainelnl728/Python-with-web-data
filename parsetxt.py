import re
name = input("Enter a file name")
if len(name) < 1 : name = "regex_sum_91324.txt"
fhand = open(name)
sum = 0
for line in fhand:
    line = line.strip()
    numbers = re.findall('[0-9]+', line)
    for num in numbers:
        num = int(num)
        sum = sum + num
print(sum)
