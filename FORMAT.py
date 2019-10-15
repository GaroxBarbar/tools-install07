import os, sys

print ("\033[31;1mANDA HARUS LOGIN TERLEBIH DAHULU:)")
print ("\033[1;31;1mNGGAK TAHU?SILAHKAN CHATTING TUANG4ROX 089510474520")
username = 'GAROX155007'
password = 'MULUTANDAKOTOR'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("username : ")
	if uname == username:
		pwd = raw_input("password : ")

		if pwd == password:
			print "\n\033[1;34mSELAMAT DATANG DI TOOLS SAYA", 
			sys.exit()

		else:
			print "\n\033[1;36mANDA TIDAK TAHU TOLONG UNTUK SEGERA MENGHUBUNGI GAROX\033[00m"
			print "Back Login\n"
			restart()

	else:
		print "\n\033[1;36mANDA TIDAK TAHU TOLONG UNTUK SEGERA MENGHUBUNGI GAROX\033[00m"
		print "Back Login\n"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()

