#%% for x in range(start,stop,step)
for x in range (10,30,2):
    print(x)
    print"we're on time %d"%(x)
#%% while loop from 1 to infinity
x = 1
while True:
    print "To infinity and beyond! We're getting close, on %d now!"%(x)
    x += 1
#%% Nested loops
for x in xrange(1,5):
    for y in xrange(1,3):
        print'%d * %d = %d' %(x, y, x*y)
#%% xrange vs range
range(4)
xrange(4)
#%% Exams: else
for x in range(3):
    print x
else:
    print 'Final x= %d' %(x)
#%% Strings as an iterable
    string = "Hello world!"
    for x in string:
        print x 
#%% lists as an iterable
collection = ['hey',5,'d']
for x in collection:
    print x 
#%% loop over Lists of lists
    list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
    for a in list_of_lists:
        for x in a:
            print a
            print x
#%% Creating your own iterable
class Iterable(object):
    def __int__(self,values):
        self.values = values
        self.location = 0
        
    def __iter__(self):
        return self
        
    def next(self):
        if self.location == len(self.values):
            raise StopIteration
        value = self.values[self.location]
        self.location += 1
        return value
        
#%% range vs xrange (Python2)
import time
# use time.time() on Linux
start = time.clock()
for x in range(10000000):
    pass
stop = time.clock()
print stop - start

start = time.clock()
for x in xrange(10000000):
    pass
stop = time.clock()
print stop - start
#%% Time on small ranges 
import time
#use time.time() on Linux
start = time.clock()
for x in range(1000):
    pass
stop = time.clock()
print stop-start

start = time.clock()
for x in xrange(1000):
    pass
stop = time.clock()
print stop-start
#%% Your own range generator using yield!
def my_range(start,stop,step):
    while start <= stop:
        yield start
        start = start + step
        
for x in my_range(1,10,0.7):
    print x
#%%
x = 5;
while x<100:
    x = x + 20
    print x







        