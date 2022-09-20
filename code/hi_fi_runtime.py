import numpy as np
from matplotlib.pyplot import *

    
if __name__ == '__main__':

	dim 		= 8
	CPU_count 	= 896

	runtimes = [31335.413, 28674.621, 33461.511, 32384.355, 24585.751, 45932.856, 31241.044, 30851.113, 30704.991, \
		 		22806.507, 39843.840, 36114.160, 38811.821, 17151.326, 29220.285, 58162.841, 29416.229, 24352.944, \
		 		45925.425, 31399.631, 21184.897, 33557.586, 23184.809, 39041.995, 28328.124, 20733.520, 30561.471, \
		 		30538.169, 26369.213, 52326.384, 35227.736, 23623.536, 39569.497, 36972.533, 32105.918, 42027.132, \
		 		22687.837, 36644.119, 32944.933, 49934.406, 16860.141, 55689.136, 16941.540, 29474.893, 25665.566, \
		 		52391.600, 23330.119, 49858.804, 46171.919, 18403.305, 28939.167, 33569.043, 25158.100, 45827.350, \
		 		31398.046, 30452.882, 21735.813]

	print(len(runtimes))

	print(CPU_count * np.sum(np.array(runtimes[:56]))/3600)

	print('**********')
	print('Minimum runtime: {} [hours]'.format(np.min(runtimes)/3600))
	print('Minimum runtime: {} [CPU hours]'.format(CPU_count * np.min(runtimes)/3600))
	print('**********')
	print('**********')
	print('Maximum runtime: {} [hours]'.format(np.max(runtimes)/3600))
	print('Maximum runtime: {} [CPU hours]'.format(CPU_count * np.max(runtimes)/3600))
	print('**********')
	print('**********')
	print('Average runtime: {} [hours]'.format(np.mean(runtimes)/3600))
	print('Average runtime: {} [CPU hours]'.format(CPU_count * np.mean(runtimes)/3600))
	print('**********')