#!C:\RampUp\dev-sprint3\my_first_app\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==1.4','console_scripts','pip-2.7'
__requires__ = 'pip==1.4'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pip==1.4', 'console_scripts', 'pip-2.7')()
    )