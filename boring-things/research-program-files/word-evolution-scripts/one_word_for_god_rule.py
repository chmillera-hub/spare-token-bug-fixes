# Personal rule set by Charles for the selections he chose: the name "yahweh" is replaced by the word "god"
# in a key phrase file so that the selection uses one word for God. Usage: python3 one_word_for_god_rule.py ph_charles.json
import json,sys
M={'yahweh':'god','yahwehs':'gods'}
for f in sys.argv[1:]:
    D=json.load(open(f));uid={};u=[];new=[]
    for x in D['u']:
        y=' '.join(M.get(w,w) for w in x.split())
        if y not in uid: uid[y]=len(u);u.append(y)
        new.append(uid[y])
    D['u']=u;D['seq']=[new[k] for k in D['seq']];json.dump(D,open(f,'w'))
