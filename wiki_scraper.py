import wikipedia


def get_wiki_content(url):
    tokens = url.split('/')
    query = tokens[len(tokens) - 1]
    page_name = wikipedia.search(query, results=1)

    page = wikipedia.page(page_name)
    content = page.content

    return content
