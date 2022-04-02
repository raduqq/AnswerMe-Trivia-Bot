from googlesearch import search


def get_question_url(question):
    wiki = 'wikipedia'

    urls = []

    for curr_url in search(question):
        urls.append(curr_url)

    for url in urls:
        print(url)

    url = urls[0]
    for curr_url in urls:
        if wiki in curr_url:
            url = curr_url
            break

    return url

