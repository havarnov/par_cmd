#/usr/bin/env python

import parallel, time, os

class par_cmd:

    def status(self):
        self.p = parallel.Parallel()
        return self.p.getInSelected()

    def ex_cmd(self, cmd):
        # denne funksjonen kan byttes ut med 'subprocesses'
        os.popen(cmd)

    def chg_status(self, command):
        x = 1
        while x == 1:
            t = time.time()
            st_chg == False
            while t <= t + 2:
                if self.status() == True:
                    st_chg == True
                time.sleep(0.1)
            if st_chg == True:
                self.ex_cmd(command)

