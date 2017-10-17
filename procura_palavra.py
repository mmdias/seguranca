#!/usr/bin/env python3.4
def main():	

#	f = open(filename , 'wb')
	for  i in range(1,2):
		filename = "%s" % i
		with open(filename,"r" ) as file_d:
			for line in file_d:
				line = line.strip()			
				if line.find( "115 101 120 116 111" )!= -1:#  Procura a palavra "sexto" 
						print(i)
				else: print("a")
main()
