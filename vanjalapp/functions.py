import os

def signup(*sup):
        """
        taking the data from the signup page,and storing it in a fie name signup.txt
        returns false if the email id already exist!!!
        """
        s = os.getcwd()
        with open(s+'\\files\\signup.txt','r+') as f:
        	for email in f.readlines():
        	 	emails = email.split('|')#if email[0] == sup[0]:
        	 	if emails[0] == sup[0]:
        	 		return False
        	f.write(sup[0]+'|'+sup[1]+'|'+sup[2]+'|'+sup[3]+'\n')
def checklogin(*log):
    """
    checks for login authentiction using the signup.txt file
    """  
    s = os.getcwd() 
    with open(s+'\\files\\signup.txt') as f:
    	for user in f.readlines():
    		details = user.split('|')
    		if details[0]==log[0] and  details[1]==log[1]:
    			return details[3]
    	return False