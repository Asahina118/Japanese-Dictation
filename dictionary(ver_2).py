import random
import os
here = os.path.dirname(os.path.abspath(__file__))

select =''

while select != 'Q':
    hist = []
    li = ''
    with open(os.path.join(here, '漢字と意味.txt'), encoding='utf8') as fp:
        for i, l in enumerate(fp):
            pass
    num = i+1
    print('words contained in the file:',num)
    fp.close()
    select = input('Select(D/A/L/Q):')
    if select == 'D':
        print('enter *quit* to exit dictation') 

    while select == "D":
        if li == '':
            li = input('Display correct list throughout the dictation?(Y/N)')
        #file_choice = input('File version(1/2):')
        file_choice = ('漢字と意味.txt')
        rep = True
        while (rep):
            rep = False
            file = open(os.path.join(here, file_choice),'r',encoding='utf8')
            line = next(file)
            for num, aline in enumerate(file, 2):
                if random.randrange(num):
                    continue
                line = aline
            temp_list = line.split()
            for i in range(len(hist)):
                if temp_list[1] == hist[i]:
                    rep = True
        print(temp_list[1])
        x = input("Answer:")
        while x != temp_list[0] and x!='quit':
            print("Incorrect")
            x = input("Again:")
        if x == 'quit':
            break
        if x == temp_list[0]:
            print("Correct!")
            hist.append(temp_list[1])
            if li == 'Y':
                print('words got right:',hist)
        if len(hist) == num:
            print('all words are dictated')
            break

    while select == "A":
        word = input('hiragana:')
        if word == 'quit':
            break
        tran = input('translation:')
        if tran == 'quit':
            break
        with open(os.path.join(here, '漢字と意味.txt'),'a',encoding='utf8') as file:
            file.write('\n'+word+' '+tran)
        print('successful')

    if select == 'L':
        print('=================================')
        with open(os.path.join(here, '漢字と意味.txt'),'r',encoding='utf8') as file:
            print(file.read())
        print('=================================')
        

exit()
