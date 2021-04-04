from argparse import ArgumentParser
from ultrascanner import NetworkScannerThread,PortScanner

parser = ArgumentParser(description="UltraScanner Build in python  ",epilog="""This is a description usage
    python main.py -I 192.168.1.1/24 -S 1 -L 200 OR python main.py -H 192.168.1.100""")

req_parser = parser.add_argument_group('Required Argument')

req_parser.add_argument('-H','--host',dest='host',type=str,help="specify host ip address")
req_parser.add_argument('-I','--subnetip',dest='subnetip',type=str,help="specify subnetip address")
req_parser.add_argument('-S','--start',dest='start',type=int,help="enter the starting number  ")
req_parser.add_argument('-L','--last',dest='last',type=int,help="enter the last number  ")
req_parser.add_argument('-t','--thread',dest='thread',type=int,help="enter number of thread ")



args= parser.parse_args()
subnetip = args.subnetip
start = args.start
last = args.last
host = args.host
threads = args.thread
print(subnetip,start,last,host)

if subnetip and start and last and threads:
	n = NetworkScannerThread(subnetip,start,last,threads)
	n.main()
elif subnetip and start and last:
	n = NetworkScannerThread(subnetip,start,last)
	n.main()
elif host and threads:
	p = PortScanner(host,threads)
	p.main()
elif host:
	p = PortScanner(host)
	p.main()

else:
	print('This is a description usage python ultrascanner.py -I 192.168.1.1/24 -S 1 -L 200 OR python ultrascanner.py -H 192.168.1.100')


