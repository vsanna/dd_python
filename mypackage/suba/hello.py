# __all__ = ['Hello', 'hello']

class Hello:
    def __init__(self):
        pass


def hello(msg: str):
    print(f'hello {msg}')

def internal_without_underscore_hello():
    hello("internal_without_underscore_hello")

def _internal_hello():
    hello("internal")