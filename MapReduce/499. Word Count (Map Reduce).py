# chunk1: "Google Bye GoodBye Hadopp lintcode"
# chunk2: "lintcode Google code"
# chunk3: "Bye Bye Google"


class WordCount:

    def mapper(self, _, line):
        # Write your code here
        for word in line.split():
            yield word, 1


    def reducer(self, key, values):
        # Write your code here
        yield key, sum(values)
