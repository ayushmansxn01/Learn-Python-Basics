def searcher():
    import time
    book="this is my boook on developement and Modi"
    time.sleep(2)

    while True:
        text=(yield)
        if text in book:
            print("text is in book")
        else:
            print("text is not in book")

search=searcher()
print("search started")
next(search)
print("next method rum")
search.send("harry")

search.close()
