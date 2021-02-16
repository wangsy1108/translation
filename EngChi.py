##########################
#名称：EngChi.py
#作者：王思源
#版本：1.0.0
#更新记录：
#
#
#
#
#
#
#########################
from random import *
inputw=None
word_list=[]
wrong_word=[]
word_file = open('nce4.txt')
for line in word_file:
	word_list.append(line)
rest_list=word_list
while rest_list!=[]:
	word=rest_list[randint(0,len(rest_list)-1)]
	rest_list.remove(word)
	eng,chi,wtype=word.split(',',3)
	input(eng+wtype)
	inputw=input(chi)
	if inputw!=' ':
		wrong_word.append(word)
wrong_file=open('wrong','w')
wrong_file.writelines(wrong_word)
word_file.close
wrong_file.close
	
