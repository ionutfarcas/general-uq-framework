import numpy as np
from pickle import dump, load

class SerializeRefInfo(object):
	
	def serialize_ref_info(self, ref_step, local_len, total_no_grid_points, serialization_file):

		with open(serialization_file, "wb") as output_file:
			data = [ref_step, local_len, total_no_grid_points]
			dump(data, output_file)

		output_file.close()

	def unserialize_ref_info(self, serialization_file):

		with open(serialization_file, "rb") as input_file:
			ref_step, local_len, total_no_grid_points = load(input_file)

		input_file.close()

		return ref_step, local_len, total_no_grid_points

	def serialize_curr_no_sims(self, curr_no_sims, serialization_file):

		with open(serialization_file, "wb") as output_file:
			dump(curr_no_sims, output_file)

		output_file.close()

	def unserialize_curr_no_sims(self, serialization_file):

		with open(serialization_file, "rb") as input_file:
			curr_no_sims = load(input_file)

		input_file.close()

		return curr_no_sims

	def serialize_physical_mode(self, physical_mode, serialization_file):

		with open(serialization_file, "wb") as output_file:
			dump(physical_mode, output_file)

		output_file.close()

	def unserialize_physical_mode(self, serialization_file):

		with open(serialization_file, "rb") as input_file:
			physical_mode = load(input_file)

		input_file.close()

		return physical_mode