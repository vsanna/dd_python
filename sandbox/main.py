"""
## todo
- 並行プログラミングできる? thread safeなlist/mapあるか
- packageのsample作る
- decoratorのsample作る
- coroutineのsample
    - 内部的にはthread/cpuをどう使っているのか

## note
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
- list系
    - all(list), any(list), not any(list)
    - map(func, list)
        - 複数list渡せる map(lambda animal, fruit: ..., animals, fruits)
    - filter(func, list)
    - functools.reduce(func, list)
        - operatorモジュールを使って簡易化
    - collections.deque でqueueデータ構造を使える
- tuple
    - イミュータブルなリスト t1 = (1, 'hoge', False)
    - len, min, max, z in t, z not in t, t1 + t2, t * n
- set
    - s1 = {1, 2, 3}
    - s1 | s2, s1 & s2, s1 - s2, s1 ^ s2
    - s1.issubset(s2), s1.issuperset(s2), s1.isdisjoint(s2)
    - set comprehension: {int(i) for i in data if i > 0}
- dict
    - keyに使えるもの: int, str, bytes, tuple, frozenset ... 案外少ない
    - 辞書にもcomprehensionがある
- 正規表現
    - re.compile(raw文字列)
    - search, findall, finditer, match
    - group, start, end, span, pos, endpos, lastindex
    - option: IGNORECASE, MULTILINE, VERVOSE(X)
    - 最短マッチ: . + * -> .? +? *?
    - 名前付きキャプチャ: ?P<area>
    - 参照しないグルーピング: (?:)
    - あと読み先読み: (?=B) (?!B) (?<=B) (?<!B)
- file操作
    - with open(...) as file:
    - for line in file.readlines()よりも for line in file. 一気にメモリロードさせない
    - for raw in csv.reader(file, delimiter='\t') でcsv/tsv読み込み
    - writer = csv.writer(file, delimiter='\t\); writer.writerows(list[list[value]])
- シリアライズ
    - Pythonのシリアライズはpickleという。つまり言語の互換性ない~
    - dump(object, file, protocol: int)
    - load(file)
- http requests
    - import requests
- その他
    - math, random, random
- データ型変換, 判定
    - 変換: bool(val), list(value)などなど
        - pythonは暗黙的な型変換をあまりしない
    - type(val) ... これは実はconstructor. class typeが存在する
    - isinstance(val)
    - dir(module または class) でそのclassに属する要素(とは?)を返す
- 関数
    - immutableは値渡し(tupleであっても), mutableは値渡し
        - 正確には参照の値渡し。javaもそう。
        - よっていわゆる "copy of reference"に値をセットしても呼び出し元に影響を与えられない現象が起こる
    - Pythonにはブロックスコープない!
    - tupleで返してdeconstして受け取る、というパターン
    - 高階関数の取り扱いかのう
    - lambda関数: 複数文かけない...
- The Zen of Python
- decorator
    - 関数を受け取って関数を返す関数を定義するだけ。簡単
    - 引数を受け取るdecoratorとで微妙に実装のパターンがややこしいが
- generator
    - yieldを用いるcoroutine的なもの。suspendできる
    - generator関数の戻り地はgeneratorオブジェクト。
    - gen.send(val)で値を送る
- module
    - 1ファイル。。関数 / 変数 / 型を持てる
    - __name__
        - scriptとして呼び出された場合は"__main__", moduleとして呼び出された場合は別の値が入る。
        - ここには本来テストコードを書くらしい
    - moduleファイル
        - __all__変数にexportする関数を明記する
        - _hoge とunderscoreを戦闘につけた関数はexportされない
    - moduleの検索先(classpath的なもの)
        - current directory
        - PYTHONPATHの中
        - sys.pathで確認できる
- package
    - 複数moduleをまとめ合わせるdirectory. 単なるdirectory
    - __init__.pyはpackage初期化のためのファイル。なくてもよく、その場合はnamespace packageになる
        - サブパッケージの中身をimportしておくなど
- 非同期処理 = coroutine!
    - asyncio packageを使う
        - 3.4まではgeneratorをつかってcoroutineしていたが3.5からはnative coroutineがサポート. こちらを使うべき
    - 通常関数にasyncキーワードを付け、その呼出にawaitをつける
    - 実体はpromise. Kotlinと異なり値を返さずcoroutine = promiseを返す
    - 実行主体としてのevent_loopは手で呼び出す. ここがKotlinと大きく違う
    - そういう意味ではよりpromiseより...そして呼び出し方に違いがある
        - 通常の関数下でもasync関数呼べる(kotlinは呼べない). 一方で返り値は値ではなくcoroutine
    - async関数は "coroutine = promise"を返す
    - asyncio.get_event_loop().run_until_complete(print_sleep())
    - 非awaitableなコード(例えばrequests packageのhttp callなど)をawaitableにする
        - res = await asyncio.run_in_executor(None, requests.get, url) とすることでawaitableにできる
    - 非同期処理のエントリーポイントとなる(そこから先が非同期処理あり)をmain関数として、asyncio.runを一回だけ呼び出すのがよくある書き方
    - awaitable オブジェクト: coroutine, task, future
        - coroutine: promise
        - future: 低レベルのクラス。applicationからは使わない
        - task: coroutineを並列実行するためのもの。await asyncio.create_task(print_sleep()) は並列処理になる
            - coroutine 3つを連続してawaitすると ひとつあたりの処理時間 * 3かかるが、task 3つをawaitすると1つ分ですむ(いわゆる真の並行実行)
- documentation
    - docstringで書くのが通常。いくつかのスタイルパターンがある
    - Sphinx: docsを自動生成してくれる
    - 関数アノテーション: 型annotation. 実は説明書きもつけられる
        - __annotations__でアクセス可能
- class
    - __slots__ インスタンス変数に事由に追加できるものをホワイトリストで明示する
    - @property, @name.setter
    - 複数継承可能. 同名メソッドの名前解決は"継承順" かつ 深さ優先探索
    - instance method / class method / static method
    - 移譲
        - 普通にconstructorに移譲先objectを渡す
    - mixin
        - attrを持たないclassをextendすることでなす。うーむ
    - ポリモーフィズム
        - 抽象クラス(@abstractmethodを持つクラス)を継承させることでメソッドの保持を強制/担保
    - isinstance(obj, klass) で そのクラスまたはその派生クラスのインスタンスであることを確認
- 例外
    - class MyError(Exception)
    - 基本中身はpassでOK.
- data class
    - __init__, __repr__(toString相当), __eq__, __lt__, __le__, __gt__, __ge__, __hash__ を自動生成
    - attrをconstructorではなくクラス定義直下における
    - dataclass.fields(Person) でFieldオブジェクト取得
    - dataclass.replace(user, name="new name") でcopy取得
- metaclass
    - 動的にclassを生成する仕組み. class decoratorとかで使うのかな? skip

"""
import asyncio
import functools
import itertools
import operator
import pickle
import re


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

    print('=========')
    for animal, fruit in itertools.zip_longest(animals, fruits):
        print(f'{animal=} {fruit=}')

    # Iterator[int]. listではない!この時点では多分計算走らないとか?
    # NOTE: lambdaは改行できるが2つの式を含めないっぽい? andは苦肉の策でいれた。
    mapped = map((lambda animal: print("hey")), animals)
    print("right after mapped")
    list(mapped)
    """
    right after mapped 
    hey // lazy evaluation
    hey
    hey
    """

    comprehensive = [print("Hey") for animal in animals]
    print("right after comprehensive")
    list(comprehensive)
    """
    Hey // 先に評価
    Hey
    Hey
    right after comprehensive
    """

    result1 = functools.reduce(lambda accum, animal: accum + animal, animals)
    result2 = functools.reduce(operator.add, animals)
    print(f"{result1=}")
    print(f"{result2=}")
    # result1='dogcatmonkey'
    # result2='dogcatmonkey'

    # raw文字列: \をエスケープと認識せず、通常の文字列とみなす
    ptn = re.compile(r'([a-zA-Z0-9+-]{2,3}])')
    if searched := ptn.search("hey DJ!"):
        searched.group(0)
        searched.group(1)
    else:
        print("no match")

    # r=readonly, w=overwrite, a=append くらい覚えておけばいい気がする
    with open("./test.txt", mode="a") as file:
        file.write("Hello\n")

    with open("./test.txt", mode='r') as file:
        for line in file.readlines():
            print(line)

    # こちら推奨. 一気にメモリにロードせず一行ずつロード
    with open("./test.txt", mode='r') as file:
        for line in file:
            print(line)

    # dump要ファイルはbinaryファイルとして開く
    with open("./dump.txt", mode='ab') as file:
        user = {'name': "Tom", 'age': 100}
        pickle.dump(user, file)
    with open("./dump.txt", mode='rb') as file:
        obj = pickle.load(file)
        print(f'{obj=}')

    val = 100
    t_val = type(val) # class typeが存在する
    print(f'{t_val=}')
    print(f'{isinstance(val, int)=}') # class intも存在する
    # t_val=<class 'int'>
    # isinstance(val, int)=True


    data = 100
    print(f'before: {data=} {id(data)=}')
    def replace(d: int):
        d = 200 # copy of referenceに別の値をセットしても呼び出し元のreferenceには影響を与えない
        print(f'in:     {d=} {id(d)=}')
    replace(data)
    print(f'after:  {data=} {id(data)=}')
    # before: data=100 id(data)=4493297104
    # in:     d=200    id(d)   =4493300368
    # after:  data=100 id(data)=4493297104

    data = {'name': 'tom'}
    print(f'before: {data=} {id(data)=}')
    def replace(d: dict):
        d['name'] = 'Hoge'
        print(f'in:     {d=} {id(d)=}')
    replace(data)
    print(f'after:  {data=} {id(data)=}')
    # before: data={'name': 'tom'} id(data) =4494073664
    # in:     d={'name': 'Hoge'}   id(d)    =4494073664
    # after:  data={'name': 'Hoge'} id(data)=4494073664


    # referenceが指すobject自体を差し替えるような操作は "copy of reference"問題が生じる
    data = {'name': 'original'}
    print(f'before: {data=} {id(data)=}')
    def replace(d: dict):
        d = {'super': 'set'}
        print(f'in:     {d=} {id(d)=}')
    replace(data)
    print(f'after:  {data=} {id(data)=}')
    # before: data={'name': 'original'} id(data)=4534462912
    # in:     d={'super': 'set'}        id(d)   =4534462592
    # after:  data={'name': 'original'} id(data)=4534462912

    data = int(100)
    print(f'before: {data=} {id(data)=}')
    def replace(d):
        d = int(200)
        print(f'in:     {d=} {id(d)=}')
    replace(data)
    print(f'after:  {data=} {id(data)=}')
    # before: data=100 id(data)=4493297104
    # in:     d=200    id(d)   =4493300368
    # after:  data=100 id(data)=4493297104


    # funcを受け取ってfuncを返す
    def log_func(func):
        def inner(*args, **keywords):
            print(f"before: {func.__name__}, {args=}, {keywords=}")
            return func(*args)

        return inner

    @log_func
    def hello(msg):
        print(f"{msg=}")

    hello("WORLD")


    def cache_result(size=16):
        print("initializing cache..")
        cache = {}
        def outer(func):
            def inner(*args, **keywords):
                if args[0] in cache:
                    print("using cache...")
                    return cache[args[0]]

                print("calc..")
                result = func(*args, **keywords)
                if len(cache) > size:
                    del cache[args[0]]

                cache[args[0]] = result
                return result
            return inner
        return outer

    @cache_result(size=4)
    def hello(num: int):
        print(f"{num=}")

    # hello(1)
    # hello(2)
    # hello(3)
    # hello(4)
    # hello(5)
    # hello(5)
    # hello(6)
    # hello(6)
    # initializing cache..
    # calc..
    # num=1
    # calc..
    # num=2
    # calc..
    # num=3
    # calc..
    # num=4
    # calc..
    # num=5
    # using cache...
    # calc..
    # num=6

    async def print_sleep():
        await asyncio.sleep(10)
        print("from print_sleep")

    c = print_sleep()
    print(f'{c=}')
    # c=<coroutine object main.<locals>.print_sleep at 0x1079d5540>

    asyncio.get_event_loop().run_until_complete(print_sleep())


    def sample_func(msg: str):
        '''
        This func does nothing
        :param msg:
        :return:
        '''


