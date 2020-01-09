
import os
import subprocess
import time

class Runner:
    def __init__(self, exe, no):
        self.exe_file = exe
        self.problem_no = no

        self.case_map = {99 : {1 : {"in" : "a a b b", "out" : "4"}}, no :{}}
        case_co = 0
        if False:
            self.file_path = "./case/" + str(no) + "/"
            #os.chdir(self.file_path)
            print('Converting:', self.file_path)
            for fd in os.listdir(self.file_path):
                tmp = fd.split('_')
                if len(tmp) != 2 or not tmp[1].isdigit():
                    continue
                if int(tmp[1]) not in self.case_map[no]:
                    case_co += 1
                    self.case_map[no][int(tmp[1])] = {'no' : case_co}
                keys = ''
                if fd.startswith('in'):
                    keys = 'in'
                    #self.case_map[no][int(tmp[1])][keys] = self.file_path + fd
                elif fd.startswith('out'):
                    keys = 'out'
                with open(self.file_path + fd, 'r') as fp:
                    self.case_map[no][int(tmp[1])][keys] = fp.read()
        else:
            self.file_path = "./case/" + str(no) + ".data"
            print('Converting:', self.file_path)
            with open(self.file_path, 'r') as fp:
                for case in fp.readlines():
                    tmp = case.split('|')
                    if len(tmp) != 2:
                        continue
                    case_co += 1
                    self.case_map[no][case_co] = {'no' : case_co}
                    self.case_map[no][case_co]['in'] = tmp[0].replace(',', '\n')
                    self.case_map[no][case_co]['out'] = tmp[1].strip()
        self.case_co = case_co
        #print(self.case_map)

    
    def run_and_record(self):
        no = self.problem_no
        if no not in self.case_map:
            print("Not find output of ", no)
        else:
            s = time.clock()
            for k, v in self.case_map[no].items():
                #print("run_and_record test case", k, v)
                if 'in' in v and 'out' in v and 'no' in v:
                    try:
                        p = subprocess.run([self.exe_file], stdout=subprocess.PIPE, input= v['in'], encoding='ascii', timeout=3)
                        #print('ret:', p.returncode)
                        if p.returncode != 0:
                            print('=== BAD MAIN RETURN VALUE (CASE AT %d/%d) ===' %(v['no'], self.case_co))
                            return False
                        if p.stdout.strip() != v['out'].strip():
                            print('=== WRONG ANSWER (CASE AT %d/%d) ===\nInput:%s\nExpect:%s\nActual:%s\n' \
                                % (v['no'], self.case_co, v['in'].strip(), v['out'].strip(), p.stdout.strip()))
                            return False
                    except subprocess.TimeoutExpired:
                        print('=== TIME LIMIT EXPIRED 3s (CASE AT %d/%d) ===\nInput:%s\nExpect:%s\nTimeout!' \
                                % (v['no'], self.case_co, v['in'].strip(), v['out'].strip()))
                        return False
                else:
                    print('=== BAD CASE K/V ===', k, v)
                    return False
            e = time.clock()
            print('=== PASSED ( %d/%d CASES ) %d ms ===' % (self.case_co, self.case_co, (e - s)*1000 ))
            return True
                    

