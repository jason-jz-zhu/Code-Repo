class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        import collections
        if paths is None or len(paths) == 0:
            return []
        hashmap = collections.defaultdict(list)
        for path in paths:
            tmp = path.split(' ')
            for i in range(1, len(tmp)):
                start, end = tmp[i].find('('), tmp[i].find(')')
                file_name = tmp[0] + '/' + tmp[i][: start]
                file_content = tmp[i][start + 1: end]
                hashmap[file_content].append(file_name)

        res = []
        for val in hashmap.values():
            if len(val) > 1:
                res.append(val)
        return res


Follow up questions:

1. Imagine you are given a real file system, how will you search files? DFS or BFS ?
In general, BFS will use more memory then DFS. However BFS can take advantage of the locality of files in inside directories, and therefore will probably be faster

2. If the file content is very large (GB level), how will you modify your solution?
In a real life solution we will not hash the entire file content, since it's not practical. Instead we will first map all the files according to size. Files with different sizes are guaranteed to be different. We will than hash a small part of the files with equal sizes (using MD5 for example). Only if the md5 is the same, we will compare the files byte by byte

3. If you can only read the file by 1kb each time, how will you modify your solution?
This won't change the solution. We can create the hash from the 1kb chunks, and then read the entire file if a full byte by byte comparison is required.

What is the time complexity of your modified solution? What is the most time consuming part and memory consuming part of it? How to optimize?
Time complexity is O(n^2 * k) since in worse case we might need to compare every file to all others. k is the file size

How to make sure the duplicated files you find are not false positive?
We will use several filters to compare: File size, Hash and byte by byte comparisons.
