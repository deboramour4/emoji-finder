# -*- coding: UTF-8 -*-

import emoji
import operator

from emoji import UNICODE_EMOJI

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

def order_dict(x):
	sorted_x = sorted(x.items(), key=operator.itemgetter(1), reverse=True)
	return(sorted_x)

# --------------------------------------------------------

#Lê arquivo com os dados da conversa
f = open("/home/deboramoura/chat_text.txt", "r")

#Junta os emojis de cada linha em um dicionário maior - all_emojis
all_emojis = {}
for r in range(1,42203):
#for r in range(1,100):
	line = f.readline()
	if (has_emoji(line)):
		all_emojis = merge_dicts(all_emojis, has_emoji(line))

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

#file.write("--------------------------------------------\n")
#for t in all_emojis_list:
#	encoded_emoji = t[0].encode('unicode_escape')
#	file.write(str(encoded_emoji))	
#	file.write(" : ")
#	file.write(str(t[1]))
#	file.write("\n")

f.close()