#!C:\Users\aman.raj\MyProject\PythonProgram\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'flask-swagger==0.2.13','console_scripts','flaskswagger'
__requires__ = 'flask-swagger==0.2.13'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('flask-swagger==0.2.13', 'console_scripts', 'flaskswagger')()
    )
