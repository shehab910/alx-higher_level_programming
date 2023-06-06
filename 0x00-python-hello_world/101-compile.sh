# Write a script that compiles a Python script file.

# The Python file name will be stored in the environment variable $PYFILE

# The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)
#!/bin/bash
python3 -m compileall -b $PYFILE
