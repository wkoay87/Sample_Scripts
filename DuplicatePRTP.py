import pyodbc,xlsxwriter, sys, datetime as dt, time,calendar,os, argparse,cx_Oracle
from datetime import datetime
from datetime import timedelta
from subprocess import call

from helpers.email_helper import send_mail
from helpers import SQL_helper
from helpers.DB_helper import DB_Connection
    
def create_xl(sql_rows,ws_num,xl_nm):
    assert type(sql_rows)==list
    
    workbook = xlsxwriter.Workbook(xl_nm)
    print len(sql_rows)
    if ws_num ==2:
        for x in range(0,len(sql_rows)):

            rows = sql_rows[x][0]
            tbl_len = str(len(rows)+2)
        
            if len(rows)>0:
                print 'Adding worksheet'
                worksheet = workbook.add_worksheet(sql_rows[x][1])
                for i, row in enumerate(rows):
                    worksheet.write_row(i+2, 1, row)
            
            if (x==1 and len(rows)>0):
                worksheet.add_table('B2:E'+tbl_len,
                            {'columns':[{'header': 'Agmt #'},
                            {'header': 'Subs #'},
                            {'header': 'Agmt Type'},
                            {'header': 'Subject'}]})
                worksheet.set_column('B:E',25)
            elif len(rows)>0:
                worksheet.add_table('B2:D'+tbl_len,
                            {'columns':[{'header': 'Agmt #'},
                            {'header': 'Agmt Type'},
                            {'header': 'Subject'}]})
                worksheet.set_column('B:E',25)

    workbook.close()
    
def extract_sql(dbpw,db,dbuser,elist,cclist):
    try:
        db_con = DB_Connection(db,dbuser,dbpw)
        prtp_xl = 'DuplicatedPRTP_'+datetime.now().strftime('%m_%d_%Y.xlsx')
        # check records before sending notification
        AGM_rows = db_con.ora_sql(SQL_helper.DuplicatePrtp.AGM_SQL)
        ARE_rows = db_con.ora_sql(SQL_helper.DuplicatePrtp.ARE_SQL)

        ws_values = []

        ws_num=0
        
        if len(AGM_rows)>0:
            run_proc = True
        else:
            AGM_rows = [['N/A','N/A','N/A']]

        if len(ARE_rows)>0:
            run_proc = True
        else:
            ARE_rows = [['N/A','N/A','N/A','N/A']]            

        if run_proc:
            create_xl([[AGM_rows,'AGM-DuplicatePrtp'],[ARE_rows,'ARE-DuplicatePRTP']],2,'DuplicatedPRTP_'+datetime.now().strftime('%m_%d_%Y.xlsx'))
            
            send_mail('DataIntegrityCheck@blackstoneminerals.com',
                      elist,
                      cclist,
                      'Duplicate Participation for '+datetime.now().strftime("%B")+", "+ datetime.now().strftime("%Y"),
                      'The attached Excel spreadsheet contains duplicated participation at the AGM and ARE levels.  If you have any questions regarding this spreadsheet, please contact InformationTechnology@blackstoneminerals.com.',
                      [prtp_xl])

    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        raw_input("Script has encountered an error. Please investigate and fix the problem before rerunning the script.  Press Enter to exit...")
        sys.exit()
    

try:
    parser = argparse.ArgumentParser(description = 'Builds emails to send list of newly added wells for the previous month.')
    parser.add_argument("-pw", required=True, help="QLS pws", type = str, nargs = 1)
    parser.add_argument("-db",required=True, help="QLS database name", type = str, nargs = 1)
    parser.add_argument("-u",required=True, help="QLS database user", type = str, nargs = 1)
    parser.add_argument("-e",required=True, help="List of recipient emails", type = str, nargs = '+')
    parser.add_argument("-cc", help="List of email recipients",type =str, nargs = '+')              
    args = parser.parse_args()

    
    if len(args.pw[0])>0 and len(args.db[0])>0 and len(args.u[0])>0 and len(args.e[0])>0:
        extract_sql(args.pw[0],args.db[0],args.u[0],args.e,args.cc)
    else:
        raw_input('Error: Not enough values to process values.  Please re-enter server, database, user, and email information.')

except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        raw_input("Error: cript has encountered an error. Please investigate and fix the problem before rerunning the script.  Press Enter to exit...")
        sys.exit()
    
finally:
    print('Emails sent for KEA and internal well masters')


