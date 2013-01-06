=====
pdict
=====

pdict has a dictionary like interface and a sqlite backend.
It uses pickle to store Python objects and strings, which are then compressed with zlib for storage in sqlite.
Multithreaded interaction is supported.

Depends on python 2.5+

Example use: ::

    >>> filename = 'cache.db'
    >>> cache = pdict.PersistentDict(filename)
    >>> url = 'http://google.com/abc'
    >>> html = '<html>abc</html>'
    >>>
    >>> url in cache
    False
    >>> cache[url] = html
    >>> url in cache
    True
    >>> cache[url] == html
    True
    >>> cache.get(url)['value'] == html
    True
    >>> now = datetime.datetime.now()
    >>> cache.meta(url)
    {}
    >>> cache.meta(url, 'meta')
    >>> cache.meta(url)
    'meta'
    >>> del cache[url]
    >>> url in cache
    False
