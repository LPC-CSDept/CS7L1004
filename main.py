class Point:
    #########################################
    # Code your program here
    #########################################
   


def main():
    p = Point(10, 20)
    print(f'Point x={p.x} y={p.y}')
    p.x = 100
    p.y = 200
    print(f'Point x={p._x} y={p._y}')


if __name__ == '__main__':
    main()
