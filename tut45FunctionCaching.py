import time
from functools import lru_cache

@lru_cache(maxsize=2)

def work(n):
    time.sleep(n)
    return n
if __name__ == '__main__':
    print("On the go")
    print(work(3))
    print("Ready")
    print(work(3))
    print(work(1))
    print("finish")
    print(work(1))

# in this case it will be able to store 2 recent values as cache
# the next time if that function is called it wont take the time and the stored value will be returned


