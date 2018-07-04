import os
import sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.getcwd(), '../'))

import unittest                                 # noqa
import cherrypy                                 # noqa
import threading                                # noqa
import time                                     # noqa
from datetime import datetime, timedelta        # noqa
from cherrypysytray import SysTrayPlugin   # noqa


def on_quit(self):
    ''' Test for the user-defined `on_quit` method '''
    return 'on_quit'


def menu_method(self):
    return 'menu_method'


class TestScheduler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.setup_done = False
        cls.task_name = 'Increase Counter'
        cls.task_counter = 0
        cls.now = datetime.now().replace(microsecond=0)
        cls.task_instance = None

    def test_00_(self):
        return

    @classmethod
    def tearDownClass(cls):
        cherrypy.engine.stop()
        cherrypy.engine.exit()
        if os.path.isfile('./test_tasks.json'):
            os.unlink('./test_tasks.json')


class ServerRoot(object):
    @cherrypy.expose
    def index(self):
        return 'Test server running'


if __name__ == '__main__':
    menu_options = (('TestOption', None, TestScheduler.menu_method),)
    systrayplugin = SysTrayPlugin(cherrypy.engine, 'core/favicon.ico', 'Watcher', menu_options)

    # Start the CherryPy server
    cherrypy.log.screen = None
    cherrypy.engine.signals.subscribe()
    cherrypy.tree.mount(ServerRoot(), '/')
    cherrypy.config.update('./cp_config.conf')
    cherrypy.engine.start()

    threading.Thread(target=unittest.main, kwargs={'verbosity': 2}).start()
    cherrypy.engine.block()
