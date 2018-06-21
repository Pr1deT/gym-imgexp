"""
class for one blood cell

attributes:
	type: 		0 - IDK; 1 - red; 2 - white
	cell_pos: 	cell center position [x,y]
	guess_type: agent guess of cell type
	guess_pos: 	agent guess of position [x,y]
	prob_type:	probability for right guess of the cell type
	prob_pos:	probability for right guess of the cell position
	img:		image representation

"""
from PIL import Image
import numpy as np

class BloodCell(object):
	def __init__(self,cell_type,cell_pos):
		# ground truth
		self.type = cell_type
		self.cell_pos = cell_pos

		# prediction by agent
		self.guess_type = 0
		self.guess_pos = [0,0]

		# probability for right guess
		self.prob_type = 0.5
		self.prob_pos = [0,0]

		# load image
		if (cell_type == 1):
			img = Image.open('red.png')
		elif (cell_type == 2):
			img = Image.open('white.png')
		self.img = np.array(img)

	def update_prob_cell_type():
		update_flag = False
		if self.prob_type < 1.0:
			update_flag = True
			self.prob_type += 0.1
			if self.prob_type > 1.0:
				self.prob_type = 1.0

		if update_flag == True:
			update_guess_cell_type()
			return True
		else:
			return False


	def update_prob_cell_pos(pos):
		update_flag = False 
		# probability is <= 1.0
		for i in range(2):
			if self.prob_pos[i] < 1.0 and pos[i]==1:
				# update
				update_flag = True
				# increse probability by 0.1
				self.prob_pos[i] += 0.1
				if self.prob_pos[i] > 1.0:
					self.prob_pos[i] = 1.0

		# update guess position when probability is high
		if update_flag == True:
			update_guess_cell_pos()
			return True
		else:
			return False

	def update_guess_cell_type():
		if self.cell_type == 1:
			p = [self.prob_type,1.0-self.prob_type]
		else:
			p = [1.0-self.prob_type,self.prob_type]

		self.guess_type = np.random.choice([1,2],p)

	def update_guess_cell_pos(guess_pos):
		# generate guessed position based on:
		# 1: cell_pos - true position
		# 2: prob_pos - probability of knowing the true position
		return 1

"""
class of blood smear image contains several red and white blood cells
attributes:
	n_cell: 		total number of cells
	cells: 			list of BloodCell objects
	img: 			test image with several red and white blood cells
	rep_img:		replicated test image
	prob_img_size:	probability of knowing the right size of the image [width, height]


methods:
	_create_test_image

"""

class BloodSmearImage(object):
	def __init__(self,cells):
		# generate cell objects
		self.n_cell = len(cells)
		# debug
		#print 'number of cells: ', cell_num

		# initiate attribute cells: a list of cells
		self.cells = []
		for i in range(self.n_cell):
			cell_type, cell_x, cell_y = cells[i]
			one_cell = BloodCell(cell_type,[cell_x, cell_y])
			self.cells.append(one_cell)

		# build test image
		# initiate image
		self.img = np.zeros(shape=(260,399,4),dtype=np.uint8)
		self._create_test_image()

		# initialize knowlege of the image
		self.prob_img_size = [0.0,0.0]

		# initialize replicated image
		self.rep_img = 0

	# ------------- create image related functions -----------------
	"""
		create test image based on:
		1. number of cells
		2. cell positions
	"""
	def _create_test_image(self):
		
		for i in range(self.n_cell):
			# add the cell to the test image
			self._add_one_obj(self.cells[i])

		# debug
		#img = Image.fromarray(self.img)
		#img.save('out.png')

	"""
		cell: BloodCell object
	"""
	def _add_one_obj(self,cell):

		# get cell image size
		[height, width, _]  = cell.img.shape 
		# debug
		#print "cell image size: ", width, " , ", height	
		
		# build a same size img with 0 background
		img_to_add = np.zeros(shape=self.img.shape,dtype=np.uint8)
		
		# get cell center position
		pos = cell.cell_pos
		# ger left upper corner and lower right corner position
		x_low = pos[0] - width/2
		y_low = pos[1] - height/2
		x_high = pos[0] + width/2
		y_high = pos[1] + height/2

		# debug
		#print "upper corner: ", x_low, ", ", y_low
		#print "lower corner: ", x_high, ", ", y_high

		for x in range(x_low, x_high-1):
			for y in range(y_low, y_high-1):
				img_to_add[y,x,:] = cell.img[y-y_low,x-x_low,:]

		# debug
		#img = Image.fromarray(img_to_add)
		#img.save('out.png')

		# add to img
		self.img += img_to_add

	# --------------------------------------------------------------
	def update_prob_image(side):
		self.prob_img_size += side * 0.5
		for i in range(2):
			if self.prob_img_size[i]>1.0:
				self.prob_img_size = 1.0 

	def update_replicate_image(cell):
		# remove the pixels of this cell

		# update the cell type

		# put new piexels of this cell

		return 1



if __name__ == '__main__':
	cells_list = []
	blood_smear_img = BloodSmearImage(cells_list)


