import main
import io
import sys
import re
import math
import types


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = 'Kim \n 100 80 70 60\n Bill \n 100 90 80 60 \n Mary \n 90 80 70 100'
    # sys.stdin = io.StringIO(datastr)

    p = main.Point(10, 20)
    print(f'Point x={p.x} y={p.y}')

    assert p.x == 10
    assert p.y == 20
    assert p._x == 10
    assert p._y == 20

    p._x = 100
    p._y = 200
    print(f'Point x={p.x} y={p.y}')
    assert p.x == 100, 'The x should be 100'
    assert p.y == 200, 'The y shoud be 200'

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*Elapsed'
    # regex_string += r'[\w,\W]*time'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, lines[1])
    # assert res != None
    # print(res.group())
