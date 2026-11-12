# personal selection without Proverbs: nine whole books cut into key phrases, with the name "yahweh" replaced by "god".
import json
src=open('phrase_build.py').read();exec(src[:src.index('# 1 Claude selection')])
BOOKS.pop('proverbs')
sel=[]
for bk in BOOKS:
    d=json.load(open(J+bk+'.json',encoding='utf-8'))
    for ch in sorted({x['chapterNumber'] for x in d if 'chapterNumber' in x}): sel.append((bk,BOOKS[bk],ch,1,999))
pack(from_json(sel),'ph_personal.json')
