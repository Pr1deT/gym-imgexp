
"""
Simulate a image exploration and replication environment.

Each episode is explore and replicate one image.
"""

import gym
from gym import error, spaces, utils
from gym.utils import seeding
from blood_cell import BloodSmearImage


class ImgexpEnv(gym.Env):
	"""
	Define a simple Banana environment.
	The environment defines which actions can be taken at which point and
	when the agent receives which reward.
	"""

	metadata = {'render.modes': ['human']}

	def __init__(self):
		self.__version__ = "0.0.1"

		# when task ends
		self.TOTAL_TIME_STEPS = 200

		self.curr_step = -1
		self.is_task_done = False

		# generate test image
		self.test_img = create_test_image()
		[row, col, _] = self.test_img.shape

		# Define actions - what the agent can do
		# start position: [x,y] / (col, row)
		# ep CF flag: if this action would be contour following (0/1) 
		# moving direction: 0 to 359/ [0,1] cw, ccw

		self.action_space = spaces.Tuple(
			spaces.Tuple(spaces.Discrete(col), spaces.Discrete(row)),
			spaces.Discrete(2),
			spaces.Discrete(360),
			# end position: [-1,-1]/ [x,y] on boundary
			#spaces.Tuple(spaces.Discrete(col), spaces.Discrete(row)),
			)
		
		# Define state
		# current position: [x,y]
		# replicated image
		self.state = spaces.Tuple(
			spaces.Tuple(spaces.Discrete(col), spaces.Discrete(row)),
			np.zeros(shape=self.test_img.shape,dtype=uint8)
			)

		# Observation


		# Store what the agent tried
		self.curr_episode = -1
		self.action_episode_memory = []


	def step(self, action):
		"""
		The agent takes a step in the environment.
		Parameters
		----------
		action : int
		Returns
		-------
		ob, reward, episode_over, info : tuple
			ob (object) :
				an environment-specific object representing your observation of
				the environment.
			reward (float) :
				amount of reward achieved by the previous action. The scale
				varies between environments, but the goal is always to increase
				your total reward.
			episode_over (bool) :
				whether it's time to reset the environment again. Most (but not
				all) tasks are divided up into well-defined episodes, and done
				being True indicates the episode has terminated. (For example,
				perhaps the pole tipped too far, or you lost your last life.)
			info (dict) :
				 diagnostic information useful for debugging. It can sometimes
				 be useful for learning (for example, it might contain the raw
				 probabilities behind the environment's last state change).
				 However, official evaluations of your agent are not allowed to
				 use this for learning.
		"""
		if self.is_task_done:
			raise RuntimeError("Episode is done")

		self.curr_step += 1
		self._take_action(action) # 06/20
		reward = self._get_reward()
		ob = self._get_state()
		return ob, reward, self.is_task_done, {}

	def _take_action(self, action):
		self.action_episode_memory[self.curr_episode].append(action)

		# determine the end position
		
		# determine the performed exploration procedure
		ep, cell_st, cell_ed = self._determine_ep()

		# is NOT ep Contour Following
		if action[1] == 0:
			# find end position with force feedback
			self.end_pos = self._get_end_pos()
			
			# frame following
			if ep == 1:
				# get side of boundary -- INCOMPLETE
				side = get_side_of_image()
				img.update_prob_image(side)
			# surface swiping
			elif ep == 3:
				# get cell object
				cell = img.cells[cell_st]
				# update its knowledge
				if cell.update_prob_cell_type() == True and cell.guess_pos != [0,0] :
					img.update_replicate_image(cell)
			# relative positioning
			#elif ep == 4:
			
			# absolute positioning	
			elif ep == 5:
				# get cell object
				cell = img.cells[cell_st]
				# get dierction

				# update its knowlege
				if cell.update_prob_cell_pos(pos) == True:
					img.update_replicate_image(cell)
		# if Contour Following
		else:
			# get cell object
			cell = img.cells[cell_st]
			# update its knowledge
			if cell.update_prob_cell_type() == True and cell.guess_pos != [0,0] :
				img.update_replicate_image(cell)
		
		# update current position



		# update observation
		if action[1:2] == self.cell_type:
			task_is_done = True 

		if task_is_done:
			self.is_task_done = True

		remaining_steps = self.TOTAL_TIME_STEPS - self.curr_step
		time_is_over = (remaining_steps <= 0)
		
		if time_is_over:
			self.is_task_done = True  # abuse this a bit
			self.awards = 0.0

	def _get_state(self):
		"""Get the pixel value"""
		ob = self.test_img[self.y][self.x]
		return ob

	def _get_reward(self):
		reward = 0.0

		"""give reward on visits to boundaries"""
		if is_boundary(self.x, self.y):
			reward += 1.0 

		"""give reward with towards center motion"""
		return reward

  	def update_replicate_image(rep_img,action,obj1,obj2):
		# 
		if (action==1 or action==2):
			return 1


  	#def reset(self):
		#...
  	#def render(self, mode='human', close=False):
		#...

def create_test_image():
	num_red = 1
	num_white = 1
	pos_red = [70,70]
	pos_white = [205,150]
	# cells format: cell type, position
	cells = []
	for i in range(num_red):
		cells.append([1,pos_red[0],pos_red[1]])
	for i in range(num_white):
		cells. append([2,pos_white[0],pos_white[1]])
	print cells
	blood_smear_img = BloodSmearImage(cells)

if __name__ == '__main__':

	#load test image
	create_test_image()

	#env = ImgexpEnv()





