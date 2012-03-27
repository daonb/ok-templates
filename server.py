# File: simplehttpserver-example-1.py
import os
import urlparse
import BaseHTTPServer
import pystache
import yaml
import json
import gettext
import mimetypes

# minimal web server.  serves mustache templates relative to the
# current `templates` directory.

PORT = 8000
LANG = ['he']
COMMON_CONTEXT_FN = 'context.yaml'
# TODO: this should be automated, maybe using os.walk
pystache.Loader.template_path = ['templates', 'templates/partials', 'templates/agenda']

class MustachServer(BaseHTTPServer.BaseHTTPRequestHandler):
    common_context = yaml.load(open(COMMON_CONTEXT_FN).read())
    loader = pystache.Loader()
    translation = gettext.translation('mustache', 'locale', LANG)

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        loc = parsed_path.path[1:] # the first char in a '/' so skip it
        size = parsed_path.params
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
            # render a mustache template based on the url
            url_parts = loc.split('/')
            app = url_parts[0]
            context = self.common_context.copy()

            if len(url_parts) == 1:
                template_name = '%s_list' % app
                context_fn = os.path.join("fixtures", app, "list.json")

            else:
                template_name = 'agenda_detail'
                fixture_name = "%s.json" % url_parts[1]
                context_fn = os.path.join("fixtures", app, fixture_name)

            if os.path.exists(context_fn):
                context.update(json.load(open(context_fn)))

            if size == 's':
                dump = {"template": open(os.path.join("templates", app, "%s.mustache"% template_name)).read(), 
                        "context": json.dumps(context),
                        "script": open(os.path.join("templates", app, "%s.js"% template_name)).read(),
                       }
                template_name = 'small_base'

            template = self.loader.load_template(template_name, encoding='utf-8')
            if not template:
                self.send_response(500)
                self.end_headers()
                return

            context['_'] = lambda x: self.translation.ugettext(x)
            html = pystache.render(template, context)

            if size == 's':
                html = pystache.render(template, context) % dump

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

