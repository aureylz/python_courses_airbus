# Answers to questions #
When you import a module you have to be carefull about the package search priority.<br>
If there is many modules with the same name in the python path, you have to remember python will use the following priorities:
 1. system libraries
 2. current folder
 3. PYTHONPATH
 4. default lib folder (like /usr/local/lib/python/)