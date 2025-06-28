def sqr(num):
    """
    this function gets a number and return his sqrt if he is a number and not negative
    :param num: int of number
    :return: sqrt of the num
    """
    abs_num = str(num).replace("-", "")
    if not abs_num.isdigit():
        raise TypeError("not expects not digit input")
    else:
        if num < 0:
            raise ValueError("not expects negative int")
        else:
            return num ** 0.5


def main():
    print(sqr(36))
if __name__ == "__main__":
    main()