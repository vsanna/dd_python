"""
- 定数がない。
- range関数 range(start, end, skip)
- 比較演算子の is in and or
- switchがない
- 三項演算子 a if cond else b ... 覚えられない
- リスト内包表記
    - リストからリスト
    - [i * 2 for i in data] ... 覚えられるかこれ
    - [i for i in data if i > 10] ... filter関数に相当。どうしたって覚えられない
- try except else finally
- f'{name=} は {age=} です' という評価つき構文
"""


def main():
    try:
        1 / 0
    except Exception as ex:
        print(ex)
    else:
        print("everything goes fine")
    finally:
        print("always pass here")

    animals = ['dog', 'cat', 'monkey']
    fruits = ['apple', 'banana', 'orange', 'grape']
    for animal, fruit in zip(animals, fruits):
        print(f'{animal=} {fruit=}')

    for animal, fruit in itertools(animals, fruits):
        print(f'{animal=} {fruit=}')


if __name__ == "__main__":
    main()
    name = "Tom"
    age = 20
    print(f'{name} is {age} yo')
    print(f'{name=} is {age=} yo')
    # Tom is 20 yo
    # name='Tom' is age=20 yo
