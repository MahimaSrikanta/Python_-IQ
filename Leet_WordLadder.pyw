'''
Question: Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that only one letter can be changed at a time and each intermediate word must exist in the dictionary. For example, given:

    start = "hit"
    end = "cog"
    dict = ["hot","dot","dog","lot","log"]
    One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", the program should return its length 5.


Solution: Using BFS and set, to determine the tree and bactracking to construct the tree from bottom up method

'''


import collections
class Ladder:

    def wordLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)
        trace = collections.OrderedDict()
        result, current, visited, found,trace = [], [start], set([start]), False, {word: [] for word in dict} 
        while current and not found:
            for word in current:
                visited.add(word)
                
            next = set()
            check=set()
            
            for words in dict:
                for i in range (3):
                    check.add(words[i])
                    check.add(word[i])
                if len(check) ==4:
                    if words not in visited:
                        if words == end:
                            found= True
                            
                        next.add(words)
                        trace[words].append(word)
                        check.clear()
                else:
                    check.clear()
                        
            current = next
                
        if found:
            self.backtrack(result, trace, [], end)
            
        return result
            
    def backtrack(self, result, trace, path, word):
        if not trace[word]:
            result.append([word] + path)
        else:
            for prev in trace[word]:
                self.backtrack(result, trace, [word] + path, prev)

                
           
if __name__ == "__main__":
    print (Ladder().wordLadders("hit", "cog", set(["hot","dot","dog","lot","log"])))
