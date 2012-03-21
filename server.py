# File: simplehttpserver-example-1.py
import os
import urlparse
import BaseHTTPServer
import pystache
import yaml
import gettext
import mimetypes

# minimal web server.  serves mustache templates relative to the
# current `templates` directory.

PORT = 8000
LANG = ['he']
COMMON_CONTEXT_FN = 'context.yaml'
pystache.Loader.template_path = ['templates', 'templates/partials']

class MustachServer(BaseHTTPServer.BaseHTTPRequestHandler):
    common_context = yaml.load(open(COMMON_CONTEXT_FN).read())
    loader = pystache.Loader()
    translation = gettext.translation('mustache', 'locale', LANG)

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        loc = parsed_path.path[1:] # the first char in a '/' so skip it
        if os.path.exists(loc):
            # static file, guess the content-type and serve
            src = open(loc).read()
            self.send_response(200)
            mime, enc = mimetypes.guess_type(loc)
            if (mime):
                self.send_header("content-type", mime) 

            self.end_headers()
            self.wfile.write(src)
        else:
            template = self.loader.load_template(loc, encoding='utf-8')
            if not template:
                self.send_response(500)
                self.end_headers()
                return

            context = self.common_context.copy()
            context_fn  = 'templates/%s.yaml' % loc
            if os.path.exists(context_fn):
                context.update(yaml.load(open(context_fn).read()))

            context['_'] = lambda x: self.translation.ugettext(x)
            html = pystache.render(template, context)
            # response headers
            self.send_response(200)
            self.send_header("content-type", "text/html") # 200 in an HTTP OK Result Code
            self.end_headers()
            # and the content
            self.wfile.write(html.encode('utf-8'))

# the next few lines are what happens when ran from the shell:
# $ python server.py
if __name__ == "__main__":
    httpd = BaseHTTPServer.HTTPServer(('', PORT), MustachServer)
    print "serving at port", PORT
    httpd.serve_forever()

