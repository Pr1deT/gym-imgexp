"""
Bayesian inference

FF  CF SS RP AP
   \| /
    \/
    |\
   /| \
  / |  \
 cell   cell
 type  location(4)

"""
class BayesProb():
	def __init__(self):
		self.num_cause = 5
		self.num_effect = 5
		self.model = np.zeros(shape=(self.num_effect,self.num_cause))
		# build model structure
		self.model[0][1:3] = [0.5,0.5]
		self.model[1][0] = 0.3
		self.model[1][3:5] = []


def 