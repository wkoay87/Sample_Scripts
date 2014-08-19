from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium ,os , time
from datetime import datetime

def DI_CopyResults(results,filename,page):
    f = open(filename + page + '.html','w')
    f.write(results.encode('ascii','ignore'))
    f.close()

def DI_basic(driver):
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[3]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[3]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[3]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[3]/td[7]/input').click()
            
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[4]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[4]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[4]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[4]/td[7]/input').click()
            
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[5]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[5]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[5]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[5]/td[7]/input').click()
            
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[6]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[6]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[6]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[6]/td[7]/input').click()
            
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[7]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[7]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[7]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[7]/td[7]/input').click()
            
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[8]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[8]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[8]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[8]/td[7]/input').click()
    
    
def DI_Prod_Basic(driver):
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[11]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[11]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[11]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[11]/td[7]/input').click()

    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[12]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[12]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[12]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[12]/td[7]/input').click()

    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[13]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[13]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[13]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[13]/td[7]/input').click()

    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[14]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[14]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[14]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[14]/td[7]/input').click()

    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[15]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[15]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[15]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[15]/td[7]/input').click()


def DI_Prod_Eng(driver):
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[17]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[17]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[17]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[17]/td[7]/input').click()

    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[18]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[18]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[18]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[18]/td[7]/input').click()

    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[19]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[19]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[19]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[19]/td[7]/input').click()

    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[20]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[20]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[20]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[20]/td[7]/input').click()

    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[21]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[21]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[21]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[21]/td[7]/input').click()

    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[22]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[22]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[22]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[22]/td[7]/input').click()

    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[23]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[23]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[23]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[23]/td[7]/input').click()

    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[24]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[24]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[24]/td[5]/input').click()

def DI_BD_columns(driver):
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[7]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[7]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[7]/td[7]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[8]/td[1]/input').click()

    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[11]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[11]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[11]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[11]/td[7]/input').click()

    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[12]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[12]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[12]/td[5]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[12]/td[7]/input').click()

    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[13]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[13]/td[3]/input').click()    

    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[14]/td[1]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[14]/td[3]/input').click()
    driver.find_element_by_xpath('//*[@id="selectableColumnsTable"]/tbody/tr/td[2]/table/tbody/tr[14]/td[5]/input').click()
    
