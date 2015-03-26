from splinter import Browser
from selenium import webdriver
import time
import csv
import os, errno
import datetime
from datetime import datetime, timedelta
import sys

#user setup
dncdir = "< update with the dir to download reports>"
mmxusername = "< update with metamarkets username>"
mmxpassword = "< update with metamarkets password>"
reportRefreshTime = 30

#initializations
yday = datetime.now() - timedelta(days=1)
yesterdate = yday.strftime('%Y-%m-%d')
homepage = "https://dash.metamarkets.com"

#cleanup
try:
	for root, dirs, files in os.walk(dncdir):
        	for file in files:
			os.remove(dncdir + "/" + file)
except OSError as e:
	print("Nothing to cleanup. So moving on")
except IOError as e:
	print("Did you setup the dnc director? Please update and rerun!!!")
	

#set firefox preferences 
profile = webdriver.firefox.firefox_profile.FirefoxProfile()
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('text/csv,'
                                                                  'application/csv,'
                                                                  'application/msexcel'))
profile.set_preference('browser.download.dir', dncdir)
profile.set_preference("browser.download.folderList",2)

#instantiate firefox
browser = webdriver.Firefox(firefox_profile=profile)
browser.maximize_window()

#access mmx and login
browser.get(homepage)
time.sleep(5)
browser.find_element_by_id("form-id1").send_keys(mmxusername)
browser.find_element_by_id("form-id2").send_keys(mmxpassword)
browser.find_element_by_css_selector(".primary.login").click()
time.sleep(5)

#read the urls from the urls config file
urls = open('urls.csv').read().split("\r")
#Download each report
u=1
for row in urls:
	try:
		url = row
	        url = url.replace("$$todate$$", str(yesterdate))
        	print url
	        browser.get(url)
        	time.sleep(reportRefreshTime)
	        browser.find_element_by_css_selector(".range-label.ng-binding").click()
        	browser.switch_to_active_element()
	        time.sleep(2)
        	daterange = browser.find_elements_by_css_selector(".preset.ng-binding.ng-scope")
	        daterange[1].click()
        	rangeapply = browser.find_elements_by_css_selector(".apply-button")
	        rangeapply[1].click()
        	time.sleep(5)
		button = browser.find_element_by_xpath("//div[@title='Download']")
		button.click()	
		time.sleep(5)
		browser.switch_to_active_element()
		time.sleep(1)
		columns = browser.find_elements_by_css_selector(".ng-binding.ng-scope.unchecked-box")
		columns[1].click()
		columns[2].click()
		browser.find_element_by_css_selector(".primary.ng-binding").click()
		print str(u) + "/5 reports Downloaded..."
		u = u+1
		time.sleep(reportRefreshTime)
		print("")
	except:
		e = sys.exc_info()[0]
		print e
		print("")
		print("!!! Action needed !!!")
		print("There was a failure. Probably the pages are loading slowly.")
		print("Please increase the value of -- reportRefresh -- in the \'user setup\' section and retry") 
		browser.quit()
		quit()
time.sleep(5)
browser.quit()

#parse the report and print out the creative ids for which auctions > 10000 and survival rate < 0.1
print""
print""
print""
print "Creative Ids that need your attention"
print ""
os.chdir(dncdir)
for root, dirs, files in os.walk(dncdir):
        for file in files:
                with open(file, 'rU') as f:
                        reader = csv.reader(f)
                        j=0
                        try:
                                for row in reader:
                                        if j == 3:
                                                print "Checking the creatives from the report:"
                                                print row[1]
                                                print ""
                                        if j >= 6:
						dsp = row[0]
                                                creativeId = row[1]
                                                auctions = row[2]
                                                survivalRate = row[4]
                                                ctr = row[5]
                                                if int(auctions) > 10000:
                                                        if survivalRate != "" and float(survivalRate) < 0.1:
                                                                print "survival is < 0.1      :  " + dsp + " - " + creativeId 
                                                        if ctr != "" and float(ctr) < 0.01:
                                                                print "ctr is < 0.01         : " + dsp + " - " + creativeId
                                        j = j+1
                        except csv.Error as e:
                                print e
                        print ""
                        print "-----"
                        print ""
print""
print""
print""
