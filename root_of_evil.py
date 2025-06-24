def sqr(num):
    if not str(num).isdigit():
        raise TypeError("not expects not digit input")
    if num < 0:
        raise ValueError("not expects negative int")
    return num ** 0.5


def main():
    print(sqr(9))
if __name__ == "__main__":
    main()

