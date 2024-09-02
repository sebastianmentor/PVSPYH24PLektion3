sentence = input('Skriv en mening: ')
sentence_list = sentence.split(' ')
# print(len(sentence))

print(sentence.count(' ') + 1)
print(len(sentence_list))
print(sentence_list.reverse())
print(sentence_list)
print(' '.join(sentence_list))

sentence_reversed = list(sentence)
sentence_reversed.reverse()
print(''.join(sentence_reversed))

