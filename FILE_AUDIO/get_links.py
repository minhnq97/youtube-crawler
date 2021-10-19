import random
f1 = open("URL_MIENNAM_1.txt", "w")
f2 = open("URL_MIENNAM_2.txt", "w")



with open("URL_MIENNAM_FULL.txt", "rt") as f:
    lines = f.read().splitlines()
    num_files = len(lines) // 2
    print(len(lines))
    while num_files > 0:
        choice = random.choice(lines)
        index = lines.index(choice)
        del lines[index]
        print(len(lines))
        f1.write(choice)
        f1.write("\n")
        num_files -= 1
    for line in lines:
        f2.write(line)
        f2.write("\n")
