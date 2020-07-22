from http.client import HTTPConnection
con = HTTPConnection('www.google.com')
con.request('GET', '/')
result = con.getresponse()
contents = result.read()
print(contents)