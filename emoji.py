# -*- coding: UTF-8 -*-

import emoji
import operator

from emoji import UNICODE_EMOJI

#Funções
def extract_emojis(str):
	s = ''.join(c for c in str if c in emoji.UNICODE_EMOJI)
	return (count_emoji(s))
	#return ''.join(c for c in str if c in emoji.UNICODE_EMOJI)

def has_emoji(s):
	count = 0
	for emoji in UNICODE_EMOJI:
		count += s.count(emoji)
	if count == 0:
		return False
	else:
		return (extract_emojis(s))

def count_emoji(s):
	list_emojis = {}
	for emoji in s:
		if emoji != "🏿" and emoji != "🏾" and emoji != "🏽" and emoji != "🏼" and emoji != "🏻":
			if emoji not in list_emojis:
				list_emojis[emoji] = 1
			else:
				list_emojis[emoji] += 1
	return (dict(list_emojis))

def merge_dicts(x, y):
	return { k: x.get(k, 0) + y.get(k, 0) for k in set(x) | set(y) }

def merge_dicts_words(x, y):
	k = {}
	if bool(x):
		for keyX,valueX in x.items():
			k[keyX] = valueX

		for keyY,valueY in y.items():
			if  keyY not in x:
				k[keyY] = valueY
			else:
				k[keyY] += valueY
	elif bool(y):
		for keyY,valueY in y.items():
			k[keyY] = valueY
	return dict(k)
	
def order_dict(x):
	sorted_x = sorted(x.items(), key=operator.itemgetter(1), reverse=True)
	return(sorted_x)

def words_next_emoji(line, all_emojis):

	count = 0
	word_lines = line.split()
	all_emojis_words = {}
	emoji_words = dict(all_emojis)
	useful_words = []
	for key, value in all_emojis.items():
		emoji_words[key] = []

	for w in word_lines:
		if word_lines.index(w) < 6: #exclui informação desnecessaria
			i = word_lines.index(w)
			word_lines[i] = ""
		else:						
			for emoji in UNICODE_EMOJI: #encontra o emoji
				count += w.count(emoji)
			if count != 0:              #é emoji 
				#cria lista de emojis com suas palavras e fica aguardando mais palavras
								
				for e in w:           #caso tenha mais de um emoji na string, 'e' é um emoji
					if e != "🏿" and e != "🏾" and e != "🏽" and e != "🏼" and e != "🏻":
						i = word_lines.index(w)
						before = i - 1
						after = i + 1
						if before > 0 and word_lines[before] != "":
							useful_words.append(word_lines[before])
						if after < len(word_lines):
							useful_words.append(word_lines[after])
						
						emoji_words[e] = useful_words
						all_emojis_words.update(emoji_words)
						useful_words = []

	return (dict(all_emojis_words))

# --------------------------------------------------------

#Lê arquivo com os dados da conversa
f = open("/home/deboramoura/chat_text.txt", "r")

#Junta os emojis de cada linha em um dicionário maior - all_emojis
all_emojis = {}
words_emojis = {}
for r in range(1,42203):
#for r in range(0,200):
	line = f.readline()
	if (has_emoji(line)):
		all_emojis = merge_dicts(all_emojis, has_emoji(line))
		result = words_next_emoji(line, all_emojis)
		words_emojis = merge_dicts_words(words_emojis, result)
f.close()
# --------------------------------------------------------

#Cria um arquivo de resultados
file = open("result.txt","w") 
#Lista os resultados no arquivo
file.write("Resultado da quantidade de Emojis\n") 
all_emojis_list = order_dict(all_emojis)
for t in all_emojis_list:
	file.write(str(t))
	file.write(" : ")
	encoded_emoji = t[0].encode('unicode_escape')
	file.write(str(encoded_emoji))	
	file.write("\n")

file.close()
# --------------------------------------------------------

#Cria um arquivo de resultados
file2 = open("result2.txt","w") 
#Lista os resultados no arquivo
file2.write("Resultado da das Palavras ao redor de emojis\n") 
for key, value in words_emojis.items():
	file2.write(str(key))
	file2.write(" : ")
	file2.write(str(value))
	file2.write("\n")

file2.close()
