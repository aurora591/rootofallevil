def sqr(num):
    """
    this function gets a number and return his sqrt if he is a number and not negative
    :param num: int of number
    :return: sqrt of the num
    """
    is_num = False
    for i in range(10):
        if num == i or num == (i*-1):
            is_num = True
    if not is_num:
        raise TypeError("not expects not digit input")
    else:
        if num < 0:
            raise ValueError("not expects negative int")
        else:
            return num ** 0.5


def main():
    print(sqr(-9))
if __name__ == "__main__":
    main()