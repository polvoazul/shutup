from importlib.metadata import version
try: __version__ = version(__name__)
except: pass
del version

def please():
    import warnings
    please._orig_warning = warnings.warn
    def warn(message:str, category:str='', stacklevel:int=1, source:str=''): # need hints to work with pytorch
        pass
    warnings.warn = warn
