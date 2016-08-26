import os 
# import csv
# from openpyxl import Workbook

class ProcessorReportGenerator():

	def main(self,args=None):
		pass

	PROCESSORS = ('provider pay', 'inmar')

	DSN = 'SSRXDEVIQ1'

	# run sql and output to a csv
	def runSQL(self):

		for processor in self.PROCESSORS:
			SQL = 'call ssrx.ssrx_835_report(' + processor + ')'
			os.system('dbisql -c ' + DSN + ' -nogui "' + SQL + '" output to ~ quote '' delimited by '','';')

			print ('run sql for ' + processor)

		# os.system('echo SQL has succesfully run')

	# convert csv file to .xls
	# def fileConversionXLS():

def main(args=None):
	processor = ProcessorReportGenerator()
	processor.runSQL()


if __name__ == '__main__': main()