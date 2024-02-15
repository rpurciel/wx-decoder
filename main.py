import builtins
import json
import os
from pathlib import Path, PurePath

WX_TABLES = [
	'wx_codes.json',
	'ack.json',
	'desc_misc.json'
	]

DIR_TABLES = [
	'dirs.json'
	]

LOC_TABLES = [
	'cities_us.json'
	'states_us.json',
	'regions_na.json',
	'countries.json'
	]

class EncodedStr(builtins.str):

	def __init__(self, str):
		self.str = str

		self.wx_codes = False
		self.dir_codes = False
		self.loc_codes = False

	def decode(self, **kwargs):

		wx_decoded = self.decode_wx(self.str, kwargs)
		dirs_decoded = self.decode_dirs(wx_decoded, kwargs)
		final_decoded = self.decode_locs(dirs_decoded, kwargs)

	def decode_wx(self, use=None, **kwargs):
		if use:
			inpt_str = use
		else:
			inpt_str = self.str

		if not self.wx_codes:
			self.wx_codes = self.__load(WX_TABLES)
		
		elements = inpt_str.split(" ")
		tr_str = ""
		for el in elements:
			try:
				tr_el = self.wx_codes[el]
			except KeyError:
				tr_el = el
			tr_str += f"{tr_el} "

		return tr_str

	def decode_locs(self, use=None, **kwargs):
		if use:
			inpt_str = use
		else:
			inpt_str = self.str

		return inpt_str

	def decode_dirs(self, use=None, **kwargs):
		if use:
			inpt_str = use
		else:
			inpt_str = self.str

		if not self.dir_codes:
			self.dir_codes = self.__load(DIR_TABLES)
		
		elements = inpt_str.split(" ")
		tr_str = ""
		for el in elements:
			try:
				tr_el = self.dir_codes[el]
			except KeyError:
				tr_el = el
			tr_str += f"{tr_el} "

	def __load(self, tables):

		tables_data = []
		wd = PurePath.joinpath(Path.cwd(), 'tables')

		for table in tables:
			with open(PurePath.joinpath(wd, table)) as data:
				tables_data += [json.load(data)]

		master_data = {}
		for data in tables_data:
			master_data.update(data)

		return master_data

if __name__ == "__main__":

	text = "TC IAN CONT TO MOV SLOWLY NNEWD ALG THE EAST COAST OF THE U.S. WNDS ASSOC WITH TC IAN WILL CONT TO AFCT WRN PTNS OF MIAMI AND NY FIRS IMPROVING FM THE S THRUT THE PD. LINES OF TSRA ARE ALSO EXPD ACRS THESE AREAS IN ASSOC WITH TS IAN. LARGE AREA OF DISTURBED WEATHER ASSOC WITH AN UPRLVL LOW ACRS ERN CARIB LOCATIONS INCLUDING SAN JUAN...PIARCO AND MAIQUETIA FIRS. TROF INTO HABANA AND NERN CNTRL AMER FIR FM 22N81W TO 17N83W. LGT SHRA ASSOC WITH THIS FEATURE. HIGH PRES MOVG INTO SRN GLFMEX LOCATIONS WITH SCT CLDS EXPD TO CLEAR FM N TO S. ISOL SHRA EXPD ACRS REMAINING AREAS OF THE WRN ATLC AND CARIB."
	test = EncodedStr(text)

	print(test.decode())



