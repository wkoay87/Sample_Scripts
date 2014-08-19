import pyodbc,xlsxwriter, sys, datetime as dt, time,calendar,os, argparse,adodbapi
from datetime import datetime
from datetime import timedelta
from subprocess import call

from helpers.email_helper import send_mail
from helpers import SQL_helper
from helpers.DB_helper import DB_Connection
#SQL statements

KEA_SQL = SQL_helper.NewWellsAdded.KEA_SQL

INT_SQL = SQL_helper.NewWellsAdded.INT_SQL
    
def create_xl(server,db,user,sql_nm,ws_num,xl_nm):
    assert type(sql_nm)==list
    PRD_con = DB_Connection(server,db,user)
    workbook = xlsxwriter.Workbook(xl_nm)
    
    if ws_num ==1:
        rows = PRD_con.sqlserver_sql(sql_nm[0])
        worksheet = workbook.add_worksheet(sql_nm[1])
        worksheet.set_column('B:Q',10)

        tbl_len = str(len(rows)+2) #add two to include header and 0 row
        
        for i, row in enumerate(rows):
                worksheet.write_row(i+2, 1, row)

        worksheet.add_table('B2:P'+tbl_len,
                            {'columns':[{'header': 'Property #'},
                            {'header': 'Property Name'},
                            {'header': 'Acquisition #'},
                            {'header': 'State'},
                            {'header':'County'},
                            {'header': 'Completion Status'},
                            {'header': 'API #'},
                            {'header': 'BA #'},
                            {'header': 'Interest Type'},
                            {'header': 'Decimal Interest'},
                            {'header': 'Development Year'},
                            {'header': 'Field'},
                            {'header': 'Reservior'},
                            {'header': 'Operator'},
                            {'header': 'Effective Date'}]})

    else:
        rows = PRD_con.sqlserver_sql(sql_nm[0])
        worksheet = workbook.add_worksheet(sql_nm[1])
        worksheet.set_column('B:Q',12)
        format = workbook.add_format({'bold':True})
        #tbl_len = str(len(rows)+2) #add two to include header and 0 row

        columns = ['Property #',
                'Property Name',
                'Acquisition #',
                'State',
                'County',
                'Completion Status',
                'API #',
                'Interest Type',
                'Decimal Interest',
                'Development Year',
                'Field',
                'Reservior',
                'Operator',
                'Effective Date']
        
        worksheet.write_row(1,1,columns,format)
        
        for i, row in enumerate(rows):
                worksheet.write_row(i+2, 1, row)

        
        
        '''worksheet.add_table('B2:O'+tbl_len,
                            {'columns':[{'header': 'Property #'},
                            {'header': 'Property Name'},
                            {'header': 'Acquisition #'},
                            {'header': 'State'},
                            {'header':'County'},
                            {'header': 'Completion Status'},
                            {'header': 'API #'},
                            {'header': 'Interest Type'},
                            {'header': 'Decimal Interest'},
                            {'header': 'Development Year'},
                            {'header': 'Field'},
                            {'header': 'Reservior'},
                            {'header': 'Operator'},
                            {'header': 'Effective Date'}]})
        
        for i, row in enumerate(rows):
            worksheet.write_row(i+2, 1, row)'''
                
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

        kea_nm_dt = 'KEA_NewWellsAdded' + datetime.now().strftime('%m_%d_%Y.xlsx')
        bsm_nm_dt = 'BSM_NewWellsAdded' + datetime.now().strftime('%m_%d_%Y.xlsx')

        sql_kea = KEA_SQL + sfirst_day + ' AND ' + slast_day    
        sql_bsm = INT_SQL.replace("@@DATERANGE",sfirst_day + ' AND ' + slast_day)
        #sql_bsm_gwi = INT_SQL_GWI.replace("@@DATERANGE",sfirst_day + ' AND ' + slast_day)

        '''sql_kea = KEA_SQL + "'2014/04/01'" + ' AND ' + "'2014/04/30'"
        sql_bsm = INT_SQL.replace("@@DATERANGE", "'2014/04/01' AND '2014/04/30'")
        sql_bsm_gwi = INT_SQL_GWI.replace("@@DATERANGE", " '2014/04/01' AND '2014/04/30' ")'''
        
        create_xl(server,db,user,[sql_kea,'KEA New Wells'],1,kea_nm_dt)
        #create_xl(server,db,user,[[sql_bsm,'BSM New Wells'],[sql_bsm_gwi,'BSM New Wells(GWI)']],1,bsm_nm_dt)
        create_xl(server,db,user,[sql_bsm,'BSM New Wells'],2,bsm_nm_dt)
        
        send_mail('NewWellsAdded@blackstoneminerals.com',
                  elist,
                  cclist,
                  'New Wells Added generated on ' + lastMonth.strftime("%B") +' '+ lastMonth.strftime("%Y") ,
                  'The attached Excel spreadsheet contains newly added wells for the month of '+ lastMonth.strftime("%B")+', ' + datetime.now().strftime('%Y')+
                  '.  If you have any questions regarding this spreadsheet, please contact InformationTechnology@blackstoneminerals.com.',
                  [kea_nm_dt,bsm_nm_dt])

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
    print('Emails sent for KEA and internal well masters')


