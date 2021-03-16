import re


fn = 'augustine_cog_1-13.txt'
with open(fn, encoding='utf8', mode='r') as f:
    cog_1 = f.read()

fn = 'augustine_cog_14-22.txt'
with open(fn, encoding='utf8', mode='r') as f:
    cog_2 = f.read()

complete_text = cog_1 + '\n' + cog_2

# remove footnote numbers i.e. [1]
pattern = r'\[(\d+)\]'
complete_text = re.sub(pattern, '', complete_text)

# remove \n
pattern = r'\n'
complete_text = re.sub(pattern, ' ', complete_text)

# split text into books
pattern = r'Book \d+'
cog_books = re.split(pattern, complete_text)

del cog_books[0]

fns = ['aug_cog_1', 'aug_cog_2', 'aug_cog_3', 'aug_cog_4', 'aug_cog_5',
'aug_cog_6', 'aug_cog_7', 'aug_cog_8', 'aug_cog_9', 'aug_cog_10',
'aug_cog_11','aug_cog_12', 'aug_cog_13', 'aug_cog_14', 'aug_cog_15',
'aug_cog_16', 'aug_cog_17', 'aug_cog_18', 'aug_cog_19', 'aug_cog_20',
'aug_cog_21', 'aug_cog_22']

for fn, cog_book in zip(fns, cog_books):
    with open('augustine_cog\\' + fn + '.txt', encoding='utf8', mode='w') as f:
        f.write(cog_book)
