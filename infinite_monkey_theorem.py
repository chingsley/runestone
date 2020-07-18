import random


def generate_str(strLen):
    char_pool = 'abcdefghijklmnopqrstuvwxyz '
    str = ''
    for i in range(strLen):
        str = str + char_pool[random.randrange(27)]

    return str


def test(test_str, target_str):
    count_same_str = 0
    for i in range(len(target_str)):
        if test_str[i] == target_str[i]:
            count_same_str += 1

    return count_same_str * 100 / len(target_str)


def main():
    target_str = "methinks it is like a weasel"
    score = 0
    best_score = 0
    while score < 100:
        test_str = generate_str(28)
        score = test(test_str, target_str)
        if score > best_score:
            best_score = score
            print(f"{test_str}\t=>\tscore: {score}%")


# target_str = "methinks it is like a weasel"
# test_str = generate_str(28)
# score = test(test_str, target_str)
# print(score)
main()
