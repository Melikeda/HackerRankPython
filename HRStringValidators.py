if __name__ == '__main__':
    s = input()
    
print(any(c.isalnum() for c in s))   
print(any(c.isalpha() for c in s))   
print(any(c.isdigit() for c in s))   
print(any(c.islower() for c in s))   
print(any(c.isupper() for c in s))   

# any() bir iterable alır (liste, tuple, string, generator vb.) ve içinde en az bir True değeri varsa True, yoksa False döner.
