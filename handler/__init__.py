from .version import __version__
from .handler import Handler

# if somebody does "from handler import *", this is what they will
# be able to access:
__all__ = [
    'Handler',
]