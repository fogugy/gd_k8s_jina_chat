import os

from jina import Flow
from jina.parsers.helloworld import set_hw_chatbot_parser
from jina.types.document.generators import from_csv
from my_executors import MyTransformer, MyIndexer


def index(args):
    targets = {
        'covid-csv': {
            'url': args.index_data_url,
            'filename': os.path.join(args.workdir, 'dataset.csv'),
        }
    }

    f = Flow.load_config('flow.yml')

    with f, open(targets['covid-csv']['filename']) as fp:
        f.index(from_csv(fp, field_resolver={'question': 'text'}))


if __name__ == '__main__':
    args = set_hw_chatbot_parser().parse_args()
    args.workdir = os.environ['HW_WORKDIR']

    index(args)
