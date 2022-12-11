caves="""TR-start
xx-JT
xx-TR
hc-dd
ab-JT
hc-end
dd-JT
ab-dd
TR-ab
vh-xx
hc-JT
TR-vh
xx-start
hc-ME
vh-dd
JT-bm
end-ab
dd-xx
end-TR
hc-TR
start-vh"""


class Cave():
	def __init__(self,n):
		self.name=n
		self.neigbors = []
		self.isbig= (n==n.upper())
		self.isend= (n=="end")
		self.isstart= (n=="start")
		#self.visitcounter = 0
		
	def add(self,n):
		self.neigbors.append(n)
		
		
	def visit(self,listing,ident):
		#we are the end of the line, this route is valid
		if self.isend:
			#print("--->",end='')
			#self.lpr(listing)
			return 1
			
		if self.isstart and len(listing)>0:
			return 0
			
		#we are small, and have been visited in this route before, not a valid route
		if not self.isbig:
			if self in listing:
				if ident < 2:
					ident += 1
				else:
					return 0
				
		#still not finished, visit all neighbours:
		g = 0
		newlist = []
		newlist.extend(listing)
		newlist.append(self)
		for n in self.neigbors:
			g+=n.visit(newlist,ident)
		return g
		
	def lpr(self,l):
		for i in l:
			print(i,end=',')
		print(self.name)	
		
	def __repr__(self):
		return str(self.name)
		
cavelist={}
for line in caves.splitlines():
	start,end = line.split("-")
	if start not in cavelist:
		cavelist[start]=Cave(start)
	if end not in cavelist:
		cavelist[end]=Cave(end)

for line in caves.splitlines():
	start,end = line.split("-")
	cavelist[start].add(cavelist[end])
	cavelist[end].add(cavelist[start])

print(cavelist["start"].visit([],1))
	
