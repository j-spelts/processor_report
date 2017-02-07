import csv
import datetime
import glob
import openpyxl
import os
import sqlanydb

class ProcessorReportGenerator:

    def main(self,args=None):
            pass

    processors = ('provider pay', 'inmar', 'reconrx', 'apns', 'nhin', 'scriptpro')

    # run sql and output to a csv
    def call835Proc(self):
        # run sql and output to a csv
        conn = sqlanydb.connect( DSN="SSRXDEVIQ1" )
        curs = conn.cursor()

        now = datetime.datetime.now()
        date = now.strftime('%Y-%m-%d')
        for processor_name in self.processors:
            output_file = 'processor_835_extract_' + date + '_' + processor_name + '.csv'
            output_file = output_file.replace(" ", "")
            sql = """call ssrx.ssrx_835_report('""" + processor_name + """');"""
            curs.execute(sql)

            with open(output_file,'w', newline = '') as result:
                rowset = curs.fetchall()
                for row in rowset:
                    wtr= csv.writer( result, delimiter = '|' )
                    wtr.writerow((row[0], row[1], row[2], row[3]))

        curs.close()
        conn.close()

        # convert csv to Excel spreadhseet
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
        # os.rename('')


def main(args=None):
        processor = ProcessorReportGenerator()
        processor.call835Proc()

if __name__ == '__main__': main()