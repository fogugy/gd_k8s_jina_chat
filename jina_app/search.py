import os

from jina import Flow
from jina.parsers.helloworld import set_hw_chatbot_parser


def search():
    f = Flow.load_config('flow.yml')

    with f:
        f.use_rest_gateway(args.port_expose)
        f.block()


if __name__ == '__main__':
    args = set_hw_chatbot_parser().parse_args()
    search()
