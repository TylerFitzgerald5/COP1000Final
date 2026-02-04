def PCutBefore(input, reps = 1):
    output = input
    for i in range(reps):
        index = output.find("|") + 1
        output = output[index:]
    return output


def PCutAfter(input):
    index = input.find("|")
    return input[:index]

print(PCutAfter("player|p1|buhuizhibuyutianti|blackbelt-gen4dp|1159"))