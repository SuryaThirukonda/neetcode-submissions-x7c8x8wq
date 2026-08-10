class PrefixTree:

    def __init__(self):
        self.children = {}
        self.word = False

    def insert(self, word: str) -> None:
        temp = self

        i=0
        for c in word:
            if c not in temp.children:
                temp.children[c] = PrefixTree()
            temp = temp.children[c]
            if i == len(word)-1:
                temp.word = True
            i+=1


    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.word
        if word[0] in self.children:
            return self.children[word[0]].search(word[1:])
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            #doesnt check whether its a word, so just return true
            return True
        if prefix[0] in self.children:
            return self.children[prefix[0]].startsWith(prefix[1:])
        else:
            return False
        