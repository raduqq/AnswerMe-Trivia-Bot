from bs4 import *
import requests
import wikipedia


def get_wiki_content(url):
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
        count = 0
        max_count = 3

        # Iterate through all tags
        for tag in soup.find_all():

            # Check each tag name
            # For Paragraph use p tag
            if count == max_count:
                break

            if tag.name == "p":
                # use text for fetch the content inside p tag
                paragraphs.append(tag.text)
                count += 1

        # Concatenate paragraph in final content
        for p in paragraphs:
            content = content + p
    finally:
        return content
