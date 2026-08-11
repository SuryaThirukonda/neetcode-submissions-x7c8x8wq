class WordDictionary:

    def __init__(self):
        self.children = {}
        self.word = False

    def addWord(self, word: str) -> None:
        temp = self

        i=0
        for c in word:
            if c not in temp.children:
                temp.children[c] = WordDictionary()
            temp = temp.children[c]
            if i == len(word)-1:
                temp.word = True
            i+=1

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.word
        if word[0] in self.children:
            return self.children[word[0]].search(word[1:])
        elif word[0]==".":
            for child in self.children.values():
                if child.search(word[1:]):
                    return True
            return False
        else:
            return False
