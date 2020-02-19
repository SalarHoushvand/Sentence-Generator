from nltk.util import ngrams
from nltk.tokenize import RegexpTokenizer

# load data from a file
filename = 'brown.txt'
file = open(filename, 'rt')
s = file.read()

# make the text lowercase and replace new line tags with space
s = s.lower()
s = s.replace('\n',' ')
file.close()

# remove punctuations
tokenizer = RegexpTokenizer(r'\w+')
result = tokenizer.tokenize(s)


# make text with no punctuations
listToStr = ' '.join(map(str, result))
tokens = [token for token in listToStr.split(" ") if token != ""]

# make bigrams out of text
output_bigram = list(ngrams(tokens, 2))

# ask user to enter text and make a bigram
s1=input('please type two words : ')
li_input = s1.split(' ')


output = []


# define punctuation list without dot
punctuations = '''!()-[]{};:'"\,<>/?@#$%^&*_~'''

#define punctuation list with dot
punctuations_dot = '''!()-[]{};:'"\,<>/?@#$%^&*_~'''

no_punct = ""


# remove punctuations with dot
for char in s:
   if char not in punctuations_dot:
       no_punct = no_punct + char

# split sentences with dot as stop point
sentences_list = no_punct.split('.')

# make a list for last words of each sentences

tokens = []
last_bigrams = []
lastWords = []

# make bigrams out of last words
for i in range(0,len(sentences_list)):
    tokens.append([token for token in sentences_list[i].split(" ") if token != ""])


for i in range(0,len(tokens)):
    if len(tokens[i]) >= 2:
         last_bigrams.append(tokens[i][-2])
         last_bigrams.append(tokens[i][-1])
         lastWords.append(last_bigrams)
         last_bigrams=[]

# compare user input to all bigrams and make sentences
UserInput = tuple(li_input)
li2 = []
for i in range(0,len(output_bigram)):
    if UserInput == output_bigram[i]:
            while list(output_bigram[i]) not in lastWords:
                 li2.append(output_bigram[i+1][1])
                 i = i +1
            li2 = li_input + li2
            print(' '.join(li2) + '.')
            li2 = []
