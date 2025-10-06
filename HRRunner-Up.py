if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))  # Tek satırda n puanı al

    scores.sort(reverse=True)  
    highest = scores[0]

    for score in scores:
        if score < highest:    
            runner_up = score
            break

    print(runner_up)
