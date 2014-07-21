# -*- coding: UTF-8 -*-
	
	
#这是一个格式化输出内容的函数
def printindex(*content):
    sing=inred("+")
    sing1=ingreen("-")
    sing2=ingreen("|")
    sentence=[]
    maxsent=0
    for i in xrange(len(content)):
        sentence.append(content[i])
        if maxsent <=len(content[i]):
            maxsent=len(content[i])
    screen_width=70
    text_width=maxsent
    box_width=text_width+6
    left_margin=(screen_width-box_width)//2
    print "Welcome to our system:"
    print ' ' * left_margin + sing + sing1 *(box_width-4) + sing
    print ' ' * left_margin + sing2 + ' ' *(text_width+1) +' ' + sing2
    for i in xrange(len(content)):
        print ' ' * left_margin + sing2 + ' ' + sentence[i]  + ' '*(maxsent-len(sentence[i])+1)  + sing2
   # print ' ' * left_margin + sing2 + ' ' + sentence1 + ' '*(maxsent-len(sentence1)+1) + sing2
    #print ' ' * left_margin + sing2 + ' ' + sentence2 + ' '*(maxsent-len(sentence2)+1) + sing2
    print ' ' * left_margin + sing2 + ' ' *(text_width+1) + " "    + sing2
    print ' ' * left_margin + sing + sing1 *(box_width-4)  + sing