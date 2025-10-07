if __name__ == '__main__':
    nested_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name, score])

    scores = sorted(set([score for name, score in nested_list]))   // # Tüm notları sırala ve tekrarları kaldır

    second_lowest = scores[1]

    names = [name for name, score in nested_list if score == second_lowest]

    for name in sorted(names):
        print(name)
