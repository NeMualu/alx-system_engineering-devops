#!/usr/bin/python3
""" Module for storing the count_words function. """
from requests import get

def count_words(subreddit, word_list, word_count=[], page_after=None):
    """
    Prints the count of the given words present in the title of the
    subreddit's hottest articles.
    """
    headers = {'User-Agent': 'HolbertonSchool'}
    word_list = [word.lower() for word in word_list]

    if not word_count:
        word_count = [0] * len(word_list)

    if page_after is None:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, page_after)

    response = get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        for child in response.json().get('data', {}).get('children', []):
            for i, word in enumerate(word_list):
                for title_word in [w.lower() for w in child.get('data', {}).get('title', '').split()]:
                    if word == title_word:
                        word_count[i] += 1

        if response.json().get('data', {}).get('after') is not None:
            count_words(subreddit, word_list, word_count, response.json().get('data', {}).get('after'))
        else:
            word_dict = {}
            for key_word in list(set(word_list)):
                index = word_list.index(key_word)
                if word_count[index] != 0:
                    word_dict[key_word] = word_count[index] * word_list.count(key_word)

            for key, value in sorted(word_dict.items(), key=lambda x: (-x[1], x[0])):
                print('{}: {}'.format(key, value))
    else:
        print(None)

