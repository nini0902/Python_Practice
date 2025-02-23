import textwrap

def wrap(string, max_width):
  #以固定長度分段 string 並以換行隔開
    return "\n".join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
