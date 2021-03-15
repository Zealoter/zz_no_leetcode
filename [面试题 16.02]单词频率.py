class WordsFrequency:

    def __init__(self, book: List[str]):
        self.tmp_dic=dict()
        for s in book:
            if s in self.tmp_dic:
                self.tmp_dic[s]+=1
            else:
                self.tmp_dic[s]=1


    def get(self, word: str) -> int:
        if word in self.tmp_dic:
            return self.tmp_dic[word]
        return 0