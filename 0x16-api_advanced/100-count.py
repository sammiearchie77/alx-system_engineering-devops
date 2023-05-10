#!/usr/bin/python3
"""
Module for count_words function
"""
import requests


def count_words(subreddit, word_list, new_after='',
                words_dict={}):
    """
    A recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints a
    sorted count of given keywords
    """

    word_list = map(lambda x: x.lower(), word_list)
    word_list = list(word_list)

    res = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit),
                       headers={'User-Agent': 'Custom'},
                       params={'after': new_after},
                       allow_redirects=False)

    if res.status_code != 200:
        return

    try:
        response = res.json().get('data', None)

        if response is None:
            return
    except ValueError:
        return

    children = response.get('children', [])

    for post in children:
        title = post.get('data', {}).get('title', '')
        for key_word in word_list:
            for word in title.lower().split():
                if key_word == word:
                    words_dict[key_word] = words_dict.get(key_word, 0) + 1

    new_after = response.get('after', None)

    if new_after is None:
        sorted_dict = sorted(words_dict.items(),
                             key=lambda x: x[1],
                             reverse=True)

        for i in sorted_dict:
            if i[1] != 0:
                print("{}: {}".format(i[0], i[1]))
        return

    return count_words(subreddit, word_list,
                       new_after, words_dict)
