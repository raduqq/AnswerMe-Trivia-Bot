from bs4 import BeautifulSoup
import requests
import wikipedia


def get_urls_context(urls):
    context = ''

    for url in urls:
        context += get_url_context(url)

    return context


def get_url_context(url):
    content = ""

    try:
        tokens = url.split('/')
        query = tokens[len(tokens) - 1]
        page_name = wikipedia.search(query, results=1)

        page = wikipedia.page(page_name)
        content = page.summary
    except:
        # Fetch URL Content
        r = requests.get(url)

        # Get body content
        soup = BeautifulSoup(r.text, 'html.parser').select('body')[0]

        # Initialize variable
        paragraphs = []

        # Iterate through all tags
        for tag in soup.find_all():

            # Check each tag name
            # For Paragraph use p tag
            if tag.name == "p":
                # use text for fetch the content inside p tag
                paragraphs.append(tag.text)

        # Concatenate paragraph in final content
        for p in paragraphs:
            content = content + p
    finally:
        return content
