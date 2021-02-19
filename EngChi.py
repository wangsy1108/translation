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
INPUTW=None
WORD_LIST=[]
WRONG_WORD=[]
WORD_FILE=open('nce4.txt')
for LINE in WORD_FILE:
	WORD_LIST.append(line)
REST_LIST=WORD_LIST
while REST_LIST!=[]:
	WORD=REST_LIST[randint(0,len(REST_LIST)-1)]
	REST_LIST.remove(WORD)
	ENG,CHI,WTYPE=WORD.split(',',3)
	input(ENG+WTYPE)
	INPUTW=input(CHI)
	if INPUTW!=' ':
		WRONG_WORD.append(WORD)
WRONG_FILE=open('wrong','w')
WRONG_FILE.writelines(WRONG_WORD)
WORD_FILE.close
WRONG_FILE.close
	
