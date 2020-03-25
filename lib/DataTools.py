import os  
#import fcntl  

def my_align(_string, _length, _type='L'):
    """
    中英文混合字符串对齐函数
    my_align(_string, _length[, _type]) -> str

    :param _string:[str]需要对齐的字符串
    :param _length:[int]对齐长度
    :param _type:[str]对齐方式（'L'：默认，左对齐；'R'：右对齐；'C'或其他：居中对齐）
    :return:[str]输出_string的对齐结果
    """
    _str_len = len(_string)  # 原始字符串长度（汉字算1个长度）
    for _char in _string:  # 判断字符串内汉字的数量，有一个汉字增加一个长度
        if '\u4e00' <= _char <= '\u9fa5':  # 判断一个字是否为汉字（这句网上也有说是“ <= u'\u9ffff' ”的）
            _str_len += 1
    _space = _length-_str_len  # 计算需要填充的空格数
    if _type == 'L':  # 根据对齐方式分配空格
        _left = 0
        _right = _space
    elif _type == 'R':
        _left = _space
        _right = 0
    else:
        _left = _space//2
        _right = _space-_left
    return ' '*_left + _string + ' '*_right


class Painter:
    hard_map = {1:'Easy', 2:'Median', 3:'Medium', 4:'Memorize', 5:'Taste'}
    def paint_problem(self, p):
        print("%d. %s" % (p.no, p.title))
        print("Difficult: [%s]" % (self.hard_map[p.hard]))
        if p.total_commit == 0:
            if p.total_passed == 0:
                print("Passed: 0/0 (100%)")
            else:
                print("Passed: 0/%d (0%)" % (p.total_commit))
        else:
            print("Passed: %d/%d (%.0f%%)" % (p.total_passed, p.total_commit, p.total_passed/float(p.total_commit)*100))
        print("%s\n" % (p.text))
    def paint_problem_line(self, p):
        print("%d. %s %s" % (p.no, my_align(p.title, 35), my_align('[' + self.hard_map[p.hard] + ']', 12)) , end='') 
        #print("%d. %s %s [%s] %s" % (p.no, p.title, chr(12288)*(35 - len(p.title)), self.hard_map[p.hard], chr(12288)*(11 - len(self.hard_map[p.hard]))),  end='')
        if p.total_commit == 0:
            if p.total_passed == 0:
                print("Passed: 0/0 100%")
            else:
                print("Passed: 0/%d 0%" % (p.total_commit))
        else:
            print("Passed: %d/%d %.0f%%" % (p.total_passed, p.total_commit, p.total_passed/float(p.total_commit)*100))

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
