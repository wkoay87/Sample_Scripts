import pyodbc,xlsxwriter, sys, datetime as dt, time,calendar,os, argparse,adodbapi
from datetime import datetime
from datetime import timedelta
from subprocess import call

from helpers.email_helper import send_mail
from helpers import SQL_helper
from helpers.DB_helper import DB_Connection
#SQL statements

SQL = SQL_helper.QRARemitterRpt.CHK_REMITTER_SQL

PIVOT_SQL = SQL_helper.QRARemitterRpt.CHK_REMITTER_PIVOT_SQL

EXCEPTION_SQL = SQL_helper.QRARemitterRpt.CHK_REMITTER_EXCEPTION_SQL

def create_xl(server,db,user,xl_nm,directory):
    try:
        dates = []
        alist = {1:'F' , 2:'G', 3:'H', 4:'I', 5:'J',6:'K',7:'L',8:'M',9:'N',10:'O',11:'P',12:'Q'}
        #for testing
        #os.chdir(r"\\shares\Corporate\IT\APPLICATIONS\QUORUM\ISSUES TRACKING\QLS\SIRs\05072014_QRAChecks")
        os.chdir(r""+directory)
                 
        #for current month
        syear = time.strftime("%Y")
        smonth = time.strftime("%m")
        first_day = '01' #default to first day of the month
        last_day = calendar.monthrange(int(syear),int(smonth))[1]
        
        #if need to get data from last month use this instead
        current_date = dt.date.today()
        first = dt.date(day=1, month=current_date.month, year=current_date.year)
        lastMonth = first - dt.timedelta(days=1)
        prev_last_day = calendar.monthrange(int(syear),int(smonth)-1)[1]
        
        #sfirst_day = "'"+syear+"/"+lastMonth.strftime("%m")+"/"+first_day+"'"
        slast_day = "'"+lastMonth.strftime("%m")+"/"+str(prev_last_day)+"/"+syear+"'"
        DATE_RANGE = "'01/01/"+str(current_date.year)+"' and "+ slast_day
        sql = SQL.replace("@@DATE_RANGE",DATE_RANGE)

        #Connect to database
        db_con = DB_Connection(server,db,user)
        rows = db_con.sqlserver_sql(sql)
        
        '''cnxn = adodbapi.connect('Provider=SQLOLEDB.1;Integrated Security=SSPI;Persist Security Info=True;Initial Catalog='+db+';Data Source='+\
                                server+';Use Procedure for Prepare=1;Auto Translate=True;Packet Size=4096;User Id = '+user,timeout=300)

        print ('Querying data...')
        cursor = cnxn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()'''
        tbl_len = str(len(rows)+2)
        
        workbook = xlsxwriter.Workbook(xl_nm)
        format1 = workbook.add_format()
        format1.set_num_format('0000000000')
        
        worksheet = workbook.add_worksheet('Remitter Report')
        worksheet.set_column('B:D',18)
        worksheet.set_column('E:F',40)
        worksheet.set_column('G:G',20)
        
        print ('Writing data to WS1...')
        '''for i in range(len(columns)):
            worksheet.write_string(1,i+1,columns[i],format1)'''

        for i, row in enumerate(rows):
            worksheet.write_row(i+2, 1, row)
            
        worksheet.add_table('B2:G'+tbl_len,
                            {'columns':[{'header': 'Accounting Month'},
                            {'header': 'Acquisition'},
                            {'header': 'Remitter Number'},
                            {'header': 'BA name line 1'},
                            {'header': 'BA name line 2'},
                            {'header': 'Transaction Amount'}]})

        #worksheet.add_table('B2:G2',{'header_row':False})
        
        for row in rows:
            if row[0] not in dates:
                dates.append(row[0])
                
        print dates
        
	#Pivot values
        date_list = "],[".join(dates)
        date_list = "["+date_list+"]"

        null_list = ""
        
        for nulldate in dates:
            null_list += "ISNULL(["+nulldate+"],0) AS " + "[" + nulldate + "],"

        #remove last comma
        null_list = null_list[0:len(null_list)-1]
        
        #null_list = "],0.00),ISNULL([".join(dates)
        #null_list = "ISNULL(["+null_list+"],0.00)"
        
        psql = PIVOT_SQL.replace("@@DATE_RANGE", DATE_RANGE)
        psql = psql.replace("@@MONTHS",date_list)
        psql = psql.replace("@@MNULL",null_list)
        psql += " ORDER BY 1,2"

        print psql
        
        '''cursor.execute(psql)
        pivot_rows = cursor.fetchall()'''
        pivot_rows = db_con.sqlserver_sql(psql)
        tbl_len2 = str(len(pivot_rows)+2)
        worksheet2 = workbook.add_worksheet('Remitter Pivot Report')
        worksheet2.set_column('B:B',30)
        worksheet2.set_column('C:D',40)
        worksheet2.set_column('E:E',15)
        worksheet2.set_column('F:R',12)        
            
        print ('Writing data to WS2...')
        '''for i in range(len(columns2)):
            worksheet2.write_string(1,i+1,columns2[i])'''

        for i, row in enumerate(pivot_rows):
            worksheet2.write_row(i+2, 1, row)
        
        worksheet2.add_table('B2:'+alist[len(dates)]+tbl_len2,
                             {'columns':[{'header': 'Acquisition'},
                            {'header': 'BA name line 1'},
                            {'header': 'BA name line 2'},
                            {'header': 'Remitter Number'},
                            {'header': '[01/01/2014]'},
                            {'header': '[02/01/2014]'},
                            {'header': '[03/01/2014]'},
                            {'header': '[04/01/2014]'},
                            {'header': '[05/01/2014]'},
                            {'header': '[06/01/2014]'},
                            {'header': '[07/01/2014]'},
                            {'header': '[08/01/2014]'},
                            {'header': '[09/01/2014]'},
                            {'header': '[10/01/2014]'},
                            {'header': '[11/01/2014]'},
                            {'header': '[12/01/2014]'}]})
        
        '''worksheet2.add_table('B2:Q15000',
                            {'columns':[{'header': 'Accounting Month'},
                            {'header': 'Acquisition'},
                            {'header': 'BA name line 1'},
                            {'header': 'BA name line 2'},
                            {'header': 'Remitter Number'},
                            date_header]})'''
        #EXCEPTION TAB
        z_list = "]=0 OR [".join(dates)
        z_list = "["+z_list+"] = 0"
            
        esql = EXCEPTION_SQL.replace("@@DATE_RANGE", DATE_RANGE)
        esql = esql.replace("@@MONTHS",date_list)
        esql = esql.replace("@@MNULL",null_list)
        esql = esql.replace("@@ZMON",z_list)
        
        '''cursor.execute(esql)
        ex_rows = cursor.fetchall()'''

        ex_rows = db_con.sqlserver_sql(esql)
        tbl_len3 = str(len(ex_rows)+2)
        worksheet3 = workbook.add_worksheet('Remitter Exception Report')
        worksheet3.set_column('B:B',30)
        worksheet3.set_column('C:D',40)
        worksheet3.set_column('E:E',15)
        worksheet3.set_column('F:R',12)
        
        print ('Writing data to WS3...')
        '''for i in range(len(columns2)):
            worksheet3.write_string(1,i+1,columns2[i])'''

        worksheet3.add_table('B2:'+alist[len(dates)]+tbl_len3,
                             {'columns':[{'header': 'Acquisition'},
                            {'header': 'BA name line 1'},
                            {'header': 'BA name line 2'},
                            {'header': 'Remitter Number'},
                            {'header': '[01/01/2014]'},
                            {'header': '[02/01/2014]'},
                            {'header': '[03/01/2014]'},
                            {'header': '[04/01/2014]'},
                            {'header': '[05/01/2014]'},
                            {'header': '[06/01/2014]'},
                            {'header': '[07/01/2014]'},
                            {'header': '[08/01/2014]'},
                            {'header': '[09/01/2014]'},
                            {'header': '[10/01/2014]'},
                            {'header': '[11/01/2014]'},
                            {'header': '[12/01/2014]'}]})

        for i, row in enumerate(ex_rows):
            worksheet3.write_row(i+2, 1, row)
            
        workbook.close()
        #cnxn.close()
        
    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        raw_input("Script has encountered an error. Please investigate and fix the problem before rerunning the script.  Press Enter to exit...")
        sys.exit()
        
