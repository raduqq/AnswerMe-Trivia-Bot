from googlesearch import search


def get_urls(question, num_urls):
    urls = []

    # Get all relevant URLs
    for curr_url in search(question):
        urls.append(curr_url)

    chosen_urls = []

    for url in urls:
        if len(chosen_urls) >= num_urls:
            break

        # Choose URL if wikipedia
        if 'wikipedia' in url:
            chosen_urls.append(url)

    if len(chosen_urls) == num_urls:
        return chosen_urls

    # If no of picked URLs is not reach, fill with rest until limit
    for url in urls:
        if len(chosen_urls) >= num_urls:
            break

        if 'wikipedia' not in url:
            chosen_urls.append(url)

    return chosen_urls
