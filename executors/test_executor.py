from jina import Executor


class MyTestExecutor(Executor):
    def invoke(self, **kwargs):
        print('INVOKE__' * 5)
