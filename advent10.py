digits = """7777838353
2217272478
3355318645
2242618113
7182468666
5441641111
4773862364
5717125521
7542127721
4576678341""" 

class Octopus():
	def __init__(self,level):
		self.level=level
		self.flashing = False
		self.neighbours=[]
		self.flashctr=0
		
	def step(self,reset=False):
		if not self.flashing:
			self.level += 1
			if self.level > 9:
				self.flashctr+=1
				self.flashing = True
				self.level = 0;
				for i in self.neighbours:
					i.step()

	def add(self,n):
		self.neighbours.append(n)
	def reset(self):
		self.flashing = False
	def ret(self):
		return self.flashctr
	def val(self):
		return self.level
	def __repr__(self):
		if self.flashing:
			return "F" #"\033[1m0\033[0m" #"F"
		else:
			return str(self.level)
			
	
hmap = []
for line in digits.splitlines():
    height = list(line)
    l = map(int,height)
    l = [Octopus(x) for x in list(l)]
    hmap.append(list(l))

x = len(hmap[0])
y = len(hmap)
print(f"Grid({x}x{y})")

for i in range(y):
	for j in range(x):
		if i > 0 and j > 0:
			hmap[i][j].add(hmap[i-1][j-1])
		if i > 0:
			hmap[i][j].add(hmap[i-1][j])
		if i > 0 and j < x-1:
			hmap[i][j].add(hmap[i-1][j+1])


		if j > 0:
			hmap[i][j].add(hmap[i][j-1])
		if j < x-1:
			hmap[i][j].add(hmap[i][j+1])
			
			
		if i < y-1 and j >0:
			hmap[i][j].add(hmap[i+1][j-1])
		if i < y-1:
			hmap[i][j].add(hmap[i+1][j])		
		if i < y-1 and j < x-1:
			hmap[i][j].add(hmap[i+1][j+1])



	
s=0
for line in hmap:
		for x in line:
			s+=x.ret()
#print(c,s)
	
from PIL import Image, ImageDraw

images = []

width = 100
center = width // 2
color_1 = (0, 0, 0)
color_2 = (255, 255, 255)
max_radius = int(center * 1.5)
step = 8



loop = True
c=0
while loop:
	im = Image.new('RGB', (width, width), color_1)
	draw = ImageDraw.Draw(im)
	images.append(im)

	loop = False
	c+=1
	for line in hmap:
		for x in line:
			x.step()
	for i in range(10):
		for j in range(10):
			x=hmap[i][j]
			draw.ellipse((j*10, i*10, j*10 + 10, i*10 + 10), fill=(x.val()*25,0,0,255))

			if str(x)!="F":
				loop = True
			else:
				draw.ellipse((j*10+2, i*10+2, j*10 + 6, i*10 + 6), fill=(0,255,0,255))

			print(x, end = ' ')
			
		print("")
	for line in hmap:
		for x in line:
			x.reset()
	print("\n---------------\n")
	
images[0].save('./pillow_imagedraw.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)
