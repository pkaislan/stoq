
import os
import sys

program_name    = "Stoq"
website         = 'http://www.stoq.com.br'
version         = "0.8.1"
release_date    = (2006, 8, 25)

# Required version of Python
REQUIRED_VERSION = (2, 4)

KIWI_REQUIRED = '1.9.9'

# Directory name, defaults to name of binary, it is relative to ..
# a, __init__.py and main.py is expected to be found there.
DIRNAME = None

# Application name, defaults to capitalized name of binary
APPNAME = None

# Do not modify code below this point
dirname = DIRNAME or os.path.split(sys.argv[0])[1]
appname = APPNAME or dirname.capitalize()

version_string = sys.version.split(' ')[0]
majmin = tuple(map(int, version_string.split('.')))
if majmin < REQUIRED_VERSION:
    raise SystemExit("ERROR: Python %s or higher is required to run %s, "
                     "%s found" % ('.'.join(map(str, REQUIRED_VERSION)),
                                   appname,
                                   version_string))


try:
    from kiwi.environ import Library
except ImportError:
    raise SystemExit("Could not find kiwi, is a recent version %s installed?"
                      % KIWI_REQUIRED)

# XXX: Use Application
lib = Library('stoq')
if lib.uninstalled:
    lib.add_global_resource('pixmaps', 'data/pixmaps')
    lib.add_global_resource('glade', 'data/glade')
    lib.add_global_resource('config', 'data/config')
    lib.add_global_resource('docs', '.')
lib.enable_translation()
lib.set_application_domain('stoq')
