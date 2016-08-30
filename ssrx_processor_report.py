import os 
import csv
import datetime
from openpyxl import Workbook

class ProcessorReportGenerator():

	def main(self,args=None):
		pass

	processors = ('provider pay', 'inmar')

	# run sql and output to a csv
	def runSQL(self):
		dsn = '$LOCALIQDB' 
		now = datetime.datetime.now()
		date = now.strftime('%Y-%m-%d')
		for processor_name in self.processors:
			sql = 'call ssrx.ssrx_835_report(' + processor_name + ')'
			output_file = 'processor_835_extract_' + date + '_' + processor_name + '.csv'
			os.system('dbisql -c ' + dsn + ' -nogui "' + sql + '" output to ' + output_file + 'quote '' delimited by '','';')
		os.system('echo SQL has succesfully run')

	# convert csv file to .xls
	# def fileConversionXLS():

def main(args=None):
	processor = ProcessorReportGenerator()
	processor.runSQL()

if __name__ == '__main__': main()