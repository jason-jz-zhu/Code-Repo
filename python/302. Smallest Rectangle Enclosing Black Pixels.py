class Solution(object):
    # @param image {List[List[str]]}  a binary matrix with '0' and '1'
    # @param x, y {int} the location of one of the black pixels
    # @return an integer
    def minArea(self, image, x, y):
        # Write your code here
        if image is None:
            return 0
        top, bottom, left, right = 0, 0, 0, 0
        # search the top one
        start, end = 0, x
        while start + 1 < end:
            mid = start + (end - start) / 2
            if '1' in image[mid]:
                end = mid
            else:
                start = mid
        top = start if '1' in image[start] else end
        # search the bottom one
        start, end = x, len(image) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if '1' in image[mid]:
                start = mid
            else:
                end = mid
        bottom = end if '1' in image[end] else start
        # search the left one
        start, end = 0, y
        while start + 1 < end:
            mid = start + (end - start) / 2
            if any(image[i][mid] == '1' for i in xrange(len(image))):
                end = mid
            else:
                start = mid
        left = start if any(image[i][start] == '1' for i in xrange(len(image))) else end
        # search the right one
        start, end = y, len(image[0]) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if any(image[i][mid] == '1' for i in xrange(len(image))):
                start = mid
            else:
                end = mid
        right = end if any(image[i][end] == '1' for i in xrange(len(image))) else start

        return (right - left + 1) * (bottom - top + 1)
