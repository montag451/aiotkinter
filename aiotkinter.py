import asyncio
try:
    import selectors
except ImportError:
    import asyncio.selectors as selectors
import tkinter
import sys

if sys.platform == 'win32':
    raise ImportError('%s is not available on your platform'.format(__name__))

class _TkinterSelector(selectors._BaseSelectorImpl):

    def __init__(self):
        super().__init__()
        self._tk = tkinter.Tk(useTk=0)
        self._ready = []

    def register(self, fileobj, events, data=None):
        key = super().register(fileobj, events, data)
        mask = 0
        if events & selectors.EVENT_READ:
            mask |= tkinter.READABLE
        if events & selectors.EVENT_WRITE:
            mask |= tkinter.WRITABLE
        def ready(fd, mask):
            assert key.fd == fd
            events = 0
            if mask & tkinter.READABLE:
                events |= selectors.EVENT_READ
            if mask & tkinter.WRITABLE:
                events |= selectors.EVENT_WRITE
            self._ready.append((key, events))
        self._tk.createfilehandler(key.fd, mask, ready)
        return key

    def unregister(self, fileobj):
        key = super().unregister(fileobj)
        self._tk.deletefilehandler(key.fd)
        return key

    def select(self, timeout=None):
        self._ready = []
        if timeout is not None:
            timeout = int(timeout*1000)
            token = self._tk.createtimerhandler(timeout, lambda: True)
        self._tk.dooneevent()
        if timeout is not None:
            token.deletetimerhandler()
        return self._ready

class TkinterEventLoopPolicy(asyncio.DefaultEventLoopPolicy):

    def new_event_loop(self):
        try:
            return self._loop_factory(selector=_TkinterSelector())
        except TypeError:
            raise Exception('The default event loop is not a selector event loop')
