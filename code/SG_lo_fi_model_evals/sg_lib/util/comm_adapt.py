import numpy as np
from math import trunc

class CommAdapt(object):

	def __truncate(self, number, digits):

		stepper = pow(10.0, digits)
		res     = trunc(stepper * number) / stepper

		return res

	def read_real_part(self, file_name):

		real_parts  = np.zeros(2)
		imag_parts  = np.zeros(2)
		
		with open(file_name, "r") as file:
			lines 		= file.readlines()
			
			data_line_1 	= lines[1]
			data_split_1 = data_line_1.split()
			if len(data_split_1) == 2:
				real_part_str, imag_part_str 	= data_split_1
				real_parts[0] 					= self.__truncate(float(real_part_str), 6)
				imag_parts[0] 					= self.__truncate(float(imag_part_str), 6)
			elif len(data_split_1) == 3:
				ky, real_part_str, imag_part_str 	= data_split_1
				real_parts[0] 						= self.__truncate(float(real_part_str), 6)
				imag_parts[0] 						= self.__truncate(float(imag_part_str), 6)

			data_line_2 	= lines[2]
			data_split_2 = data_line_2.split()
			if len(data_split_2) == 2:
				real_part_str, imag_part_str 	= data_split_2
				real_parts[1]					= self.__truncate(float(real_part_str), 6)
				imag_parts[1]					= self.__truncate(float(imag_part_str), 6)
			elif len(data_split_2) == 3:
				ky, real_part_str, imag_part_str 	= data_split_2
				real_parts[1] 						= self.__truncate(float(real_part_str), 6)
				imag_parts[1] 						= self.__truncate(float(imag_part_str), 6)

		file.close()

		return real_parts, imag_parts


	def read_imag_part(self, file_name):

		imag_parts  = np.zeros(2)
		
		with open(file_name, "r") as file:
			lines 		= file.readlines()
			
			data_line_1 	= lines[1]
			data_split_1 = data_line_1.split()
			if len(data_split_1) == 2:
				real_part_str, imag_part_str 	= data_split_1
				imag_parts[0] 					= self.__truncate(float(imag_part_str), 6)
			elif len(data_split_1) == 3:
				ky, real_part_str, imag_part_str 	= data_split_1
				imag_parts[0] 						= self.__truncate(float(imag_part_str), 6)

			data_line_2 	= lines[2]
			data_split_2 = data_line_2.split()
			if len(data_split_2) == 2:
				real_part_str, imag_part_str 	= data_split_2
				imag_parts[1]					= self.__truncate(float(imag_part_str), 6)
			elif len(data_split_2) == 3:
				ky, real_part_str, imag_part_str 	= data_split_2
				imag_parts[1] 						= self.__truncate(float(imag_part_str), 6)

		file.close()

		return imag_parts

	def write_sg_data(self, file_name, sg_data):

		with open(file_name, "w") as file:
			for sg_info in sg_data:
				line = ''

				sg_points 	= sg_info[0]
				sim_no 		= sg_info[1]

				for sg_point in sg_points:
					line += str(sg_point) + ' '

				line += str(sim_no) + '\n'
				
				file.write(line)

		file.close

	def write_is_terminated(self, file_name, is_not_terminated):
		
		is_not_terminated = str(is_not_terminated).lower()

		with open(file_name, "w") as file:
			file.write(is_not_terminated + '\n')

		file.close()