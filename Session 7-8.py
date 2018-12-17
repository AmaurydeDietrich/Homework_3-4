string = 'azcbobobegghakl'
#string = input ("Please enter string here")

result = ''
substring = ''

for number in range(len(string)):

    numberbefore = number - 1

    if substring is "":
        substring = string[number]
        continue

    if string[number] >= string[numberbefore]:
        substring += string[number]
    else:
        temp = string[number]

    # print(temp, iterator - 1, end=" - ")

    if len(substring) > len(result):
        result = substring



print(result)