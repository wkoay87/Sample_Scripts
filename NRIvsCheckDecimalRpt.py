import pyodbc,xlsxwriter, sys, datetime as dt, time,calendar,os, argparse,adodbapi
from datetime import datetime
from datetime import timedelta
from subprocess import call

from helpers.email_helper import send_mail
from helpers import SQL_helper
from helpers.DB_helper import DB_Connection
#SQL statements

SQL = SQL_helper.NRIvsCheckDecimalRpt.SQL

    
def create_xl(server,db,user,xl_nm):
    PRD_con = DB_Connection(server,db,user)
    #workbook = xlsxwriter.Workbook(xl_nm, {'constant_memory': True})
    workbook = xlsxwriter.Workbook(xl_nm)
    #ws_num = ['002','020','040','101','102','103','104']
    ws_num = ['020']
    for ws in ws_num:
        
        sql_bsm = SQL.replace("@@BUSCD","'"+ws+"'")
        print 'Query records...'
        rows = PRD_con.sqlserver_sql(sql_bsm)
        if len(rows) > 300000:
            rows1 = rows[0:300000]
            rows2 = rows[300000:]

            worksheet = workbook.add_worksheet(ws+"1")
            print 'Adding rows...'
            for i, row in enumerate(rows1):
                    worksheet.write_row(i+2, 1, row)

            worksheet = workbook.add_worksheet(ws+"2")
            print 'Adding rows...'
            for i, row in enumerate(rows2):
                    worksheet.write_row(i+2, 1, row)
            
        else:    
        
            print 'Add ws to wb...'
            worksheet = workbook.add_worksheet(ws)
            worksheet.set_column('B:AE',10)

            tbl_len = str(len(rows)+2) #add two to include header and 0 row

            print 'Adding rows...'
            for i, row in enumerate(rows):
                    worksheet.write_row(i+2, 1, row)

            print 'Adding table...'
            worksheet.add_table('B2:AD'+tbl_len,
                                {'columns':[{'header': 'Check #'},
                                {'header': 'Remitter #'},
                                {'header': 'Remitter Sub'},
                                {'header': 'Remitter Prop #'},
                                {'header':'Remitter Payee #'},
                                {'header': 'Prop #'},
                                {'header': 'Completion Name'},
                                {'header': 'Tier'},
                                {'header': 'Well #'},
                                {'header': 'Accounting Month'},
                                {'header': 'Printed Date'},
                                {'header': 'Business Unit Code'},
                                {'header': 'Remitter Major Product Code'},
                                {'header': 'Net Amount'},
                                {'header': 'Owner Decimal'},
                                {'header': 'DOI Decimal'},
                                {'header': 'State Code'},
                                {'header': 'State Name'},
                                {'header': 'Cnty Code'},
                                {'header': 'Cnty Name'},
                                {'header': 'Reservoir Name'},
                                {'header': 'Field'},
                                {'header': 'Lat Code'},
                                {'header': 'Latitude'},
                                {'header': 'Long Code'},
                                {'header': 'Longitude'},
                                {'header': 'IHS id'},
                                {'header': 'Play Trend Code'},
                                {'header': 'Play Trend Desc'}]})
        
        rows = []
    workbook.close()
    
def extract_sql(server,db,user,elist,cclist):
    try:
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
        
        sfirst_day = "'"+syear+"/"+lastMonth.strftime("%m")+"/"+first_day+"'"
        slast_day = "'"+syear+"/"+lastMonth.strftime("%m")+"/"+str(prev_last_day)+"'"

        check_rpt = 'NRI_vs_CheckDecimal_' + datetime.now().strftime('%m_%d_%Y.xlsx')
        
        create_xl(server,db,user,check_rpt)
        print 'Sending email...'
        send_mail('AutomatedReports@blackstoneminerals.com',
                  elist,
                  cclist,
                  'NRI vs Check Decimal report generated on ' + current_date.strftime("%B") +' '+ current_date.strftime("%Y") ,
                  'The attached Excel spreadsheet contains post rollup check and DOI decimals from 04/01/2014 to the current date'+
                  '.  If you have any questions regarding this spreadsheet, please contact InformationTechnology@blackstoneminerals.com.',
                  [check_rpt])

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

    
    if len(args.s[0])>0 and len(args.db[0])>0 and len(args.u[0])>0 and len(args.e[0])>0:
        extract_sql(args.s[0],args.db[0],args.u[0],args.e,args.cc)
    else:
        raw_input('Error: Not enough values to process values.  Please re-enter server, database, user, and email information.')

except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        raw_input("Error: cript has encountered an error. Please investigate and fix the problem before rerunning the script.  Press Enter to exit...")
        sys.exit()
    
finally:
    print('Emails sent for NRI vs CHeck Decimal report')


