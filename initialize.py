from collections import defaultdict
from collections.abc import MutableMapping
from typing import List
from task import Task
from readyqueue import ReadyQueue

class Initialize:
    task_num   : int            = 0
    total_time : int            = 0
    task       : List[Task]     = []
    rq         : ReadyQueue
    o_ui = {'A':'ð¥', 'B':'ð¦', 'C': 'ð¨','D':'ð©','E':'ðª','F':'â¬'}

    def __init__(self,time_quantum = 1, queue_size = 10) :
        self.parseInput()
        self.sortInput()
        self.setTotalTime()
        self.rq = ReadyQueue(queue_size)

    def parseInput(self):
        self.task_num = 0
        # [Item 3] Default input and output operations
        # involving file handles follows str types instead of raw bytes
        f = open("./input.txt", 'r')
        #> brì ì¬ì©íë©´ ìë©ëë¤.

        for line in f:
            ps = Task()
            x = line.split()
            ps.tsk_id = str(x[0])
            ps.ariv_t = int(x[1])
            ps.rema_t = int(x[2])
            ps.serv_t = int(x[2])
            ps.qlevel = 0
            ps.ticket = int(x[3])
            self.task.append(ps)
            self.task_num += 1
        f.close()
    
    def sortInput(self) :
        tmp : Task
        for i in range(self.task_num - 1, 0, -1) :
            for j in range(0, i) :
                if self.task[j].ariv_t > self.task[j].ariv_t :
                    tmp = self.task[j+1]
                    self.task[j+1] = self.task[j]
                    self.task[j] = tmp
                elif self.task[j].ariv_t == self.task[j+1].ariv_t and self.task[j].p_name > self.task[j+1].p_name :
                    tmp = self.task[j+1]
                    self.task[j+1] = self.task[j]
                    self.task[j] = tmp
    
    def setTotalTime(self) :
        sum : int = 0 
        for i in range(0, self.task_num) :
            sum += self.task[i].serv_t
        self.total_time = sum

    def setTimeQ(self, q : int) :
        for i in range(0,self.task_num) :
            self.task[i].time_q = q

    def printTask(self):
        # [Item Underscore] Use in loop
        for _ in self.task:
            print(_)
        #> ê°ì´ íììë ë£¨íìì ì¸ëì¤ì½ì´ë¥¼ ì¬ì©íììµëë¤.

    def print_UI(self, output):
        for id in self.task:
            id = id.tsk_id
            print(id+'â', end = '')
            # [Item 7] Prefer enumerate Over range
            for t, target in enumerate(output):
                if target == id:
                    # [Item 16] Prefer get over in and KeyError to Handle Missing Dictionary Keys
                    print(self.o_ui.get(id,'â¬'), end = '')
                    #> ëìëë¦¬ì ì ìëì´ ìë A,B,C,D,E ì´ì¸ì í¤ê°ì ì°¸ì¡°íë©´ ê²ììì ì¶ë ¥íê² íììµëë¤. 
                elif t>0 and (t) % 5 == 0:
                    print('%c' %'|', end=' ')
                else:
                    print('  ', end = '')
            #> for ë¬¸ìì index ê°ê³¼ ë°ë³µíìë¥¼ ëª¨ë ì¬ì©í´ì¼ íê¸° ëë¬¸ì enumerateë¥¼ ì¬ì©íììµëë¤.
            print()
        print('  ', end='')
        for i in range(self.total_time):
            print('ââ', end='')
        print()
        print("  0", end = '')
        for i in range (5, self.total_time+1, 5):
            print('%10d' %i, end='')
        print('\n')
        # [Item 4] The format built-in and str.format
        formatted = format(' '.join(map(str, output)), '<s')
        print("â¶ ",formatted, end='\n\n')
        #> formattingì ì¬ì©íì¬ ì¶ë ¥ì ì§ì íì¬ ì½ëë¥¼ ê°ë¨íê² íììµëë¤.


    # [Item 14] Sort by Complex Criteria using the key Parameter
    def sort_proc(self):
        _proc = []
        f = open("./input.txt", 'r')
        
        for line in f:
            x = line.split()
            _proc.append(str(x[0], int(x[1])))
        f.close()

        print('Unsorted:', repr(_proc))
        _proc.sort(key=lambda x: x.name)
        print('\nSorted: ', )
    #> process í´ëì¤ë¥¼ ì ì¸íì¬ íë¡ì¸ì¤ë¤ì ëì°©ìê°ì ë§ê² ì ë ¬íë í¨ìë¥¼ êµ¬ííììµëë¤. 

    def print_Serv(self):
        p_id = []
        p_serv = []
        f = open("./input.txt", 'r')
        for line in f:
            x = line.split()
            p_id.append(str(x[0]))
            p_serv.append(int(x[2]))
        f.close()
        # [Item 8] : Use zip to Process Iterators in Parallel
        proc_zip = zip(p_id, p_serv)
        for name, count in proc_zip:
            print(name + count)
        #> zipì íì©íì¬ ê° íë¡ì¸ì¤ì servicetimeì ì¶ë ¥íë í¨ìë¥¼ ìì±íììµëë¤. 

    def print_parsed(self):
        # [Item 13] Prefer Catch-All Unpacking Over Slicing
        proc_id, *rest = self.task
        print(f'Process {proc_id} : {rest}')
        # input.txtíì¼ë¡ë¶í° parseí taskì ë³´ë¥¼ process id ì ëë¨¸ì§ ì ë³´ë¡ ëëì´ íë²ì ì¶ë ¥í©ëë¤.

# [Item 18] Know How to Construct KeyDependent Default Values with
class SearchProc(dict):
    def __missing__(self, key):
        print('no match process exist!')
# Processëìëë¦¬ë¥¼ ì ë¬ë°ì process idì ë°ë¼ ì¡°íí  ë ë§ì½ í´ë¹íë íë¡ì¸ì¤ê° ìì¼ë©´ ìë¬ë©ìì§ë¥¼ ì¶ë ¥íë¤

class Proc:
    def __init__(self, name, ariv):
        self.name = name
        self.ariv = ariv

    def __repr__(self):
        return f'Tool({self.name!r}, {self.ariv})'

class proc_level:
    def __init__(self):
        # [Item 17] Prefer defaultdict over setdefault to Handle Missing Items in Internal State
        self.proc = defaultdict(int)
        # defaultdictì íµí´ í¤ì ëí ê°ì´ ìì¼ë©´ ê°ì 0ì¼ë¡ ì´ê¸°ííì¬ priority levelì ì¦ê°ìí¬ë  
        # ì¬ì ì processì priorityë¥¼ ë°ë¡ ì´ê¸°í íì§ ììë ì¬ì©í  ì ìëë¡ ì¤ì íììµëë¤. 
    def add(self, pname, priority):
        self.proc[pname].add(priority)

