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


# if __name__ == "__main__":
main()
