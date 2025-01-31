if __name__ == '__main__':
    s = input()
    #有沒有任何a~z or A~Z or 0~9
    print(any(char.isalnum() for char in s))
    #有沒有任何a~z or A~Z
    print(any(char.isalpha() for char in s))
    #有沒有任何0~9
    print(any(char.isdigit() for char in s))
    #有沒有任何a~z
    print(any(char.islower() for char in s))
    #有沒有任何A~Z
    print(any(char.isupper() for char in s))
