import main


def test_main_1():
    r = main.Rectangle(10, 20)
    print(f'Height: {r.height} \t Width: {r.width}')

    assert r.height == 10
    assert r.width == 20


def test_main_2():
    r = main.Rectangle(10, 20)
    print(f'Height: {r.height} \t Width: {r.width}')

    r._height = 100
    r._width = 200
    print(f'Height: {r.height} \t Width: {r.width}')
    assert r.height == 100
    assert r._height == 100
    assert r.width == 200
    assert r._width == 200

    r.height = 99
    r.width = 99
    assert r._width == 99
    assert r._height == 99
