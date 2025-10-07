def split_and_join(line):
    
    splitt = line.split(" ")
    result = "-".join(splitt)
    
    return(result)
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
