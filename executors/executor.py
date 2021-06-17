from jina import Executor


class MyRemoteExecutor(Executor):
    def qux(self, **kwargs):
        print(f'qux is called: {kwargs}')