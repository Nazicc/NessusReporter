# coding: utf-8

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

print """



███╗   ██╗███████╗███████╗███████╗██╗   ██╗███████╗
████╗  ██║██╔════╝██╔════╝██╔════╝██║   ██║██╔════╝
██╔██╗ ██║█████╗  ███████╗███████╗██║   ██║███████╗
██║╚██╗██║██╔══╝  ╚════██║╚════██║██║   ██║╚════██║
██║ ╚████║███████╗███████║███████║╚██████╔╝███████║
╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝
                                                   

SeyedHojjatHosseini@gmail.com
www.hojat.net

"""


filename = open(raw_input("Enter Filename:(Exm: nessus-scan.html) "),'r')
scanrange = input("What is your scan Range?(Exm: 172) ")
MainCheck=""
PerviewLine=""
sumip=0

for line in filename:
	if MainCheck == "":
		if "Vulnerabilities by Plugin" in line:
			MainCheck = line
			continue
	else:
		if "2. Medium" in line:
			continue
		if "Critical<div" in line:
			print "\nRisk is Critical\n"
		if "High<div" in line:
			print "\nRisk is High\n"
		if "Medium<div" in line:
			print "\nRisk is Medium\n"
		if "Low<div" in line:
			print "\nRisk is Low\n"
		if "None<div" in line:
			print "\nRisk is Information\n"
		if "host (" in line:
			continue
		if "URL" in line:
			continue
		if "scan :" in line:
			continue
		if "traceroute from" in line:
			continue
		if str(scanrange) in line:
			sumip+=1
			print find_between(line,">","<")
		if "Synopsis" in line:
			print "\n"
			print "Sum IP = " + str(sumip) + "\n"
			sumip=0
			print "\n*****************\n"
			print find_between(PerviewLine," - ","</")
			print "\n"			
	PerviewLine = line
print "Sum IP = " + str(sumip) + "\n"

filename.close()


