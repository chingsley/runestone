import random


def generate_str(test_str, target_str, char_pool):
    str = ''
    if(test_str == ''):
        return '8282828282828282828282828282'

    for i in range(len(target_str)):
        if test_str[i] == target_str[i]:
            str += target_str[i]
        else:
            str += char_pool[random.randrange(len(target_str) - 1)]

    return str


def test(test_str, target_str):
    count_same_str = 0
    for i in range(len(target_str)):
        if test_str[i] == target_str[i]:
            count_same_str += 1

    return count_same_str * 100 / len(target_str)


def main():
    char_pool = 'abcdefghijklmnopqrstuvwxyz '
    target_str = "methinks it is like a weasel"
    score = 0
    best_score = 0
    test_str = ''
    while score < 100:
        test_str = generate_str(test_str, target_str, char_pool)
        score = test(test_str, target_str)
        if score > best_score:
            best_score = score
            print(f"{test_str}\t=>\tscore: {score}%")


main()
