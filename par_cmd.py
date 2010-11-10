#/usr/bin/env python

import parallel, time, os, sys, optparse

class par_cmd:

    def status(self):
        par = parallel.Parallel()
        value = par.getInSelected()
	return value

    def ex_cmd(self, cmd):
        # denne funksjonen kan byttes ut med 'subprocesses'
        os.popen(cmd)

    def chg_status(self, command):
        lasttime = time.time()
        while 1:
            if self.status() == False:
                if lasttime > time.time() + 2:
                    lasttime = time.time()
                    self.ex_cmd(command)
                else:
                    lasttime = time.time()
            time.sleep(0.1)

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
