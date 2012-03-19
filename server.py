# File: simplehttpserver-example-1.py
import urlparse
import BaseHTTPServer
import pystache
import yaml

# minimal web server.  serves mustache templates relative to the
# current `templates` directory.

PORT = 8000
pystache.Loader.template_path = ['templates', 'templates/include']

class MustachServer(BaseHTTPServer.BaseHTTPRequestHandler):
    common_context = yaml.load(open('context.yaml').read())
    loader = pystache.Loader()

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        loc = parsed_path.path[1:] # the first char in a '/' so skip it
        if loc.startswith(self.common_context['MEDIA_URL']):
            # serve static files
            self.wfile.write(open(loc).read())
        else:
            context = self.common_context.copy()
            context.update(yaml.load(open('templates/%s.yaml' % loc).read()))
            template = self.loader.load_template(loc, encoding='utf-8')
            html = pystache.render(template, context)
            self.wfile.write(html.encode('utf-8'))

        self.send_response(200) # 200 in an HTTP OK Result Code
        self.end_headers()

# the next few lines are what happens when ran from the shell:
# $ python server.py
if __name__ == "__main__":
    httpd = BaseHTTPServer.HTTPServer(('', PORT), MustachServer)
    print "serving at port", PORT
    httpd.serve_forever()

