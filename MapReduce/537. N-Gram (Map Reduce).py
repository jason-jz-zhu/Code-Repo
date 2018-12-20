# 3
# doc_1: "abcabc"
# doc_2: "abcabc"
# doc_3: "bbcabc"


class NGram:

    # @param {int} n a integer
    # @param {str} string a string
    def mapper(self, _, n, string):
        # Write your code here
        # Please use 'yield key, value' here
        l = len(string)
        for i in range(l - n + 1):
            yield string[i: i + n], 1

    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value' here
        yield key, sum(values)
