class Solution:
    """
    @param inputA: Input stream A
    @param inputB: Input stream B
    @return: The answer
    """
    def inputStream(self, inputA, inputB):
        # Write your code here
        s1 = []
        s2 = []
        for c in inputA:
            if c == '<':
                if s1 != []:
                    s1.pop()
            else:
                s1.append(c)

        for c in inputB:
            if c == '<':
                if s2 != []:
                    s2.pop()
            else:
                s2.append(c)

        if s1 == s2:
            return 'YES'
        return 'NO'
