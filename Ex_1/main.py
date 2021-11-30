import re
import nltk
import nltk.stem.porter as pt


# 获取并输出具有词根词缀的单词
def get_root(word_set):
    with open('纲举目张背单词.txt', 'r', encoding='utf-8') as f:
        rows = f.readlines()
        root_list = []
        for row in rows:
            if '_' in row:
                row = row.replace('__', '_').lower()
                row = re.sub('[^a-z_]', '', row)
                root_list.append(row)

    with open('词根.txt', 'w+') as f:
        for root in root_list:
            f.write(root + '\n')

    with open('具有词根词缀的单词.txt', 'w+') as f:
        cur_char = 'a'
        cur_index = 1
        for root in root_list:
            if root.replace('_', '')[0] != cur_char:
                cur_char = root.replace('_', '')[0]
                cur_index = 1
            temp_list = []
            for word in word_set:
                match = re.match(root.replace('_', '.*'), word)
                if match and match.group() == word:
                    temp_list.append(word)
            write_line = str(cur_index) + '\n' + root + '\n' + ' '.join(temp_list) + '\n'
            f.writelines(write_line)
            # print(write_line)
            cur_index += 1


# 获取去重后单词列表
def read_text():
    with open('3.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.lower()
        words = nltk.word_tokenize(text)
        words = [word for word in words if word.isalpha()]
        word_set = sorted(set(words))
        return word_set


# 词形相近（词干相同）
def get_similar_word(word_set):
    dit = {}
    pt_stemmer = pt.PorterStemmer()
    for word in word_set:
        key = pt_stemmer.stem(word)
        temp = dit.get(key, [])
        temp.append(word)
        dit[key] = temp
    s_list = list(dit.values())
    with open('词形相近.txt', 'w+') as f:
        for l1 in s_list:
            if len(l1) > 1:
                f.write(" ".join(l1) + "\n")


if __name__ == '__main__':
    words_set = read_text()
    get_root(words_set)
    get_similar_word(words_set)