class Animal:
    def __init__(self, name: str, age: int):
        self.name = name # setter
        self.__age = age

    def say(self):
        print(f'from Animal: {self.name=} {self.__age=}')

    # 内部的に __nameを作る。kotlinもそう。
    @property
    def name(self):
        # 無限ループ
        return self.name
        # return self.__name

    @name.setter
    def name(self, name: str):
        if isinstance(name, str):
            self.__name = name
        else:
            raise Exception("invalid value")



class HasId:
    def __init__(self, id: int):
        self.__id = id

    def say(self):
        print(f'from HasId: {self.__id=}')

class Runnable:
    def run(self):
        print("run....")

class User(Animal, HasId, Runnable):
    NUM = 0

    def __init__(self, firstname: str, lastname: str, age: int, id: int):
        super().__init__(firstname + ':' + lastname, age)
        # NOTE: HasIdの__init__は? => ない！深さ優先探索で発見したメソッドのみよべる
        # 故にidにはここで手入力.. つまりfieldを持つクラスを多重継承しない
        self.id = id

        # hidden fields
        self.__firstname = firstname
        self.__lastname = lastname

        User.NUM += 1

    @classmethod
    def get_num(cls) -> int:
        return User.NUM

    @staticmethod
    def debug():
        print("this is static method. it doesn't have self/cls.")

    def say_from_user(self):
        super().say()

class MyError(Exception):
    pass

if __name__ == "__main__":
    main()
    name = "Tom"
    age = 20
    print(f'{name} is {age} yo')
    print(f'{name=} is {age=} yo')
    # Tom is 20 yo
    # name='Tom' is age=20 yo
