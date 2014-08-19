import xlsxwriter, sys, datetime as dt, time,calendar,os, argparse,cx_Oracle
from datetime import datetime
from datetime import timedelta
from subprocess import call

from helpers.email_helper import send_mail
from helpers import SQL_helper
from helpers.DB_helper import DB_Connection

def create_xl(data_rows,xl_nm):
    #Connect to database
        
        workbook = xlsxwriter.Workbook(xl_nm)
        print 'add worksheet'
        
        worksheet = workbook.add_worksheet()

        for i, row in enumerate(data_rows):
                worksheet.write_row(i+2, 1, row)
        tbl_len = str(len(data_rows)+2)
        
        worksheet.add_table('B2:F'+tbl_len,
                            {'columns':[{'header': 'AGMT_NUM'},
                            {'header': 'DOC_ID'},
                            {'header': 'WHAT_MODIFIED'},
                            {'header': 'WHEN_MODIFIED'},
                            {'header':'WHO_MODIFIED'}
                            ]})
        
        worksheet.set_column('B:F',20)
        workbook.close()
    
def dnd_check(db,user,pw,elist,cclist):
    
    try:
        agm_send_email_chk = False
        db_con = DB_Connection (db,user,pw)

        #Check if rows > 0
        print 'query data'
        rows = db_con.ora_sql(SQL_helper.DND_Change_Log.DND_SQL)

        if len(rows)>0:
            send_email_chk = True

        if send_email_chk:
            current_date = dt.date.today()
            past_week = current_date - dt.timedelta(days=7)

            print 'create excel file'

            DND_change_log  = 'DND_Change_Log_'+ datetime.now().strftime('%m_%d_%Y.xlsx')

            create_xl(rows,DND_change_log)
        
            send_mail('DND_Change_Log@blackstoneminerals.com',elist,cclist,'Changes made to DND records from  ' + past_week.strftime("%m-%d-%Y") +' to '+ current_date.strftime("%m-%d-%Y") ,
                      'The attached Excel spreadsheet contains all updates from '+ past_week.strftime("%m-%d-%Y") +' to '+ current_date.strftime("%m-%d-%Y") +
                  '.  If you have any questions regarding this spreadsheet, please contact InformationTechnology@blackstoneminerals.com.',
                  [DND_change_log])
        
    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        raw_input("Script has encountered an error. Please investigate and fix the problem before rerunning the script.  Press Enter to exit...")
        sys.exit()
    

try:
        # Local variables:
    #Input database and PW information then run script
    parser = argparse.ArgumentParser(description = 'Checks if there are any agreement types differences at the header and subdivision level.')
    parser.add_argument("-d", help="Database TNS name", type = str, nargs = 1)    
    parser.add_argument("-u", help="Schema where log table resides", type = str, nargs = 1)
    parser.add_argument("-p", help="Password to database", type = str, nargs = 1)
    parser.add_argument("-m", help="Optional: Allows prompt of database information, user, and password. Enter a value of TRUE or FALSE (in uppercase).  Default value is False. ", type = str, default = 'False')
    parser.add_argument("-e", help="List of email recipients",type =str, nargs = '+')
    parser.add_argument("-cc", help="List of email recipients",type =str, nargs = '+')              
    args = parser.parse_args()

    if str(args.m) == 'TRUE':
        DB_INPUT = raw_input("ENTER DB NAME: ")
        USER_INPUT =  raw_input("ENTER DB USER/SCHEMA: ")
        PW_INPUT = raw_input("ENTER PW: ")
        EMAIL_LIST = raw_input("ENTER LIST OF EMAIL(S) SEPARATED BY A SPACE: ")
        CC_LIST = raw_input("OPTIONAL LIST OF CC EMAIL(S) SEPARATED BY A SPACE: ")
        EMAIL_INPUT = EMAIL_LIST.split(" ")
        CC_LIST = CC_LIST.split(" ")
        
    elif len(args.d[0])>0 and len(args.u[0])>0 and len(args.p[0])>0 and len(args.e[0])>0:
        DB_INPUT = str(args.d[0])
        USER_INPUT =  str(args.u[0])
        PW_INPUT = str(args.p[0])
        EMAIL_INPUT = args.e
        CC_LIST = args.cc
    else:
        raise Exception ("ERROR: Invalid or missing parameters have been passed into the script.")
    
    dnd_check(DB_INPUT,USER_INPUT,PW_INPUT,EMAIL_INPUT,CC_LIST)

except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        raw_input("Error: cript has encountered an error. Please investigate and fix the problem before rerunning the script.  Press Enter to exit...")
        sys.exit()
    
finally:
    print('end of script...')


