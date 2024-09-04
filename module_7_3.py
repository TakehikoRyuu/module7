import re
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.dictionary = []

    def get_all_words(self):
        all_words = {}
        dictionary = []
        for files in self.file_names:
            with open(files, 'a+', encoding='utf-8') as file:
                file.seek(0)
                for line in file:
                    line = re.sub(r'[^\w\s\']', '', line.lower()).replace('\n', '')
                    dictionary += line.split()
            all_words[files] = dictionary
        self.dictionary = dictionary
        return all_words

    def find(self, words_resurch): # return = n (слово по счёту в списке)
        words_resurch = words_resurch.lower()
        n = 1
        for words in self.dictionary:
            if words == words_resurch:
                return n
            else:
                n+=1

    def count(self, words_resurch):
        words_resurch = words_resurch.lower()
        n = 0
        for words in self.dictionary:
            if words == words_resurch:
                n+=1
        return n


finder2 = WordsFinder('test.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
