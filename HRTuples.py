if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t = tuple(integer_list)

    print(hash(t))  # “Hash”, bir veri yapısını veya değeri sabit uzunlukta bir sayıya dönüştürme işlemidir.
