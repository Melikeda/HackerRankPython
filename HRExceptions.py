for _ in range(int(input())):
    try:
        
        nums = input().split()
        a = int(nums[0])
        b = int(nums[1])
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
