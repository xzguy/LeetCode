import collections

class Solution:
    # graph BFS, slow method
    def findLadders(self, beginWord: str, endWord: str, wordList: [str]) -> [[str]]:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return []

        word_len = len(beginWord)
        generic_pattern_dictionary = collections.defaultdict(list)
        for word in wordList:
            for i in range(word_len):
                gen_pat = word[:i] + "*" + word[i+1:]
                generic_pattern_dictionary[gen_pat].append(word)

        res = []
        queue = collections.deque([])
        queue.append((beginWord, [beginWord], 1, set()))
        shortest_path = 0
        while queue:
            cur_word, cur_wList, cur_lvl, cur_visited = queue.popleft()
            if shortest_path != 0 and cur_lvl > shortest_path:
                break
            for i in range(word_len):
                gen_pat = cur_word[:i] + "*" + cur_word[i+1:]
                for word in generic_pattern_dictionary[gen_pat]:
                    if word == endWord:
                        new_list = cur_wList.copy()
                        new_list.append(word)
                        res.append(new_list)
                        shortest_path = cur_lvl
                    elif word not in cur_visited:
                        new_visited = cur_visited.copy()
                        new_visited.add(word)
                        new_list = cur_wList.copy()
                        new_list.append(word)
                        queue.append((word, new_list, cur_lvl+1, new_visited))
        return res

    # graph BFS with direction one letter comparison, slow method
    def findLadders_1(self, beginWord: str, endWord: str, wordList: [str]) -> [[str]]:
        queue = collections.deque([])
        queue.append((beginWord, [beginWord], 1, set()))
        shortest_path = 0
        res = []
        while queue:
            cur_word, cur_list, cur_lvl, cur_visited = queue.popleft()
            if shortest_path != 0 and shortest_path < cur_lvl:
                break
            for word in wordList:
                if word not in cur_visited and self.wordDist_1(cur_word, word):
                    new_list = cur_list.copy()
                    new_list.append(word)
                    if word == endWord:
                        shortest_path = cur_lvl+1
                        res.append(new_list)
                    else:
                        new_visited = cur_visited.copy()
                        new_visited.add(word)
                        queue.append((word, new_list, cur_lvl+1, new_visited))
        return res

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

    ''''
    This method is quicker mainly because the space saving.
    The data structure used for saving path is much more concise.
    Despite the above solution is slow, it is more flexbile: it can
    deal with paths of different length.
    The above BFS loops over the queue.
    The following BFS loops over level, thus it does not need to store level information. 
    The problem of getting all shortest path, gives this solution a fit.
    The key point of the following solution is to use 
    the dictionary (word, set of word's parent) to store intermediate path.
    '''
    def findLadders_2(self, beginWord: str, endWord: str, wordList: [str]) -> [[str]]:
        wordSet = set(wordList)
        
        level = set([beginWord])
        
        parents = collections.defaultdict(set)
        
        while level and endWord not in parents:
            next_level = collections.defaultdict(set)
            for word in level:
                for i in range(len(beginWord)):
                    p1 = word[:i]
                    p2 = word[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        # accelerate 
                        if word[i] != j:
                            childWord = p1 + j + p2
                            if childWord in wordSet and childWord not in parents:
                                next_level[childWord].add(word)
            level = next_level
            parents.update(next_level)
        
        res = [[endWord]]
        while res and res[0][0] !=beginWord:
            res = [[p]+r for r in res for p in parents[r[0]]]
        
        return res

    # a modified version of above quick method with different 1 letter comparison.
    def findLadders_3(self, beginWord: str, endWord: str, wordList: [str]) -> [[str]]:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return []

        wordSet = set(wordList)

        L = len(beginWord)
        generic_pattern_dict = collections.defaultdict(set)
        for word in wordSet:
            for i in range(L):
                generic_pattern = word[:i] + "*" + word[i+1:]
                generic_pattern_dict[generic_pattern].add(word)

        level = set([beginWord])
        parents = collections.defaultdict(set)
        
        while level and endWord not in parents:
            next_level = collections.defaultdict(set)
            for word in level:
                for i in range(L):
                    generic_pattern = word[:i] + "*" + word[i+1:]
                    for childWord in generic_pattern_dict[generic_pattern]:
                        if childWord not in parents:
                            next_level[childWord].add(word)
            level = next_level
            parents.update(next_level)
        
        res = [[endWord]]
        while res and res[0][0] != beginWord:
            new_res = []
            for r in res:
                for p in parents[r[0]]:
                    new_res.append([p] + r)
            res = new_res

        # while res and res[0][0] != beginWord:
        #     res = [[p]+r for r in res for p in parents[r[0]]]
        return res

    def findLadders_4(self, beginWord: str, endWord: str, wordList: [str]) -> [[str]]:
        if endWord not in wordList:
            return []
    
        wordSet = set(wordList) # faster checks against dictionary
        layer = {}
        layer[beginWord] = [[beginWord]] # stores current word and all possible sequences how we got to it

        while layer:
            newlayer = collections.defaultdict(list) # returns [] on missing keys, just to simplify code
            for word in layer:
                if word == endWord: 
                    return layer[word] # return all found sequences
                for i in range(len(word)): # change every possible letter and check if it's in dictionary
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord =  word[:i] + c + word[i+1:]
                        if newWord in wordSet:
                            # add new word to all sequences and form new layer element
                            newlayer[newWord] += [j + [newWord] for j in layer[word]] 
            wordSet -= set(newlayer.keys()) # remove from dictionary to prevent loops
            layer = newlayer # move down to new layer

        return []

beginWord = "red"
endWord = "tax"
wordList = ["ted","tex","red","tax","tad","den","rex","pee"]


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

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log", "cog"]


sol = Solution()
print(sol.findLadders_3(beginWord, endWord, wordList))