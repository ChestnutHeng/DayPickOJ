import os  
#import fcntl  


class Painter:
    hard_map = {1:'Easy', 2:'Median', 3:'Medium', 4:'Memorize', 5:'Taste'}
    def paint_problem(self, p):
        print("%d. %s" % (p.no, p.title))
        print("Difficult: %s" % (self.hard_map[p.hard]))
        if p.total_passed == 0:
            if p.total_commit == 0:
                print("Passed: 100 %")
            else:
                print("Passed: 0 %")
        else:
            print("Passed: %.2f %%" % (p.total_commit/float(p.total_passed)*100))
        print("%s\n" % (p.text))

class Locker:   
    def __init__(self, filename):  
        self.filename = filename
        self.path = './lock/' + self.filename
        self.handle = None
        # This will create it if it does not exist already  
        
      
    # Bitwise OR fcntl.LOCK_NB if you need a non-blocking lock   
    def acquire(self):  
        #fcntl.flock(self.handle, fcntl.LOCK_EX)
        if os.path.exists(self.path):
            return False
        else:
            self.handle = open(self.path, 'w')
            self.handle.close()
            return True

    def acquire_store(self, txt):  
        #fcntl.flock(self.handle, fcntl.LOCK_EX)
        if os.path.exists(self.path):
            return False
        else:
            self.handle = open(self.path, 'w')
            self.handle.write(txt)
            self.handle.close()
            return True
    
    def acquire_read(self):
        if not os.path.exists(self.path):
            return "", False
        else:
            self.handle = open(self.path, 'r')
            text = self.handle.read()
            self.handle.close()
            return text, True
          
    def release(self):
        if os.path.exists(self.path):
            os.remove(self.path)
        #fcntl.flock(self.handle, fcntl.LOCK_UN)  
          
    def __del__(self):  
        pass
