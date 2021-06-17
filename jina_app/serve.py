import os

import urllib.request

from jina import Flow
from jina.logging.profile import ProgressBar
from jina.parsers.helloworld import set_hw_chatbot_parser
from jina.types.document.generators import from_csv


def serve(args):
    targets = {
        'covid-csv': {
            'url': args.index_data_url,
            'filename': os.path.join(args.workdir, 'dataset.csv'),
        }
    }

    download_data(targets, args.download_proxy, task_name='download csv data')

    f = Flow.load_config('flow.yml')

    with f:
        with open(targets['covid-csv']['filename']) as fp:
            f.index(from_csv(fp, field_resolver={'question': 'text'}))

        print('Flow block')
        f.block()


def download_data(targets, download_proxy=None, task_name='download fashion-mnist'):
    """
    Download data.

    :param targets: target path for data.
    :param download_proxy: download proxy (e.g. 'http', 'https')
    :param task_name: name of the task
    """
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    if download_proxy:
        proxy = urllib.request.ProxyHandler(
            {'http': download_proxy, 'https': download_proxy}
        )
        opener.add_handler(proxy)
    urllib.request.install_opener(opener)
    with ProgressBar(task_name=task_name, batch_unit='') as t:
        for k, v in targets.items():
            if not os.path.exists(v['filename']):
                urllib.request.urlretrieve(
                    v['url'], v['filename'], reporthook=lambda *x: t.update_tick(0.01)
                )


if __name__ == '__main__':
    args = set_hw_chatbot_parser().parse_args()
    args.workdir = os.environ['HW_WORKDIR']

    serve(args)
