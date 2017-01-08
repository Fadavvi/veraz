####################################################
# Veraz [ File & Folder Finder ] V 0.1             #
# By: Milad Fadavvi [fadavvi\\At//gmail\\.//com]   #
# Thanks 2 ANP Sec Dep.                            #
####################################################
import sys 
import random
import string
import urllib2
from urllib2 import Request, urlopen, URLError
from time import gmtime, strftime
import time
delay_int = 0
cookie_string = ""
agent_string = "Chrome/41.0.2228.0"
################################################
##Usage & help##################################
def usage():
    print"____   ____"                          
    print"\   \ /   /________________  ________ V 0.1"
    print" \   Y   // __ \_  __ \__  \ \___   /"
    print"  \     /\  ___/|  | \// __ \_/    /_ "
    print'   \___/  \___  >__|  (____  /_____  |'
    print"              \/           \/      \/ By Milad Fadavvi\n\n "
    print ("Usage: veraz -u http://xyz.abc/ <options>\n")
    print ("Options:\n")
    print ("-o , --out <file add>             Save results in provided location.(optional)\n")
    print ("-f , --file <file add>            Format of file for searching.(optinal)\n")
    print ("-e , --extention                  File extention for searching.(optinal)\n")
    print ("-r type len repeat \n--random type len repeat\n")  
    print ("\t\t\t\t  Use random string in search.(optinal)\n")         
    print ("\t\t\t\t  |type --> uppercase, lowercase |")
    print ("\t\t\t\t  |digit, mix, all (special char)|\n")
    print ("-c , --cookie <string>            Add Cookie to request(s).(optional)\n")
    print ("-a , --agent <string>             Add User-Agent to request(s).(optional)\n")
    print ("-d , --delay <MS>                 Make delay between requests.(optional)\n")
    print ("-h , --help                       Print this message.\n")
    print ("-u --url <web address>            Base URL for searching.(recommanded)\n")
    print ('Examples:\nveraz.py -u http://x.a/ --file /r/f_names -e doc --cookie "session_id=123" -a "Chrome/41.0.2228.0"')
    print ('veraz.py -u http://xyz.abc/ -r lowercase 7 10')
    exit()
################################################
## Make random string ##########################
def random_string (char_set, lens, repeat):
    list_string= []
    if char_set == 'uppercase':
        for i in range (int(repeat)):
            list_string.insert(i ,''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(int(lens))))
    if char_set == 'lowercase':
        for i in range (int(repeat)):
            list_string.insert(i ,''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(int(lens))))
    if char_set == 'digit':
        for i in range (int(repeat)):
            list_string.insert(i ,''.join(random.SystemRandom().choice(string.digits) for _ in range(int(lens))))
    if char_set == 'mix':
        for i in range (int(repeat)):
            list_string.insert(i ,''.join(random.SystemRandom().choice(string.ascii_letters + string.digits ) for _ in range(int(lens))))
    if char_set == 'all':
        for i in range (int(repeat)):
            specials='_-:@&*()+!#$%^}{"|:;'
            list_string.insert(i ,''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + specials  ) for _ in range(int(lens))))
    return list_string
###############################################
##Read Dir(s) from file########################
def file_include(path):
    list_d =[]
    i=0
    file_d = open (path, 'r')
    for line in file_d:
        i= i+1
        list_d.insert(i , line) 
    file_d.close()     
    return list_d
##############################################
##Switches####################################
def __main__():
    i=1 
    while i < len(sys.argv):
        if (sys.argv[i] == '-h' or sys.argv[i] == '--help'):
            usage()
        if (sys.argv[i] == '-o' or sys.argv[i] == '--out'):
            global outputfile
            outputfile = sys.argv[i+1]
        if (sys.argv[i] == '-f' or sys.argv[i] == '--file'):
            global inputfile
            inputfile= file_include(sys.argv[i+1])
        if (sys.argv[i] == '-r' or sys.argv[i] == '--random'):
            global random_mode
            random_mode= random_string(sys.argv[i+1],sys.argv[i+2],sys.argv[i+3])
        if (sys.argv[i] == '-c' or sys.argv[i] == '--cookie'):
            global cookie_string       
            cookie_string= sys.argv[i+1]
        if (sys.argv[i] == '-a' or sys.argv[i] == '--agent'):
            global agent_string 
            agent_string= sys.argv[i+1]
        if (sys.argv[i] == '-d' or sys.argv[i] == '--delay'):
            global delay_int 
            delay_int= sys.argv[i+1]
        if (sys.argv[i] == "-u" or sys.argv[i] == "--url"):
            global target_url
            target_url= sys.argv[i+1]
	if (sys.argv[i] == "-e" or sys.argv[i] == "--extention"):
	    global ext
	    ext = sys.argv[i+1]
	i= i+1
##############################################
##############:)##############################
__main__()
Errors = []
OKs = []
i = 1
j= 1
links = []
##############################################
##Output File name & location#################
try: 
	file_out
except NameError:
	file_out = "Veraz-" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ".log"
file_output = open (file_out, 'a')
##############################################
##Randomized URL##############################
try: 
	random_mode
except NameError:
	random_mode =("random","mode","off")
else:
	m = 0 
	while m < len(random_mode):
		message = target_url + random_mode[m]
		links.insert(m, message)
		m = m+1
############################################
## File's contant included URL##############
try:
	inputfile
except NameError:
	inputfile = ("File","Mode","off")
else:
	m = 0 
	while m < len(inputfile):
		message = inputfile[m]
		links.insert(m, message.strip())
		m = m+1
##########################################
#File Extention mode######################
try:
	ext
except NameError:
	ext = ''
else:
	m = 0 
	while m < len(links):
		links[m] = links[m] +"."+ext
		m = m+1
#########################################
##Try access to resources################
try:
	target_url
except NameError:
	usage()
else:
	 for tests in links:
		time.sleep(float(delay_int))
		link = target_url + tests
		req = urllib2.Request(link, data=None)
		req.add_header ('Cookie', cookie_string)
		req.add_header ('User-Agent', agent_string )
		try:
    			response = urlopen(req)
		except URLError as e:
    			if hasattr(e, 'reason'):
				Error_text= link, 'Reason:', e.reason , ':('
        			Errors.insert(i, Error_text )
				i= i + 1
    			elif hasattr(e, 'code'):
	 			Error_text= link, 'Reason:', e.code , ':('
         			Errors.insert(i, Error_text)
	 			i= i + 1
		else:
       			OK_text = link, "OK :)"
       			OKs.insert (j, OK_text)
       			j = j + 1
###########################################
######Write logs###########################
for links_find in OKs:
	massage = ' -- '.join(['%s' % (links_find[n]) for n in xrange(len(links_find))]) + '\n'
	print (massage)
	file_output.write (str(massage))
for links_nfind in Errors:
	massage = ' -- '.join(['%s' % (links_nfind[n]) for n in xrange(len(links_nfind))]) + '\n'
	print (massage)
	file_output.write (str(massage))
file_output.close()
