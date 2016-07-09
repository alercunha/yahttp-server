import argparse

from tornado import ioloop, web


class CorsEnabledHandler(web.StaticFileHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_access_preflight_headers(self):
        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Preflighted_requests
        self.set_header('Access-Control-Allow-Methods', 'POST, PUT, GET, DELETE, OPTIONS, HEAD')
        self.set_header('Access-Control-Allow-Headers', self.request.headers['Access-Control-Request-Headers'])
        self.set_header('Access-Control-Max-Age', '1728000')  # allow caching for 20 days

    def set_access_control_headers(self):
        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Access-Control-Allow-Origin
        self.set_header('Access-Control-Allow-Origin', self.request.headers['Origin'])
        self.set_header('Access-Control-Allow-Credentials', 'true')

    def set_extra_headers(self, path):
        headers = self.request.headers
        if 'Access-Control-Request-Headers' in headers or 'Access-Control-Request-Method' in headers:
            self.set_access_preflight_headers()
        if 'Origin' in headers:
            self.set_access_control_headers()

    def options(self):
        self.set_status(204)
        self.finish()

    def write_error(self, status_code, **kwargs):
        super().write_error(status_code, **kwargs)


def run(args):
    # settings
    tornado_settings = {
    }
    # initialize
    handlers = [
        (r'/(.*)', CorsEnabledHandler, {'path': args.folder, 'default_filename': 'index.html'})
    ]
    app = web.Application(handlers, **tornado_settings)
    app.listen(args.port)
    print('Listening on port {0} folder {1}'.format(args.port, args.folder))
    try:
        ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        ioloop.IOLoop.instance().stop()
        print('Stopped')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-folder', help='directory to server', default='./')
    parser.add_argument('-port', help='http port to listen', default=8080)
    args = parser.parse_args()
    run(args)

if __name__ == '__main__':
    main()