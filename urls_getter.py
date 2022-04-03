from googlesearch import search

from string import punctuation
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def get_essential_words(worf_quote):
    worf_quote = worf_quote.translate(str.maketrans('', '', punctuation))
    words_in_quote = word_tokenize(worf_quote)

    stop_words = set(stopwords.words("english"))
    filtered_list = []

    for word in words_in_quote:
        if word.casefold() not in stop_words:
            filtered_list.append(word)

    lemmatizer = WordNetLemmatizer()

    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_list]

    return ' '.join(lemmatized_words)


def get_urls(question, num_urls):
    urls = []

    # Summarized question
    # summarized_q = get_essential_words(question)
    # print(summarized_q)

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
