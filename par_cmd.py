#/usr/bin/env python

import parallel, time, os, sys, getopt, optparse

class par_cmd:

    def status(self):
        par = parallel.Parallel()
        value = par.getInSelected()
	return value

    def ex_cmd(self, cmd):
        # denne funksjonen kan byttes ut med 'subprocesses'
        os.popen(cmd)

    def chg_status(self, command):
        x = 1
        while x == 1:
            t = time.time()
            st_chg = False
            while time.time() <= t + 2:
                if self.status() == False:
                    st_chg = True
                time.sleep(0.1)
            if st_chg == True:
                self.ex_cmd(command)

p_c = par_cmd()

# User Interface
def main():
    p = optparse.OptionParser()
    p.add_option('-c','--command',action='store',help='Command witch will be executed')
    option, args = p.parse_args()

    if len(sys.argv) == 1:
        p.error('\nNo options passed. \n-h[--help] for usage')
    else:
        p_c.chg_status(option.command)



if __name__ == "__main__":
    main()
