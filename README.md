## CherrypySystray

CherrypySystray is a simpleplugin interface for [infi.systray](https://github.com/Infinidat/infi.systray) that allows systray to start and stop according to Cherrypy's signals.

#### Usage

    import cherrypy
    from cherrypysytray import SysTrayPlugin
    import webbrowser


    def on_quit():
        print('This function is called if the server is shut down through the taskbar.')


    class ServerRoot(object):
        @cherrypy.expose
        def index(self):
            return 'Test server running'


    if __name__ == '__main__':
        menu_options = (('Open Browser', None, lambda *args: webbrowser.open('https://github.com/sawyersteven/CherrypySystray')),)
        systrayplugin = SysTrayPlugin(cherrypy.engine, 'favicon.ico', 'Test', menu_options, on_quit=on_quit)
        systrayplugin.subscribe()

        cherrypy.quickstart(ServerRoot(), '/')


`SysTrayPlugin` takes the same arguments as [infi.systray](https://github.com/Infinidat/infi.systray) with the addition of `cherrypy.engine` as the first argument.


#### Known Issues

When shutting down the Cherrypy server through the system tray you may see terminal output indicating that an exception has been ignored `RuntimeError: cannot join current thread`. This seems to have no negative effects on usage.
