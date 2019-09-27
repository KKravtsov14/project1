# задача программы - перевести текст в русский, если текст написан с русским смыслом на английской раскладке

# каждой английской букве и некоторым символам соответствует русская буква или знак препинания, нужно задать эти элементы, знаковые элементы заменим на условные обозначения

f = 'а'
el1 = 'б'
d = 'в'
u = 'г'
l = 'д'
t = 'е'
el2 = 'ё'
el3 = 'ж'
p = 'з'
b = 'и'
q = 'й'
r = 'к'
k = 'л'
v = 'м'
y = 'н'
j = 'о'
g = 'п'
h = 'р'
c = 'с'
n = 'т'
e = 'у'
a = 'ф'
el4 = 'х'
x = 'ч'
w = 'ц'
el9 = 'ш'
o = 'щ'
el5 = 'ъ'
s = 'ы'
m = 'ь'
el6 = 'э'
el7 = 'ю'
z = 'я'
el8 = ' '
zp1 = '.'
zp2 = ','
zp3 = '-'
zp4 = '!'
zp5 = '?'
zp6 = ';'
zp7 = ':'
zp8 = '"'

# цикл выявляет какая буква должны была быть напечатана и добавляет ее к новой строке

siz = (input())
kol = len(siz)
i = 0
sv = ''
while i < kol:
    ind = siz[i]
    if ind == ' ':
        sv+=el8
    elif ind == 'j':
        sv+=j
    elif ind == 't':
        sv+=t
    elif ind == 'f':
        sv+=f
    elif ind == 'b':
        sv+=b
    elif ind == 'y':
        sv+=y
    elif ind == 'n':
        sv+=n
    elif ind == 'c':
        sv+=c
    elif ind == 'h':
        sv+=h
    elif ind == 'd':
        sv+=d
    elif ind == 'k':
        sv+=k
    elif ind == 'r':
        sv+=r
    elif ind == 'v':
        sv+=v
    elif ind == 'l':
        sv+=l
    elif ind == 'g':
        sv+=g
    elif ind == 'e':
        sv+=e
    elif ind == 'z':
        sv+=z
    elif ind == 's':
        sv+=s
    elif ind == 'm':
        sv+=m
    elif ind == 'u':
        sv+=u
    elif ind == 'p':
        sv+=p
    elif ind == ',':
        sv+=el1
    elif ind == 'x':
        sv+=x
    elif ind == 'q':
        sv+=q
    elif ind == '[':
        sv+=el4
    elif ind == ';':
        sv+=el3
    elif ind == 'i':
        sv+=el9
    elif ind == '.':
        sv+=el7
    elif ind == 'w':
        sv+=w
    elif ind == 'o':
        sv+=o
    elif ind == """'""":
        sv+=el6
    elif ind == 'a':
        sv+=a
    elif ind == ']':
        sv+=el5
    elif ind == """`""":
        sv+=el2
    elif ind == '/':
        sv+=zp1
    elif ind == '?':
        sv+=zp2
    elif ind == '-':
        sv+=zp3
    elif ind == '!':
        sv+=zp4
    elif ind == '&':
        sv+=zp5
    elif ind == '$':
        sv+=zp6
    elif ind == '^':
        sv+=zp7
    elif ind == '@':
        sv+=zp8
    i = i+1

print (sv)

