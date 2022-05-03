# import http.client
# connection = http.client.HTTPConnection("www.google.com")
# connection.request("GET", "/")
# response = connection.getresponse()
# print(type(response))
# print(type(response))
# print(response.status, response.reason)
# if response.status == 200:
#     data  = response.read()
#     print(data)

#getresponse() - method returns an instance of the http.client.HTTPResponse class. The response object returns information about the requested resource data,and the properties and response metadata.
# The read() method allows us to read the requested resource data and return the specified number of bytes.
# Now that we have analyzed the responese object , we are going to review what could be the status code values in that object. 


#Another method to build an HTTP client with urllib.request

# import urllib.request
# import urllib.parse

#using a urlopen function, an object similar to a file is generated in whihc to read from the URL. This object has methods such as read, readline, readlines and close which work exactly the same as in file objects, although we are actually working with wrapper methods that abstract us from using low-level sockets.

#the URLopen functio provides an optional data paramter for sending information to HTTP addresses using the POST method, where the request itself sends parameters. This parameter is a string with the correct encoding.

# import urllib.request
# import urllib.parse
# data_dictionary = {"id" : "0123456789"}
# data = urllib.parse.urlencode(data_dictionary)
# data = data.encode('ascii')
# with urllib.request.urlopen("https://httpbin.org/post", data) as response:
#     print(response.read().decode('utf-8'))



#GETTING REQUEST AND RESPONSE HEADERS

import urllib.request
from urllib.request import Request
url = "https://" +input("Enter domain name : ")
# url2 = "https://" +url
print("Response Headers for " +url)
ua = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36'

def chrome_user_agent():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', ua)]
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(url)
    print("\n\nResponse Headers")
    print("----------------")
    for header, value in response.getheaders():
        print(header + ":" + value)

    request = Request(url)
    request.add_header('User_Agent', ua)
    print("\nRequest Headers")
    print("------------------")
    for header, value in request.header_items():
        print(header + ":" + value)

if __name__ == '__main__':
    chrome_user_agent()