def crawl(Cnty_Num):
    try:
        start_time = datetime.now()
        print 'Starting script at ' + start_time.strftime('%H:%M:%S')
        directory = os.getcwd()
        os.chdir(r""+directory)
        chromedriver = directory+r"\chromedriver"
        driver = webdriver.Chrome(chromedriver)
        #driver = webdriver.PhantomJS()
        url = 'http://www.drillinginfo.com/login.jsp'
        driver.get(url)
        username_login = driver.find_element_by_id("tbUserName")
        pw_login = driver.find_element_by_id("tbPassword")
        click_login = driver.find_element_by_id("submit1")

        pw_login.send_keys(pw)
        username_login.send_keys(user)
        click_login.click()

            #Second page
        driver.get('http://www.drillinginfo.com/frameInfo.jsp')
        #driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        run_search = True
        while run_search:
            #go_to_page = 75
            try:
                driver.switch_to.frame("bottomFrame")
                #Test various truncation limits
                #5K seems to work fairly well with default columns

                #Option 1 - 250, 2 - 1000,3 - 2500, 4 - 5000
                driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td[2]/form/table[7]/tbody/tr/td/select/option[4]').click()

                driver.execute_script("handleClick(document.thisForm.cbProduction)")
                driver.find_element_by_xpath('/html/body/div/form/table[1]/tbody/tr/td/table[40]/tbody/tr[2]/td[4]/table/tbody/tr[3]/td[2]/div/input[3]').click()
                
                driver.find_element_by_xpath('//*[@id="lbCounty"]/option['+str(Cnty_Num)+']').click()

                #All columns
                #driver.execute_script("checkboxBuilderOnCheckAll(true)")

                #No columns
                driver.execute_script("checkboxBuilderOnCheckAll(false)")
                
                #Basic
                #DI_basic(driver)
                
                #Prod Basic
                #DI_Prod_Basic(driver)

                #Prod engr
                #DI_Prod_Eng(driver)
                DI_BD_columns(driver)
                #time.sleep(5)
                
                from_date = driver.find_element_by_xpath('/html/body/div/form/table[1]/tbody/tr/td/table[16]/tbody/tr[2]/td[4]/table/tbody/tr/td[2]/input[1]')
                to_date = driver.find_element_by_xpath('/html/body/div/form/table[1]/tbody/tr/td/table[16]/tbody/tr[2]/td[4]/table/tbody/tr/td[2]/input[2]')

                fdate = '01/01/2014'
                tdate = '12/01/2015'
                from_date.send_keys(fdate)
                to_date.send_keys(tdate)
                time.sleep(5)
                
                driver.find_element_by_xpath('//*[@id="lbOrderAscDesc"]/option[@value="DESC"]').click()
                driver.find_element_by_xpath('//*[@id="lbOrderBy"]/option[@value="101"]').click()
                driver.find_element_by_xpath('/html/body/div/form/table[1]/tbody/tr/td/table[40]/tbody/tr[2]/td[4]/table/tbody/tr[4]/td/input').click()
                print 'Loading first page of results... if timeout occurs have to start back on Search screen'
                driver.find_element_by_id("next").click()
                print 'Not capturing load time on page0'
                run_search = False
            except:
                print 'Error loading first page navigating back to search screen...'
                driver.refresh()
                continue

        #Results page
        '''page_source = driver.page_source
        f = open('DI_prod.html','w')
        print 'writing page info to text file'
        #f.write(page_source)
        f.write(page_source.encode('ascii','ignore'))
        f.close()'''
        i = 0
        j = 0
        run = True

        #skip to certain page
        '''if go_to_page > 0:
            while go_to_page > 0 :
                go_to_page-=1
                print 'Skipping page#' + str(i)
                i+=1
                driver.find_element_by_xpath('//*[@id="table-view-results"]/table/tbody/tr[2]/td[3]/a').click()'''
        
        while run:
            try:
                page_source = driver.page_source
                DI_CopyResults(page_source,'DI_Prod_Cnty_'+str(Cnty_Num)+'_Page'+str(i))
                i += 1
                print 'Copying data on page#' + str(i)
                if "Not all the results could be returned" in page_source:
                    load_time = datetime.now()
                    driver.find_element_by_xpath('//*[@id="table-view-results"]/table/tbody/tr[2]/td[3]/a').click()
                    end_time = datetime.now()
                    loading = end_time - load_time
                    print 'Loaded page ' + str(i) + ' in ' + str(loading) + ' (HH:MM:SS) at ' +  datetime.now().strftime('%H:%M:%S')
                else:
                    run = False
                    print 'Process completed'
                    driver.quit()
                
            except :
                try:
                    j+=1
                    i+=1
                    print 'Encountered issue number ' + str(j) + ' at ' + datetime.now().strftime('%H:%M:%S')
                    print 'Assuming log out...'
                    time.sleep(5)
                    alert = driver.switch_to_alert()
                    alert.accept()
                    driver.back()
                    page_source = driver.page_source
                    continue
                
                    '''if "Not all the results could be returned" in page_source:
                        driver.find_element_by_xpath('//*[@id="table-view-results"]/table/tbody/tr[2]/td[4]/a').click()
                        print 'Should restart process here'
                        continue
                    else:
                        print 'Hit break point but going to attempt retrying 1'
                        #continue anyways.... loop will determine when to stop if page doesn't have extra info
                        i+=1
                        continue'''
                except:
                    print 'No log out but page failed to load possibly due to timeout... move onto next county'
                    driver.quit()
                    
            
    finally:
        print 'Completed copying county. Moving to next record...'
        

try:

    for Cnty_Num in xrange(1,5):
        print Cnty_Num
        crawl(Cnty_Num)
finally:
    print 'Copied 5 counties'

'''except selenium.common.exceptions.TimeoutException(msg=None, screen=None, stacktrace=None):
    driver.back()'''


'''data = []
for tr in driver.find_elements_by_xpath('//*[@id="tableViewTable"]//tr'):
tds = tr.find_elements_by_tag_name('td')
if tds:
data.append([td.text for td in tds])
        
print data[1]
print data[2]
print data[3]'''

'''time.sleep(4)
driver.execute_script("handleClick(document.thisForm.cbProduction)")
#prod_chb = driver.find_element_by_xpath('//*[@id="cbProductionLinkOn"]/a')
#prod_chb.click()


click_next = driver.find_element_by_id("submit")
click_next.click()
<a href="javascript: handleClick(document.thisForm.cbProduction);">Production</a>

//*[@id="cbProductionLinkOn"]/a'''
