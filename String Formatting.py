def print_formatted(n):
    w = n.bit_length()

    for i in range(1, n+1):
        #固定寬度為最大值的bin長度且靠右
        print("{:>{}} {:>{}} {:>{}} {:>{}}".format(
            i, w,
            oct(i)[2:], w,
            hex(i).upper()[2:], w,
            bin(i)[2:], w
        ))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
