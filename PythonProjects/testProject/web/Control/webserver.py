import  os, sys
from http.server import HTTPServer,CGIHTTPRequestHandler

webdir = "." #存放HTML文件和CGI-BIN文件夹的所在
port = 8080

os.chdir(webdir)
srvraddr = ("",port)
srvrobj = HTTPServer(srvraddr,CGIHTTPRequestHandler)
srvrobj.serve_forever()