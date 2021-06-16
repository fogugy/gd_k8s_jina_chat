import os

import webbrowser

from jina import Flow
from jina.parsers.helloworld import set_hw_chatbot_parser
from jina.logging.predefined import default_logger


def search():
    f = Flow.load_config('flow.yml')

    with f:
        f.use_rest_gateway(args.port_expose)

        url_html_path = 'file://' + os.path.abspath(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)), '../flask_app/templates/index.html'
            )
        )
        try:
            webbrowser.open(url_html_path, new=2)
        except:
            pass  # intentional pass, browser support isn't cross-platform
        finally:
            default_logger.success(
                f'You should see a demo page opened in your browser, '
                f'if not, you may open {url_html_path} manually'
            )

        if not args.unblock_query_flow:
            f.block()


if __name__ == '__main__':
    args = set_hw_chatbot_parser().parse_args()
    search()
