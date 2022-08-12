from django import db
from dramatiq.middleware import Middleware

class DbConnectionsMiddleware(Middleware):
    """This middleware cleans up db connections on worker shutdown.
    """

    def _close_connections(self, *args, **kwargs):
        for conn in db.connections.all():
            conn.close()

    before_process_message = _close_connections
    after_process_message = _close_connections

    before_consumer_thread_shutdown = _close_connections
    before_worker_thread_shutdown = _close_connections
    before_worker_shutdown = _close_connections
