from importlib.metadata import version as _version
try: __version__ = _version(__name__)
except Exception: pass

def please():
    import warnings
    please._orig_warning = warnings.warn
    def warn(message:str, category:str='', stacklevel:int=1, source:str=''): # need hints to work with pytorch
        pass # In the future, we can implement filters here. For now, just mute everything.
    warnings.warn = warn
