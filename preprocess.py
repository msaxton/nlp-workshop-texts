import re

fn = 'augustine_cog_1-13.txt'
with open(fn, encoding='utf8', mode='r') as f:
    raw = f.read()

# remove footnote numbers i.e. [1]
pattern = r'\[(\d+)\]'
text = re.sub(pattern, '', raw)

# remove \n
pattern = r'\n'
text = re.sub(pattern, ' ', text)

# remove punctuation
pattern = r'[^\w\s]'
text = re.sub(pattern, '', text)

# split text into books
pattern = r'Book \d+'
cog_books = re.split(pattern, text)

del cog_books[0]

fns = ['aug_cog_1', 'aug_cog_2', 'aug_cog_3', 'aug_cog_4', 'aug_cog_5',
'aug_cog_6', 'aug_cog_7', 'aug_cog_8', 'aug_cog_9', 'aug_cog_10',
'aug_cog_11','aug_cog_12', 'aug_cog_13',]

for fn, cog_book in zip(fns, cog_books):
    with open('augustine_cog\\' + fn + '.txt', encoding='utf8', mode='w') as f:
        f.write(cog_book)
