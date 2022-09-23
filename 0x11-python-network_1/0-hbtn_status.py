import urllib2

the_url = 'https://alx-intranet.hbtn.io/status'
req = urllib2.Request(the_url)
handle = urllib2.urlopen(req)
the_page = handle.read()