def extract_sql(server,db,user,elist,cclist,directory):
    try:
        Remitter_nm_dt = 'RemitterCheck_' + datetime.now().strftime('%m_%d_%Y.xlsx')

        print ('Creating Excel file')
        create_xl(server,db,user,Remitter_nm_dt,directory)
        
        send_mail('RemitterCheckReport@blackstoneminerals.com',
                  elist,cclist,
                  'Remitter Exception Report for ' +  time.strftime("%Y"),
                  'The attached Excel spreadsheet contains the summed transaction amounts by acquisition, BA, and remitter number for '+time.strftime("%Y") + 
                  '.  If you have any questions regarding this spreadsheet, please contact InformationTechnology@blackstoneminerals.com.',
                  [Remitter_nm_dt])

    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        raw_input("Script has encountered an error. Please investigate and fix the problem before rerunning the script.  Press Enter to exit...")
        sys.exit()
    

try:
    parser = argparse.ArgumentParser(description = 'Builds emails to send list of newly added wells for the previous month.')
    parser.add_argument("-s", required=True, help="Server hosting QRA", type = str, nargs = 1)
    parser.add_argument("-db",required=True, help="QRA database name", type = str, nargs = 1)
    parser.add_argument("-u",required=True, help="QRA database user", type = str, nargs = 1)
    parser.add_argument("-e",required=True, help="List of recipient emails", type = str, nargs = '+')
    parser.add_argument("-cc", help="List of email recipients",type =str, nargs = '+') 
    args = parser.parse_args()

    directory = os.getcwd()
    
    if len(args.s[0])>0 and len(args.db[0])>0 and len(args.u[0])>0 and len(args.e[0])>0:
        extract_sql(args.s[0],args.db[0],args.u[0],args.e,args.cc,directory)
    else:
        raw_input('Error: Not enough values to process values.  Please re-enter server, database, user, and email information.')

except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        raw_input("Error: cript has encountered an error. Please investigate and fix the problem before rerunning the script.  Press Enter to exit...")
        sys.exit()
    
finally:
    print('Done...')


