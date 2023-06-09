class Rectangle:
    """
    ########################################
    Code Your Program here
    ########################################
    """


def main():

    # 1) Constructor
    r = Rectangle(10, 20)
    print(f'Height: {r.height} \t Width: {r.width}')

    # 2) Change the property values
    r.width = 200
    r.height = 100
    print(f'Height: {r.height} \t Width: {r.width}')

    # 3) Change the propery value directly
    r._height = 999
    print(f'Height: {r.height} \t Width: {r._width}')


if __name__ == '__main__':
    main()
