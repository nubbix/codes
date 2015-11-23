#Made by Tom Knudsen - post@tknudsen.com
#Thanks to the guys over at www.python-forum.org

import random

#This print 7 random integers in 10 rows.
for i in range(10):
    print(random.sample(range(1, 35), 7))
