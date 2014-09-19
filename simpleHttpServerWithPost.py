import os
import sys
import SimpleHTTPServer
import SocketServer
import cgi
import urlparse
import json

PORT = 1234
local_filepath = sys.argv[1]

response_filepath = 'js/responseFilepath.txt'
f = open(response_filepath, 'w')
f.write(local_filepath)
f.close()

def format_JSON(json_str):
    print json_str

    # json_str.replace('":{', '":{\n        ')
    # json_str.replace('', '')
    json_dict = eval(json_str)

    #sorted by key
    sorted(json_dict.items(), key=lambda d: d[0]) 

    string = '{\n'
    for key in json_dict:
        string += '    "%s":{\n' % key
        subjson = json_dict[key]
        for ikey in subjson:
            string += '        "%s":"%s",\n' % (ikey, subjson[ikey])
        string = string[:-2]
        string += '\n'
        string += '    },\n'
    string = string[:-2]
    string += '\n' 
    string += '}'
    return string

def output_JSON(json_str):
    path = 'config/' + local_filepath
    string = format_JSON(json_str)
    f = open(path, 'w')
    f.write(string)
    f.close()
    print path

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        qs = self.rfile.read(length)
        #post_data = urlparse.parse_qs(qs.decode('utf-8'))
        output_JSON(qs)
        #form = cgi.FieldStorage()
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        #httpd.socket.close()


Handler = ServerHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT

os.system('firefox 127.0.0.1:1234')

try:
    httpd.serve_forever()
except Exception, e:
    print 'SimpleHTTPServer is closed!'
