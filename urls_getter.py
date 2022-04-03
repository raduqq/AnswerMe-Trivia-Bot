from googlesearch import search


def get_urls(question, num_urls):
    urls = []

    for curr_url in search(question):
        urls.append(curr_url)

    chosen_urls = []

    for url in urls:
        if len(chosen_urls) >= num_urls:
            break

        if 'wikipedia' in url:
            chosen_urls.append(url)

    if len(chosen_urls) == num_urls:
        return chosen_urls

    for url in urls:
        if len(chosen_urls) >= num_urls:
            break

        if 'wikipedia' not in url:
            chosen_urls.append(url)

    return chosen_urls
