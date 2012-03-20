# File: simplehttpserver-example-1.py
import os
import urlparse
import BaseHTTPServer
import pystache
import yaml
import gettext

# minimal web server.  serves mustache templates relative to the
# current `templates` directory.

PORT = 8000
COMMON_CONTEXT_FN = 'context.yaml'
pystache.Loader.template_path = ['templates', 'templates/partials']

class MustachServer(BaseHTTPServer.BaseHTTPRequestHandler):
    common_context = yaml.load(open(COMMON_CONTEXT_FN).read())
    loader = pystache.Loader()
    translation = gettext.translation('mustache', 'locale', fallback=True)

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        loc = parsed_path.path[1:] # the first char in a '/' so skip it
        try:
            context = self.common_context.copy()
            template_fn  = 'templates/%s.yaml' % loc
            if os.path.exists(template_fn):
                context.update(yaml.load(open(template_fn).read()))
            context['_t'] = lambda x: self.translation.ugettext(x)
            template = self.loader.load_template(loc, encoding='utf-8')
            html = pystache.render(template, context)
            # response headers
            self.send_response(200)
            self.send_header("content-type", "text/html") # 200 in an HTTP OK Result Code
            self.end_headers()
            # and the content
            self.wfile.write(html.encode('utf-8'))
        except IOError:
            ''' probably a static file, let's try and read it '''
            try:
                src = open(loc).read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(src)
            except IOError:
                '''nothing works, return a 500 '''
                self.send_response(500)
                self.end_headers()

# the next few lines are what happens when ran from the shell:
# $ python server.py
if __name__ == "__main__":
    os.environ['LANG'] = 'he'
    httpd = BaseHTTPServer.HTTPServer(('', PORT), MustachServer)
    print "serving at port", PORT
    httpd.serve_forever()

