class Codec:

    def __init__(self):
        self.urls = []

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.urls.append(longUrl)
        return 'http://tinyurl.com/' + str(len(self.urls) - 1)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.urls[int(shortUrl.split('/')[-1])]



class Codec:

    def __init__(self):
        self.pool = string.ascii_letters + '0123456789'
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.url2code:
            code = ''.join(random.choice(self.pool) for _ in range(6))
            if code not in self.code2url:
                self.url2code[longUrl] = code
                self.code2url[code] = longUrl
        return 'http://tinyurl.com/' + code

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.code2url[shortUrl[-6:]]
