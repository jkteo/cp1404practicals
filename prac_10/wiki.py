"""
Wikipedia test program
"""

import wikipedia

query = input("Enter your Wikipedia search: ")
while query != "":
    page_result = wikipedia.page(query)
    print(page_result.title)
    print(page_result.url)
    print(page_result.summary)
    query = ("Enter your Wikipedia search: ")
