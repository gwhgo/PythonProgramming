"""
spawn a child process/program, connect my stdin/stdout to child process's
stdout/stdin -- my reads and writes map to output and input streams of the 
spawned program; such like tying together streams with subprocess modules
"""

import os, sys

def spawn(prog, *args):
    stdinFd = sys.stdin.fileno()
    stdoutFd = sys.stdout.fileno()

    parentStdin, childStdout = os.pipe()
    childStdin, parentStdout  = os.pipe()

    pid = os.fork()
    if pid:
        os.close(childStdout)
        os.close(childStdin)
        os.dup2(parentStdin, stdinFd) # assings the parent process's stdin file to the input end of one of the two pieps created
        os.dup2(parentStdout,stdoutFd)
    else:
        os.close(parentStdin)
        os.close(parentStdout)
        os.dup2(childStdin, stdinFd)
        os.dup2(childStdout, stdoutFd)
        args = (prog,) + args
        os.execvp(prog, args)       # new program in this process
        assert False, 'execvp failed!'  

if __name__ == '__main__':
    mypid = os.getpid()
    spawn('python', 'pipes-testchild.py', 'spam') # fork child program

    print('Hello 1 from parent', mypid) # to child's stdin
    sys.stdout.flush()                  # subvert stdio buffering.
    reply = input()
    sys.stderr.write('Parent got: "%s"\n' % reply)  # stderr not tied to pipe
   
    print('Hello 2 from parent', mypid)
    sys.stdout.flush()
    reply = sys.stdin.readline()
    sys.stderr.write('Parent got: "%s"\n' % reply[:-1])
