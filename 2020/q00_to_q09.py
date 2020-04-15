import random

######
## 00.
q = 'stressed'

a = q[::-1]
print(a) # desserts
######
## 01.
q = 'パタトクカシーー'

a = q[1::2]
print(a) # タクシー
######
## 02.
q0 = 'パトカー'
q1 = 'タクシー'

a = ''.join([i+j for i, j in zip(q0, q1)])
print(a) # パタトクカシーー
######
## 03.
q = 'Now I need a drink, alcoholic of course, \
after the heavy lectures involving quantum mechanics.'

a = [len(i) for i in q.replace(',', '').replace('.', '').split()]
print(a) # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
######
## 04.
q = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. \
New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

{qw[:1] if idx in (1, 5, 6, 7, 8, 9, 15, 16, 19) else qw[:2] \
 : idx for idx, qw in enumerate(q.replace(',', '').replace('.', '').split(), 1)}

'''
{'Al': 13,
 'Ar': 18,
 'B': 5,
 'Be': 4,
 'C': 6,
 'Ca': 20,
 'Cl': 17,
 'F': 9,
 'H': 1,
 'He': 2,
 'K': 19,
 'Li': 3,
 'Mi': 12,
 'N': 7,
 'Na': 11,
 'Ne': 10,
 'O': 8,
 'P': 15,
 'S': 16,
 'Si': 14}
'''
######
## 05.
def get_n_gram(text, n):
    return [text[i:i+2] for i in range(len(text)-2+1)]

q = 'I am an NLPer'

print(get_n_gram(q, 2)) # ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
print(get_n_gram(q.split(), 2)) # [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
######
## 06.
X = set(get_n_gram('paraparaparadise', 2))
Y = set(get_n_gram('paragraph', 2))

print(X) # {'pa', 'ad', 'di', 'ra', 'se', 'ar', 'ap', 'is'}
print(Y) # {'pa', 'ag', 'gr', 'ra', 'ar', 'ph', 'ap'}

print(X | Y) # {'pa', 'ad', 'ag', 'di', 'gr', 'ra', 'se', 'ar', 'ph', 'ap', 'is'}
print(X & Y) # {'pa', 'ar', 'ra', 'ap'}
print(X - Y) # {'di', 'se', 'ad', 'is'}

print('se' in X) # True
print('se' in Y) # False
######
## 07.
def generate_sentence(x, y, z):
    return f'{x}時の{y}は{z}'

print(generate_sentence(12, '気温', 22.4)) # '12時の気温は22.4'
######
## 08.
def cipher(sentence):
    return ''.join([chr(219-ord(s)) if s.islower() else s for s in sentence])

q = "The dataset is provided by Google's Natural Questions"

print(cipher(q)) # Tsv wzgzhvg rh kilerwvw yb Glltov'h Nzgfizo Qfvhgrlmh
print(cipher(cipher(q))) # The dataset is provided by Google's Natural Questions
######
## 09.
q = 'I couldn’t believe that I could actually understand \
what I was reading : the phenomenal power of the human mind .'

a = ' '.join([w[0]+''.join(random.sample(w[1:-1], len(w[1:-1])))+w[-1] if len(w) > 4 else w for w in q.replace(',', '').replace('.', '').split()])
print(a) # I cld’uont blvieee that I colud alltcauy utsardnned what I was rainedg : the phonemenal pwoer of the hmaun mind
######

