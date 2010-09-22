#/usr/bin/env python

import parallel, time, os, sys, optparse

class par_cmd:

    def status(self):
        '''This function will return if the pin13 has value True or False'''
        par = parallel.Parallel()
        value = par.getInSelected()
	return value

    def ex_cmd(self, cmd):
        '''This function will execute the command it's taking as an argument.'''
        os.popen(cmd)

    def chg_status(self, command):
        '''This is the actual "watch pin13" function.'''
        x = 1
        while x == 1:
            st_chg = False
            t = time.time()
            while time.time() <= t + 2:
                if self.status() == False:
                    while self.status() == False:
                        pass
                    st_chg = True
                else:
                    t = time.time()
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
