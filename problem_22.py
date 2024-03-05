# names scores https://projecteuler.net/problem=22

f = open(r"project_euler\project_euler\0022_names.txt", "r")

names = f.read()
names = names[1:len(names)-1].split('","') 
names.sort()

d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

score_t = 0
for i in range(len(names)):
    score_w = 0
    for l in names[i]:
        score_w += d[l]
    score_t += score_w * (i+1)

print(score_t)

