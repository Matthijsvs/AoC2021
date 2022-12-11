
t="FSKBVOSKPCPPHVOPVFPC"
inp="""BV -> O
OS -> P
KP -> P
VK -> S
FS -> C
OK -> P
KC -> S
HV -> F
HC -> K
PF -> N
NK -> F
SC -> V
CO -> K
PO -> F
FB -> P
CN -> K
KF -> N
NH -> S
SF -> P
HP -> P
NP -> F
OV -> O
OP -> P
HH -> C
FP -> P
CS -> O
SK -> O
NS -> F
SN -> S
SP -> H
BH -> B
NO -> O
CB -> N
FO -> N
NC -> C
VF -> N
CK -> C
PC -> H
BP -> B
NF -> O
BB -> C
VN -> K
OH -> K
CH -> F
VB -> N
HO -> P
FH -> K
PK -> H
CC -> B
VH -> B
BF -> N
KS -> V
PV -> B
CP -> N
PB -> S
VP -> V
BO -> B
HS -> H
BS -> F
ON -> B
HB -> K
KH -> B
PP -> H
BN -> C
BC -> F
KV -> K
VO -> P
SO -> V
OF -> O
BK -> S
PH -> V
SV -> F
CV -> H
OB -> N
SS -> H
VV -> B
OO -> V
CF -> H
KB -> F
NV -> B
FV -> V
HK -> P
VS -> P
FF -> P
HN -> N
FN -> F
OC -> K
SH -> V
KO -> C
HF -> B
PN -> N
SB -> F
VC -> B
FK -> S
KK -> N
FC -> F
NN -> P
NB -> V
PS -> S
KN -> S"""
t2="NNCB"
inp2="""CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

repl={}
counts={}
for item in inp.splitlines():
    find,insert = item.split(" -> ")
    repl[find]=insert
    counts[insert]=0

for letter in t:
	counts[letter]+=1
print(counts)
pairs={}

for k in range(len(t)-1):
    l= t[k:k+2]	
    if l in pairs:
        pairs[l]+=1
    else:
        pairs[l]=1    
    
print(pairs)

for i in range(40):
	newpairs={}
	for item in pairs:
		if item in repl:

			f1=item[0]+repl[item]
			if f1 in pairs:
				s = pairs[f1]
			if f1 in newpairs:
				newpairs[f1]+=pairs[item]
			else:
				newpairs[f1]=pairs[item]
			f2=repl[item]+item[-1]
			if f2 in pairs:
				s = pairs[f2]
			if f2 in newpairs:
				newpairs[f2]+=pairs[item]
			else:
				newpairs[f2]=pairs[item]

			counts[repl[item]]+=pairs[item]
		else:
			raise IOError
	#print(newpairs)
	pairs=newpairs

mi=9999999999999999999999999999999
ma=0
for c in sorted(list(counts)):
	mi=min(mi,counts[c])
	ma=max(ma,counts[c])
	print(f"{c} {counts[c]}")
	
	
print(mi,ma,ma-mi)	


