import os
from time import sleep

x=os.fork()
if x:
    identity = "Darth Wader"
    #sleep(1)
else:
    identity = "Luke"

print(identity)

identity = identity + " from starwars..."

print("----- " + identity + " died ------")
