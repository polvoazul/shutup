try:
    from importlib.metadata import version as _version
    __version__ = _version(__name__)
except Exception: pass

import warnings as _warnings
_original_warn = None

def _warn(message:str, category:str='', stacklevel:int=1, source:str=''): # need hints to work with pytorch
    pass # In the future, we can implement filters here. For now, just mute everything.

def please():
    global _original_warn
    _original_warn = _warnings.warn
    _warnings.warn = _warn

def jk():
    global _original_warn
    if not _original_warn: return
    _warnings.warn = _original_warn
    _original_warn = None

def are_warnings_muted():
    return _original_warn != None

class _mute_warnings:
    ''' Mute all warnings. Can also be used as a context manager.'''
    def __call__(self):
        please()
    def __enter__(self):
        self.muted = are_warnings_muted()
        please()
    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.muted: jk()
mute_warnings = _mute_warnings()

class unmute_warnings:
    ''' Unmute warnings if previously muted. Otherwise, do nothing. Can also be used as a context manager. '''
    def __call__(self):
        jk()
    def __enter__(self):
        self.muted = are_warnings_muted()
        jk()
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.muted: please()
unmute_warnings = unmute_warnings()
