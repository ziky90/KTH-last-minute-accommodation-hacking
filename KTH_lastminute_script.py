import urllib2, re, smtplib, time

fromaddr = 'your@gmail.com'
toaddrs  = 'lastminute@accomosation.email'
username = 'your@gmail.com'
password = 'your_password'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)

def deleteTags(string):
    deleteMode = False
    string = string.replace("<br>","")
    string = string.replace("<p>","")
    string = string.replace("</p>","")
    string = string.replace("<strong>","")
    string = string.replace("</strong>","")
    string = string.replace("</br>","")
    string = string.replace("<br />","")
    string = string.replace("<br/>","")
    string = string.replace("CODE: ","")
    string = string.replace("CODE:","")
	
    string = string[:50]
    return string



#string that indicates if  the website was updated
string = "lastminute accomodation is closed"   #something that is expected to be changed on the website
time.sleep(60)

while True:
    data = urllib2.urlopen("http://www.kth.se/en/studies/2.1328/last-minute-housing-1.85804").read()
    matches = re.findall(string, data)

    #site was not updated yet string found more than once
    if len(matches) > 0:
        print "no code yet, checking over...\n"

    #website have been updated
    else:
        matches = re.findall("gen x4(.*\n.*)", data)

        #some unexpected problem
        if len(matches) == 0:
            print "not found"
            
        #code has been found so send the email
        else:
            value = matches[0]
            print "We found: " + value
            value = deleteTags(value)
            msg = "\r\n".join(["From: your@gmail.com", "To: lastminute@accomosation.email",  "Subject:"+value,  "","last minute accommodation request"])
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()
            print "email succesfully sent"

        break    


    

