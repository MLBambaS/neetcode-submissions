class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = collections.defaultdict(list)
        queue = deque()
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+'*'+word[i+1:]
                graph[pattern].append(word)
        res = 1
        queue.append(beginWord)
        visited = set()
        visited.add(beginWord)
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j]+'*'+word[j+1:]
                    for w in graph[pattern]:
                        if w not in visited:
                            visited.add(w)
                            queue.append(w)
            res+=1
        return 0