# Second Claude selection: passages picked by the AI model from books outside the ten books Charles picked
# and outside the four gospels, cut into key phrases, with the name "yahweh" replaced by "god".
import json,sys
src=open('phrase_build.py').read();exec(src[:src.index('# 1 Claude selection')])
SEL=[('genesis','Genesis',1,1,31),('genesis','Genesis',11,1,9),('exodus','Exodus',20,1,17),('deuteronomy','Deuteronomy',6,4,9),('ruth','Ruth',1,16,17),
('1samuel','First Samuel',16,7,7),('1kings','First Kings',3,5,14),('1kings','First Kings',19,11,13),('job','Job',28,1,28),('job','Job',38,1,18),
('songofsolomon','Song of Solomon',8,6,7),('lamentations','Lamentations',3,19,26),('ezekiel','Ezekiel',37,1,14),('amos','Amos',5,21,24),('micah','Micah',4,1,5),('micah','Micah',6,6,8),
('habakkuk','Habakkuk',3,17,19),('acts','Acts',2,42,47),('acts','Acts',17,22,31),('1corinthians','First Corinthians',12,12,27),('1corinthians','First Corinthians',13,1,13),
('2corinthians','Second Corinthians',4,7,18),('galatians','Galatians',5,22,26),('ephesians','Ephesians',4,1,6),('ephesians','Ephesians',4,25,32),('philippians','Philippians',2,1,11),('philippians','Philippians',4,4,9),
('colossians','Colossians',3,12,17),('hebrews','Hebrews',11,1,3),('james','James',1,19,27),('james','James',2,14,17),('james','James',3,13,18),('1peter','First Peter',4,8,11),('1john','First John',4,7,21),('revelation','Revelation',21,1,7)]
secs=from_json(SEL)
for n,t in secs:
    if len(t.split())<8: print('SHORT/EMPTY',n,len(t.split()))
pack(secs,'ph_mine.json')
print(sum(len(t.split()) for n,t in secs),'words',len(SEL),'passages')
