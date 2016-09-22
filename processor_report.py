import os
import csv
import datetime
import glob
import openpyxl

class ProcessorReportGenerator():

    def main(self,args=None):
            pass

    processors = ('provider pay', 'inmar', 'reconrx')

    # run sql and output to a csv
    def call835Proc(self):
        dsn = 'SSRXDEVIQ1'
        now = datetime.datetime.now()
        date = now.strftime('%Y-%m-%d')
        for processor_name in self.processors:
            output_file = 'processor_835_extract_' + date + '_' + processor_name + '.csv'
            output_file = output_file.replace(" ", "")
            sql = """call ssrx.ssrx_835_report('""" + processor_name + """'); output to """ + output_file + """ quote '' delimited by '|';"""
            cmd = '. ~sybiq/IQ/IQ.sh; dbisql -c dsn=' + dsn + ' -nogui "' + sql + '"'
            os.system(cmd)

        for file in glob.glob("*.csv"):
            wb = openpyxl.Workbook()
            ws = wb.active
            f = open(file)
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                ws.append(row)
            f.close()
            file = file.replace(".csv", ".xlsx")
            wb.save(file)
        os.system('rm *.csv*')


def main(args=None):
        processor = ProcessorReportGenerator()
        processor.call835Proc()

if __name__ == '__main__': main()
