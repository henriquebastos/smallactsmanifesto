import sys
import virtualenv

extension = open('venv-extension.py').read()
output = virtualenv.create_bootstrap_script(extension)

version = sys.version_info
f = open('bootstrap%d.%d.py' % (version.major, version.minor), 'w').write(output)
