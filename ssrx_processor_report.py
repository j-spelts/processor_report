import os 
import csv
from openpyxl import Workbook

class processorReportGenerator():

	SQL= 'select '\
	'    processor  PROCESSOR'\
	'    , id_type  PAYMEMT_LEVEL'\
	'    , payment_id  PAYMENT_LEVEL_CODE'\
	'    , provider  PAYMENT_DESCRIPTION;'\
	'from ssrx.eob_835'\
	'where processor like ''ReconRx%'''\
	';'\
	''

	DSN= 'SSRXDEVIQ1'

	# run sql and output to a csv
	def runSQL(SQL):

		os.system('dbisql -c ' + DSN + ' -nogui "' + SQL + '" output to ~ quote '' delimited by '','';')
		os.system('echo SQL has succesfully run')

	# convert csv file to .xls
	def fileConversionXLS():
		