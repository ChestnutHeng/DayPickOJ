#encoding=utf8

import sqlite3
import random
import json

class Problem:
    no = 0
    hard = 0
    title = ""
    text = ""
    total_commit = 0
    total_passed = 0
    def __init__(self, no, hard, title, text, total_commit, total_passed):
        self.no = no
        self.hard = hard
        self.title = title
        self.text = text
        self.total_commit = total_commit
        self.total_passed = total_passed

    def __repr__(self):
        return json.dumps(self.__dict__)


class DataModule:
    conn = None
    problems = []
    shows = []
    def __init__(self):
        self.conn = sqlite3.connect('./lock/master.db')
    def InitDB(self):
        self.conn = sqlite3.connect('./lock/master.db')
        cursor = self.conn.cursor()
        sql = """create table if not exists `problems` (
            `id` INTEGER PRIMARY KEY AUTOINCREMENT,
            `no` INT NOT NULL DEFAULT '0' UNIQUE, --COMMENT '题号'
            `hard` TINYINT NOT NULL DEFAULT '0', --COMMENT '1简单 2中等 3困难 4精通 5尝试',
            `title` VARCHAR(100) NOT NULL DEFAULT '', -- COMMENT '题目标题',
            `text` TEXT NOT NULL, -- COMMENT '题目描述',
            `total_commit` INT NOT NULL DEFAULT '0', -- '提交次数',
            `total_passed` INT NOT NULL DEFAULT '0' -- COMMENT '通过次数'
        )"""
        #print(sql)
        cursor.execute(sql)
        cursor.close()
    
    def CatchAll(self):
        problems = []
        cursor = self.conn.cursor()
        sql = '''select no, hard, title, text, total_commit, total_passed from problems'''
        #print(sql)
        cursor.execute(sql)
        for row in cursor:
            if len(row) != 6:
                continue
            problems.append(Problem(*row))
        if problems:
            self.problems = problems
        cursor.close()
    
    def Pick(self):
        if not self.problems:
            return None
        ans = random.choice(self.problems)
        self.problems.remove(ans)
        self.shows.append(ans)
        return ans
    
    def IsPicked(self, word):
        return word in self.shows
    
    def NopeCommit(self, no):
        cursor = self.conn.cursor()
        sql = '''update problems set total_commit=total_commit+1 where no=''' + str(no)
        cursor.execute(sql)
        self.conn.commit()
        print(sql)
        cursor.close()
    
    def PassCommit(self, no):
        cursor = self.conn.cursor()
        sql = '''update problems set total_commit=total_commit+1, total_passed=total_passed+1 where no=''' + str(no)
        print(sql)
        cursor.execute(sql)
        self.conn.commit()
        cursor.close()



if __name__ == "__main__":
    d = DataModule()
    d.InitDB()
    d.CatchAll()
    print(d.Pick())
