'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        hash = dict()
        for node in results:
            if node.id not in hash:
                hash[node.id] = []
            hash[node.id].append(node.score)
            if len(hash[node.id]) > 5:
                index = 0
                for i in xrange(1, 6):
                    if hash[node.id][i] < hash[node.id][index]:
                        index = i
                hash[node.id].pop(index)
        res = dict()
        for id, scores in hash.items():
            res[id] = sum(scores) / 5.0

        return res
