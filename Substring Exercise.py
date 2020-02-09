s = input("Hello, please input your desired string: ").lower()

result = s[0]
substring = s[0]

for i in s[1:]:

    if i >= substring[-1]:
        substring += i

        if len(substring) > len(result):
            result = substring
    else:
        substring = i

print("Longest substring in alphabetical order is:", result)