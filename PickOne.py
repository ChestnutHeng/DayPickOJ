import sys
import os

from lib.DataModule import DataModule, Problem
from lib.DataTools import Locker,Painter
from lib.Runner import Runner

class Commander:
    def __init__(self):
        self.data = DataModule()
        self.painter = Painter()
        self.data.InitDB()
        self.data.CatchAll()
        self.locker = Locker("_pick_lock")
        self.now_locker = Locker("_lock_no")
        self.history = []
    
    def cmd_helper(self):
        print("./python PickOne.py [cmd]")
        print("pick                 --- choose a random problem")
        print("index                --- show index")
        print("choose [NO]          --- choose a problem from index")
        print("submit [FILE]        --- submit now problem")
        print("quit                 --- lose now problem")
        print("add                  --- add problem")

    def pick(self):
        if self.locker.acquire():
            try:
                while True:
                    # pick and paint
                    ans = self.data.Pick()
                    if not ans:
                        print('That\'s all problems !')
                    self.painter.paint_problem(ans)

                    # parse input
                    says = input('Enter [YES/Y] to choose:')
                    if says in ['yes', 'y', 'Y', 'YES']:
                        self.now_locker.acquire_store(str(ans.no))
                        break
                    elif says in ['q', 'quit', 'exit', 'Q']:
                        self.locker.release()
                        break
                    elif self.data.IsPicked(says):
                        print('Pick the problem : index ' + says)
            except BaseException as e:
                print(e)
                self.locker.release()
        else:
            no, ok = self.now_locker.acquire_read()
            print("You have choose a problem %s . submit it!" % no)
    
    def index(self):
        for v in self.data.problems:
            self.painter.paint_problem_line(v)
        self.choose()
    
    def choose(self, says=''):
        if self.locker.acquire():
            try:
                while True:
                    if says == '':
                        says = input('Enter [Index] to choose:').strip()
                    elif says in ['q', 'quit', 'exit', 'Q']:
                        self.locker.release()
                        return
                    elif says.isdigit():
                        v = self.data.CatchNo(int(says))
                        self.now_locker.acquire_store(str(v.no))
                        self.painter.paint_problem(v)
                        return
                    elif not says.isdigit():
                        print('Please enter a index number!')
                        says = ''
            except BaseException as e:
                print(e)
                self.locker.release()
        else:
            no, ok = self.now_locker.acquire_read()
            print("You have choose a problem %s . submit it!" % no)
            v = self.data.CatchNo(int(no))
            self.painter.paint_problem(v)
    
    def submit(self, exe):
        no, ok = self.now_locker.acquire_read()
        if ok:
            r = Runner(exe, int(no))
            if r.run_and_record():
                self.data.PassCommit(no)
                self.now_locker.release()
                self.locker.release()
            else:
                self.data.NopeCommit(no)
        else:
            print("Please pick a problem first.")
            self.pick()

    def quit(self):
        self.now_locker.release()
        self.locker.release()

    def add(self):
        p = Problem()
        print('Insert a problem.')
        p.no = 0
        while p.no == 0:
            num = input('Number: ')
            if num.isdigit():
                p.no = int(num)
        p.hard = 0
        while not (p.hard >= 1 and p.hard <= 5):
            hard = input('Is it hard? [1-3], [4] memorise, [5] little try: ')
            if hard.isdigit():
                p.hard = int(hard)
        while not p.title:
            p.title = input('Title: ')
        while not p.text:
            p.text = input('Description: ')
        self.data.InsertProblem(p)
        print('Insert sunccess !')

    def parse_cmd(self):
        if len(sys.argv) < 2:
            self.cmd_helper()
            return
        if sys.argv[1] not in ['pick', 'submit', 'quit', 'add', 'index', 'choose']:
            self.cmd_helper()
            return
        if sys.argv[1] == 'pick':
            self.pick()
        elif sys.argv[1] == 'submit':
            if len(sys.argv) == 3:
                self.submit(sys.argv[2])
            else:
                self.cmd_helper()
        elif sys.argv[1] == 'quit':
            self.quit()
        elif sys.argv[1] == 'add':
            self.add()
        elif sys.argv[1] == 'index':
            self.index()
        elif sys.argv[1] == 'choose':
            if len(sys.argv) == 3:
                self.choose(sys.argv[2])
            elif len(sys.argv) == 2:
                self.choose()
    def wait(self):
        self.parse_cmd()

if __name__ == "__main__":
    d = Commander()
    d.wait()