import sys

if __name__ == "__main__":

    # for line in sys.stdin:
    #     print(line, type(line))

    # data = input()
    # print(data, type(data))
    # t = dict(eval(data))
    # print(t, type(t))

    # another way
    lines = sys.stdin.readlines()
    print(lines)

    # use cont+d in m mac to end the input or ctrl + z in windows
    # after ctrl + d we get the values in list 

    # how do we convert respective values into the given types e.g str, list, dict, tuple etc. 
    # may be we use eval
    for item in lines:
        if isinstance(eval(item), str):
            print(item, " - is a str", type(eval(item))); 
        elif isinstance(eval(item), dict):
            print(item, " - is a dict", type(eval(item))); 
    


