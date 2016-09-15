#!/usr/bin/env python3
#  coding: utf-8

# georush: Simple parallel GeoIP resolver
import sys
import os.path 
import threading
import subprocess


geoip       = "geoiplookup"
arpa_subfix = ".in-addr.arpa"
n_threads   = 10
threads     = []

instructions ="""dnsrush: Parallel DNS resolver.
usage:  georush.py <domain> ... """
lock  = threading.Lock()

# --lock and sanity check ---
def get_dnsquery():
    lock.acquire()
    result={'raw':'', 'filtered':''}
    if len(query_buffer) < 1: result = False
    else: 
        result['raw'] = result['filtered'] = query_buffer.pop().split()[0]
        if result['raw'][-13:] == arpa_subfix:result['filtered'] = result['raw'][:-13]
    lock.release()
    return result

#--- DNS Query helper ------
class Resolver(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__ (self)
        
    def run(self):
        query = get_dnsquery()
        while query:
            print (query['raw']," - ",subprocess.getoutput(geoip+" "+query['filtered']))
            query = get_dnsquery()

            
# --- Main Thread ---
def rushrun():
    for i in range(n_threads):
        dns_helper = Resolver()
        threads.append(dns_helper)
        threads[i].setName(i)
        threads[i].start()
    for i in threads: i.join()

if __name__ == '__main__':

#--- Arg parser ---    
    cmd_args = sys.argv[1:]
    if len(cmd_args) < 1: 
        print (instructions)
        sys.exit()
    else:
        query_buffer = cmd_args
        rushrun()



