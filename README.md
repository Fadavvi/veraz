# Veraz V0.1

=============================

Some kind of file/folder brute-forcer.

---------

You can you Veraz to find files in a website -e [doc,pdf,php,...] or to find folders
use random string to find or use a file with path/file names.
You can add cookie and user-agent to request and use delay to WAF protected sites.

Usage: veraz -u http://xyz.abc/ <options>

Options:
-o , --out <file add>                           Save results in provided location.(optional)

-f , --file <file add>                          Format of file for searching.(optinal)

-e , --extention                                File extention for searching.(optinal)

-r type len repeat, --random type len repeat    Use random string in search.(optinal)

              type --> uppercase, lowercase
              
              digit, mix, all (special char)
              
-c , --cookie <string>                          Add Cookie to request(s).(optional) 

-a , --agent <string>                           Add User-Agent to request(s).(optional)

-d , --delay <MS>                               Make delay between requests.(optional)

-h , --help                                     Print this message.

-u --url <web address>                          Base URL for searching.(recommanded)


Examples:

   veraz.py -u http://x.a/ -r lowercase 7 10
   
   Generate 10 lowercase random strings with lenth 7 and will test on http://x.a/
  
   -----
   
   veraz.py -u http://x.a/ --file /r/f_names -e doc --cookie "session_id=123" -a "Chrome/41.0.2228.0"
   
   
   Read filenames from /r/f_names and add .doc to them and will test on http://x.a/ with provided 
   cookie & user-agent strings.
   
   
   
   ==============================================================
   
   By Milad Fadavvi 
