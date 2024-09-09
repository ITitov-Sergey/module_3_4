def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        o_w_i = other_words[i]
        if root_word.lower() in o_w_i.lower() or o_w_i.lower() in root_word.lower():
            same_words.append(other_words[i])
    print(same_words)


single_root_words("weRt", "qWerty", "wErt", "erty", "qwer", "wer", "Er")
