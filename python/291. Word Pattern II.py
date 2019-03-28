class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:

        return self.dfs(pattern, 0, s, 0, {}, set())

    def dfs(self, pattern, p_index, s, s_index, p_hashmap, s_used):
        if len(pattern) == p_index and len(s) == s_index:
            return True
        if len(pattern) == p_index or len(s) == s_index:
            return False

        char = pattern[p_index]

        if char in p_hashmap:


            word = p_hashmap[char]
            if not s.startswith(word, s_index):
                return False
            return self.dfs(pattern, p_index + 1, s, s_index + len(word), p_hashmap, s_used)

        for i in range(s_index, len(s)):
            sub_str = s[s_index: i + 1]
            if sub_str in s_used:
                continue

            s_used.add(sub_str)
            p_hashmap[char] = sub_str
            if self.dfs(pattern, p_index + 1, s, i + 1, p_hashmap, s_used):
                return True
            del p_hashmap[char]
            s_used.remove(sub_str)


        return False
