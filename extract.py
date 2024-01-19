f = open("logs.txt")
str1 = "clearingSystem="
str2 = ", "
result = set()
for line in f:
	clearing = line.split(str1)[1].split(str2)[0]
	result.add(clearing)
print(result)
