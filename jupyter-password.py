# Script to create a password for the Jupyter notebook configuration 
#
# Written by Pieter de Rijk <pieter@de-rijk.com>
#

from notebook.auth import passwd 
import os

jupyter_config = os.path.expanduser('~/.jupyter/jupyter_notebook_config.py')
line = "==========================================================================="

print line
print "Setting Jupyter additional configuration"
print line
print "Please set a strong password"
pwhash = passwd()
print line
print "Following will be added to %s " % (jupyter_config)

jupyter_comment_start = "# Start of lines added by jupyter-password.py"
jupyter_comment_end = "# End lines added by jupyter-passwordd.py"
jupyter_passwd_line = "c.NotebookApp.password = u'%s'" % (pwhash) 
jupyter_no_browser = "c.NotebookApp.open_browser = False"

print " "
print "  %s " % (jupyter_comment_start)
print "  %s " % (jupyter_passwd_line)
print "  %s " % (jupyter_no_browser)
print "  %s " % (jupyter_comment_end)

print line

with open(jupyter_config, 'a') as file:
    file.write('\n')
    file.write(jupyter_comment_start + '\n')
    file.write(jupyter_passwd_line + '\n')
    file.write(jupyter_no_browser + '\n')
    file.write(jupyter_comment_end + '\n')
