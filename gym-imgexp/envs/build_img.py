"""
Build blood smear image using white blood cell and red blood cell
"""
from PIL import Image
import numpy as np

# load white blood cell
white = Image.open('white.png')
white = np.array(white)
red = Image.open('red.png')
red = np.array(red)

def get_dimension(type):
	if type=='white':
		#print white.shape
		print white
		return white.shape
	elif type=='red':
		#print red.shape
		return red.shape

def add_one_obj(img, type, loc):
	"""
	img: img to be updated
	type: red/white to add on
	loc: upper left coordinates
	"""
	# get cell
	if type=='white':
		obj = white
	elif type=='red':
		obj = red

	[width, height, _]  = get_dimension(type) 	
	
	# build a same size img with 0 background
	img_to_add = np.zeros(shape=img.shape,dtype=np.uint8)
	
	for x in range(loc[0],loc[0]+width):
		for y in range(loc[1],loc[1]+height):
			img_to_add[y,x,:] = obj[y-loc[1],x-loc[0],:]

	# add to img
	img += img_to_add

	return img

def build_img():
	img = np.zeros(shape=(260,399,4),dtype=np.uint8)
	# random image
	n_white = 1
	n_red = 2
	white_loc = [[20,100]]
	red_loc = [[50,200],[60,100]]

	for i in range(n_white):
		img = add_one_obj(img, 'white', white_loc[i])

	for i in range(n_red):
		img = add_one_obj(img, 'red', red_loc[i])


if __name__ == '__main__':
	img = build_img()
	img = Image.fromarray(img, 'RGB')
	img.show()




