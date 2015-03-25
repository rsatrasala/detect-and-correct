
Detect and Correct automation setup

What do you need to install?

1. Python - if you do not have python already, here you go http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/

2. Selenium - I am using selenium for automating the user actions
	1. The easiest way is to install using pip command : pip install -U selenium
	2. If you do not have pip already, use the following command or the detailed instructions are available in the above link. Please use "sudo" to install pip ![screen shot 2015-03-11 at 11 52 05 am](https://cloud.githubusercontent.com/assets/5702592/6649403/6b1b924a-c9a6-11e4-8fb1-869ea8a32409.png)
	

	
3. Splinter - is an abstraction layer on top of existing browser automation tools such as Selenium. It has a high-level API that makes it easy to write automated. Install splinter using the command [sudo] pip install splinter

4. Firefox - I am using firefox browser for the entire run. Available at https://www.mozilla.org/en-US/firefox/new/

How to setup the DNC script

1. Download the files dnc.py and urls.csv from this git project and copy them into a folder. Lets call "install directory"

2. Inside this folder open dnc.py using text edit and update the following values in the "#user setup” section
	1. dncdir : The directory where the downloaded reports should be saved for example "/Users/rsatrasala/Downloads/dnc". NOTE: This directory should be different from the install directory of step 1
	2. mmxusername : This is your metamarkets username "rsatrasala@twitter.com"
	3. mmxpassword : This is your metamarkets password "<password>"
	4. reportRefreshTime :  30

3. open a terminal and change to the install directory by doing "cd <install directory>"

4. Finally run "python dnc.py". NOTE: If you see any indentation error, tab spaces would have been messed up. Make sure its tabbed as below ![screen shot 2015-03-13 at 10 22 22 pm](https://cloud.githubusercontent.com/assets/5702592/6650443/87206a3c-c9cf-11e4-9d55-44002b5df95d.png)

