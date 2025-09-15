if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    number = list(arr)
    
    unique=set(number)
    number_unique = list(unique)
    number_unique.sort()
    
    print(number_unique[-2])
    
