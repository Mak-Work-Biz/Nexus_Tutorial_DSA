def split_and_join(line):
    # write your code here
    line_split = line.split(" ")
    line_joined = '-'.join(line_split)
    return line_joined
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
