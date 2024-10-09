#!/usr/bin/python3

import signal
import logging
from time import time
from math import floor
from configs import configs
from handlers import handlers, NotFound
from functools import partial
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.httpserver import HTTPServer

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

class Server(Application):
    def __init__(self, **kwargs):
        kwargs["debug"] = configs.env == "dev"
        kwargs["handlers"] = handlers
        kwargs["default_handler_class"] = NotFound
        super(Server, self).__init__(**kwargs)

    def graceful_shutdown(self, server):
        io_loop = IOLoop.current()

        def stop_loop(deadline):
            now = time()
            if now < deadline:
                logging.info("Shutting down in {}s".format(floor(deadline - now)))
                io_loop.call_later(1, stop_loop, deadline)
            else:
                io_loop.stop()
                logging.info("Server shutdown gracefully!")

        def shutdown():
            logging.info("Stopping HTTP server")
            server.stop()
            logging.info("Shutting down in {}s".format(configs.server.grace_period))
            stop_loop(time() + configs.server.grace_period)

        return shutdown

    def signal_handler(self, server, signum, frame):
        logging.warning("Caught signal: {}".format(signum))
        io_loop = IOLoop.current()
        io_loop.add_callback_from_signal(self.graceful_shutdown(server))

if __name__ == "__main__":
    app = Server(**{})
    host = configs.server.host
    port = configs.server.port
    grace_period = configs.server.grace_period

    server = HTTPServer(app)
    server.listen(port)
    logging.info("\n🚀 Server is up and running! \n🌐 Access it at: http://{}:{} 🎉".format(host, port))

    signal.signal(signal.SIGTERM, partial(app.signal_handler, server))
    signal.signal(signal.SIGINT, partial(app.signal_handler, server))
    IOLoop.current().start()
