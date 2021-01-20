import collections

class Solution:
    # graph BFS
    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        wordList_visited = [False] * len(wordList)
        queue = collections.deque([])
        queue.append((beginWord, 1))
        while queue:
            cur_word, cur_lvl = queue.popleft()
            for i in range(len(wordList)):
                if not wordList_visited[i] and self.wordDist_1(cur_word, wordList[i]):
                    if wordList[i] == endWord:
                        return cur_lvl+1
                    wordList_visited[i] = True
                    queue.append((wordList[i], cur_lvl+1))
        return 0

    def wordDist_1(self, w1: str, w2: str) -> bool:
        if len(w1) != len(w2):
            return-1
        dist = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                dist += 1
                if dist > 1:
                    return False
        return dist == 1

    # graph BFS with quicker 1 letter change comparsion
    def ladderLength_1(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # all the words have the same length
        L = len(beginWord)

        all_combination_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                generic_pattern = word[:i] + "*" + word[i+1:]
                all_combination_dict[generic_pattern].append(word)

        # queue for BFS
        queue = collections.deque([])
        queue.append((beginWord, 1))
        visited = {beginWord: True}
        while queue:
            cur_word, cur_lvl = queue.popleft()
            for i in range(L):
                intermediate_word = cur_word[:i] + "*" + cur_word[i+1:]
                for word in all_combination_dict[intermediate_word]:
                    if word == endWord:
                        return cur_lvl+1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, cur_lvl+1))
                # since only shortest path is preferred,
                # after scanning a intermediate_word, there will not scan again.
                all_combination_dict[intermediate_word] = []
        return 0

    # 2 graph BFS: one from begin word, one from end word
    def __init__(self):
        self.wordLength = 0
        self.all_combination_dict = collections.defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        cur_word, level = queue.popleft()
        for i in range(self.wordLength):
            generic_pattern = cur_word[:i] + "*" + cur_word[i+1:]
            for word in self.all_combination_dict[generic_pattern]:
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    visited[word] = level + 1
                    queue.append((word, level+1))
        return None

    def ladderLength_2(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        self.wordLength = len(beginWord)

        # build dictionary for all combinations of 1 letter change
        # key is generic key, value is list of words from wordList
        for word in wordList:
            for i in range(self.wordLength):
                generic_pattern = word[:i] + "*" + word[i+1:]
                self.all_combination_dict[generic_pattern].append(word)

        # initialize queues
        queue_begin = collections.deque([(beginWord, 1)])
        queue_end = collections.deque([(endWord, 1)])
        # initialize dictionaries of visited word
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}

        while queue_begin and queue_end:
            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans
        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

beginWord = "cet"
endWord = "ism"
wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr",\
            "gay","sip","kay","per","val","mes","ohs","now","boa",\
            "cet","pal","bar","die","war","hay","eco","pub","lob",\
            "rue","fry","lit","rex","jan","cot","bid","ali","pay",\
            "col","gum","ger","row","won","dan","rum","fad","tut",\
            "sag","yip","sui","ark","has","zip","fez","own","ump",\
            "dis","ads","max","jaw","out","btu","ana","gap","cry",\
            "led","abe","box","ore","pig","fie","toy","fat","cal",\
            "lie","noh","sew","ono","tam","flu","mgm","ply","awe",\
            "pry","tit","tie","yet","too","tax","jim","san","pan",\
            "map","ski","ova","wed","non","wac","nut","why","bye",\
            "lye","oct","old","fin","feb","chi","sap","owl","log",\
            "tod","dot","bow","fob","for","joe","ivy","fan","age",\
            "fax","hip","jib","mel","hus","sob","ifs","tab","ara",\
            "dab","jag","jar","arm","lot","tom","sax","tex","yum",\
            "pei","wen","wry","ire","irk","far","mew","wit","doe",\
            "gas","rte","ian","pot","ask","wag","hag","amy","nag",\
            "ron","soy","gin","don","tug","fay","vic","boo","nam",\
            "ave","buy","sop","but","orb","fen","paw","his","sub",\
            "bob","yea","oft","inn","rod","yam","pew","web","hod",\
            "hun","gyp","wei","wis","rob","gad","pie","mon","dog",\
            "bib","rub","ere","dig","era","cat","fox","bee","mod",\
            "day","apr","vie","nev","jam","pam","new","aye","ani",\
            "and","ibm","yap","can","pyx","tar","kin","fog","hum",\
            "pip","cup","dye","lyx","jog","nun","par","wan","fey",\
            "bus","oak","bad","ats","set","qom","vat","eat","pus",\
            "rev","axe","ion","six","ila","lao","mom","mas","pro",\
            "few","opt","poe","art","ash","oar","cap","lop","may",\
            "shy","rid","bat","sum","rim","fee","bmw","sky","maj",\
            "hue","thy","ava","rap","den","fla","auk","cox","ibo",\
            "hey","saw","vim","sec","ltd","you","its","tat","dew",\
            "eva","tog","ram","let","see","zit","maw","nix","ate",\
            "gig","rep","owe","ind","hog","eve","sam","zoo","any",\
            "dow","cod","bed","vet","ham","sis","hex","via","fir",\
            "nod","mao","aug","mum","hoe","bah","hal","keg","hew",\
            "zed","tow","gog","ass","dem","who","bet","gos","son",\
            "ear","spy","kit","boy","due","sen","oaf","mix","hep",\
            "fur","ada","bin","nil","mia","ewe","hit","fix","sad",\
            "rib","eye","hop","haw","wax","mid","tad","ken","wad",\
            "rye","pap","bog","gut","ito","woe","our","ado","sin",\
            "mad","ray","hon","roy","dip","hen","iva","lug","asp",\
            "hui","yak","bay","poi","yep","bun","try","lad","elm",\
            "nat","wyo","gym","dug","toe","dee","wig","sly","rip",\
            "geo","cog","pas","zen","odd","nan","lay","pod","fit",\
            "hem","joy","bum","rio","yon","dec","leg","put","sue",\
            "dim","pet","yaw","nub","bit","bur","sid","sun","oil",\
            "red","doc","moe","caw","eel","dix","cub","end","gem",\
            "off","yew","hug","pop","tub","sgt","lid","pun","ton",\
            "sol","din","yup","jab","pea","bug","gag","mil","jig",\
            "hub","low","did","tin","get","gte","sox","lei","mig",\
            "fig","lon","use","ban","flo","nov","jut","bag","mir",\
            "sty","lap","two","ins","con","ant","net","tux","ode",\
            "stu","mug","cad","nap","gun","fop","tot","sow","sal",\
            "sic","ted","wot","del","imp","cob","way","ann","tan",\
            "mci","job","wet","ism","err","him","all","pad","hah",\
            "hie","aim","ike","jed","ego","mac","baa","min","com",\
            "ill","was","cab","ago","ina","big","ilk","gal","tap",\
            "duh","ola","ran","lab","top","gob","hot","ora","tia",\
            "kip","han","met","hut","she","sac","fed","goo","tee",\
            "ell","not","act","gil","rut","ala","ape","rig","cid",\
            "god","duo","lin","aid","gel","awl","lag","elf","liz",\
            "ref","aha","fib","oho","tho","her","nor","ace","adz",\
            "fun","ned","coo","win","tao","coy","van","man","pit",\
            "guy","foe","hid","mai","sup","jay","hob","mow","jot",\
            "are","pol","arc","lax","aft","alb","len","air","pug",\
            "pox","vow","got","meg","zoe","amp","ale","bud","gee",\
            "pin","dun","pat","ten","mob"]

sol = Solution()
print(sol.ladderLength_2(beginWord, endWord, wordList))