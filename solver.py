f = open("password.txt", "r")
list = f.readlines()
f.close()
position = {}

for word in list:
    for i in range(0, 3):
        if word[i] not in position:
            position[word[i]] = 0
        
        for j in range(i+1, 3):
            if word[j] not in position:
                position[word[j]] = 0

            if position[word[j]] <= position[word[i]]:
                position[word[i]] = position[word[j]] -1
                for c in position:
                    if c != i and position[c] <= position[word[i]]:
                        position[c] -= 1
    
password = {}
for c in position:
    if position[c] in password:
        password[position[c]].append(c)
    else:
        password[position[c]] = [c]

for num in sorted(password.keys()):
    print(f"{num}: {password[num]}")

for num in sorted(password.keys()):
    print(*password[num], sep = "/", end="")
