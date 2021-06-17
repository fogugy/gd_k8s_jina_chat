from jina import Client, Document


def print_matches(req):  # the callback function invoked when task is done
    for idx, d in enumerate(req.docs[0].matches[:3]):  # print top-3 matches
        print(f'[{idx}]{d.score.value:2f}: "{d.text}"')


def go():
    c = Client(host='localhost', port_expose=49000, restful=True)
    c.post('/search', Document(text='RRRREQUEEEEST!!!'), on_done=print_matches)


if __name__ == '__main__':
    go()
