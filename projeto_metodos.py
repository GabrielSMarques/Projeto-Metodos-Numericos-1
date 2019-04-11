from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_application)
from sympy import *

y, t = symbols("y t")

saida = open("saida.txt", "w")

def euler(y0, t0, h, qtd, expr, printar):
	yn = y0
	tn = t0
	u = [0]
	if printar == true:
		saida.write("Metodo de Euler\n")
		saida.write("y(" + str(tn) + ") = " + str(yn) + "\n")
		saida.write("h = " + str(h) + "\n")
		saida.write("0 " + str(yn) + "\n")
	for x in range(1, qtd+1):
		yn1 = yn + h*expr.subs([(t, tn), (y, yn)])
		yn = yn1
		tn += h
		if printar == true:
			saida.write(str(x) + " " + str(yn1) + "\n")
		u.insert(x, yn1)
	return u

def euler_inverso(y0, t0, h, qtd, expr, printar):
	yn = y0
	tn = t0
	u = [0]
	if printar == true:
		saida.write("Metodo de Euler Inverso\n")
		saida.write("y(" + str(tn) + ") = " + str(yn) + "\n")
		saida.write("h = " + str(h) + "\n")
		saida.write("0 " + str(yn) + "\n")
	for x in range(1, qtd+1):
		tn1 = tn + h
		yn1 = yn + h*expr.subs([(t, tn), (y, yn)])
		yn1 = yn + h*expr.subs([(t, tn1), (y, yn1)])
		yn = yn1
		tn += h
		if printar == true:
			saida.write(str(x) + " " + str(yn1) + "\n")
		u.insert(x, yn)
	return u

def euler_aprimorado(y0, t0, h, qtd, expr, printar):
	yn = y0
	tn = t0
	u = [0]
	if printar == true:
		saida.write("Metodo de Euler Aprimorado\n")
		saida.write("y(" + str(tn) + ") = " + str(yn) + "\n")
		saida.write("h = " + str(h) + "\n")
		saida.write("0 " + str(yn) + "\n")
	for x in range(1, qtd+1):
		tn1 = tn + h
		yn1 = yn + h*expr.subs([(t, tn), (y, yn)])
		yn1 = yn + h*(expr.subs([(t, tn1), (y, yn1)]) + expr.subs([(t, tn), (y, yn)]))/2
		yn = yn1
		tn += h
		if printar == true:
			saida.write(str(x) + " " + str(yn1) + "\n")
		u.insert(x, yn)
	return u

def runge_kutta(y0, t0, h, qtd, expr, printar):
	yn = y0
	tn = t0
	u = [0]
	if printar == true:
		saida.write("Metodo de Runge-Kutta\n")
		saida.write("y(" + str(tn) + ") = " + str(yn) + "\n")
		saida.write("h = " + str(h) + "\n")
		saida.write("0 " + str(yn) + "\n")
	for x in range(1, qtd+1):
		k1 = expr.subs([(t, tn), (y, yn)])
		k2 = expr.subs([(t, tn + h/2), (y, yn + (h*k1)/2)])
		k3 = expr.subs([(t, tn + h/2), (y, yn + (h*k2)/2)])
		k4 = expr.subs([(t, tn + h), (y, yn + h*k3)])
		yn1 = yn + h*(k1 + 2*k2 + 2*k3 + k4)/6
		yn = yn1
		tn += h
		if printar == true:
			saida.write(str(x) + " " + str(yn1) + "\n")
		u.insert(x, yn)
	return u

def getValorInicial(valorInicial, y0, t0, h, expr, qtd):
	u = [0]
	if valorInicial == "euler":
		u = euler(y0, t0, h, qtd - 1, expr, false)
	elif valorInicial == "euler_inverso":
		u = euler_inverso(y0, t0, h, qtd - 1, expr, false)
	elif valorInicial == "euler_aprimorado":
		u = euler_aprimorado(y0, t0, h, qtd - 1, expr, false)
	elif valorInicial == "runge_kutta":
		u = runge_kutta(y0, t0, h, qtd - 1, expr, false)

	return u

def adam_bashforth(y0, t0, h, qtd, expr, ordem, metodoInicial, valorInicial):
	yn = y0	
	tn = t0

	u = [0]

	if metodoInicial == true:
		if valorInicial == "euler":
			saida.write("Metodo Adam-Bashforth por Euler ( ordem = " + str(ordem) + " )\n")
		elif valorInicial == "euler_inverso":
			saida.write("Metodo Adam-Bashforth por Euler Inverso ( ordem = "+ str(ordem) +" )\n")
		elif valorInicial == "euler_aprimorado":
			saida.write("Metodo Adam-Bashforth por Euler Aprimorado ( ordem = " + str(ordem) + " )\n")
		elif valorInicial == "runge_kutta":
			saida.write("Metodo Adam-Bashforth por Runge-Kutta ( ordem = " + str(ordem) + " )\n")

		u = getValorInicial(valorInicial, yn, tn, h, expr, ordem)
	else:
		saida.write("Metodo Adam-Bashforth ( ordem = " + str(ordem) + " )\n")
		u = lista

	saida.write("y(" + str(tn) + ") = " + str(yn) + "\n")
	saida.write("h = " + str(h) + "\n")
	saida.write("0 " + str(yn) + "\n")

	for x in range(1, len(u)):
		saida.write(str(x) + " " + str(u[x]) + "\n")

	for x in range(ordem, qtd+1):
		if ordem == 2:
			yn1 = u[1] + (3/2)*h*expr.subs([(t, tn + h), (y, u[1])]) + (-1/2)*h*expr.subs([(t, tn), (y, yn)])
		elif ordem == 3:
			yn1 = u[2] + (23/12)*h*expr.subs([(t, tn + 2*h), (y, u[2])]) + (-4/3)*h*expr.subs([(t, tn + h), (y, u[1])]) + (5/12)*h*expr.subs([(t, tn), (y, yn)])
		elif ordem == 4:
			yn1 = u[3] + (55/24)*h*expr.subs([(t, tn + 3*h), (y, u[3])]) + (-59/24)*h*expr.subs([(t, tn + 2*h), (y, u[2])])+ (37/24)*h*expr.subs([(t, tn + h), (y, u[1])]) + (-3/8)*h*expr.subs([(t, tn), (y, yn)])
		elif ordem == 5:
			yn1 = u[4] + (1901/720)*h*expr.subs([(t, tn + 4*h), (y, u[4])]) + (-1387/360)*h*expr.subs([(t, tn + 3*h), (y, u[3])]) + (109/30)*h*expr.subs([(t, tn + 2*h), (y, u[2])]) + (-637/360)*h*expr.subs([(t, tn + h), (y, u[1])]) + (251/720)*h*expr.subs([(t, tn), (y, yn)])
		elif ordem == 6:
			yn1 = u[5] + (4277/1440)*h*expr.subs([(t, tn + 5*h), (y, u[5])]) + (-2641/480)*h*expr.subs([(t, tn + 4*h), (y, u[4])]) + (4991/720)*h*expr.subs([(t, tn + 3*h), (y, u[3])]) + (-3649/720)*h*expr.subs([(t, tn + 2*h), (y, u[2])]) + (959/480)*h*expr.subs([(t, tn + h), (y, u[1])]) + (-95/288)*h*expr.subs([(t, tn), (y, yn)])
		elif ordem == 7:
			yn1 = u[6] + (198721/60480)*h*expr.subs([(t, tn + 6*h), (y, u[6])]) + (-18637/2520)*h*expr.subs([(t, tn + 5*h), (y, u[5])]) + (235183/20160)*h*expr.subs([(t, tn + 4*h), (y, u[4])]) + (10754/945)*h*expr.subs([(t, tn + 3*h), (y, u[3])]) + (135713/20160)*h*expr.subs([(t, tn + 2*h), (y, u[2])]) + (-5603/2520)*h*expr.subs([(t, tn + h), (y, u[1])]) + (19087/60480)*h*expr.subs([(t, tn), (y, yn)])
		elif ordem == 8:
			yn1 = u[7] + (16083/4480)*h*expr.subs([(t, tn + 7*h), (y, u[7])]) + (-1152169/120960)*h*expr.subs([(t, tn + 6*h), (y, u[6])]) + (242653/13440)*h*expr.subs([(t, tn + 5*h), (y, u[5])]) + (-296053/13440)*h*expr.subs([(t, tn + 4*h), (y, u[4])]) + (2102243/120960)*h*expr.subs([(t, tn + 3*h), (y, u[3])]) + (-115747/13440)*h*expr.subs([(t, tn + 2*h), (y, u[2])]) + (32863/13440)*h*expr.subs([(t, tn + h), (y, u[1])]) + (-5257/17280)*h*expr.subs([(t, tn), (y, yn)])
		yn = u[1]
		for i in range(1, ordem-1):
			u[i] = u[i+1]
		u[ordem - 1] = yn1
		tn += h
		saida.write(str(x) + " " + str(yn1) + "\n")	
			
	return u

def adam_multon(y0, t0, h, qtd, expr, ordem, metodoInicial, valorInicial):
	yn = y0
	tn = t0

	u = [0]

	if metodoInicial == true:
		if valorInicial == "euler":
			saida.write("Metodo Adam-Multon por Euler ( ordem = " + str(ordem) + " )\n")
		elif valorInicial == "euler_inverso":
			saida.write("Metodo Adam-Multon por Euler Inverso ( ordem = "+ str(ordem) +" )\n")
		elif valorInicial == "euler_aprimorado":
			saida.write("Metodo Adam-Multon por Euler Aprimorado ( ordem = " + str(ordem) + " )\n")
		elif valorInicial == "runge_kutta":
			saida.write("Metodo Adam-Multon por Runge-Kutta ( ordem = " + str(ordem) + " )\n")

		u = getValorInicial(valorInicial, yn, tn, h, expr, ordem+1)
	else:
		saida.write("Metodo Adam-Multon ( ordem = " + str(ordem) + " )\n")
		u = lista
		u.insert(ordem, getValorInicial("runge_kutta", u[ordem-1], tn + (ordem-1)*h, h, expr, 2)[1])

	saida.write("y(" + str(tn) + ") = " + str(yn) + "\n")
	saida.write("h = " + str(h) + "\n")
	saida.write("0 " + str(yn) + "\n")

	for x in range(1, len(u)-1):
		saida.write(str(x) + " " + str(u[x]) + "\n")

	for x in range(ordem, qtd+1):
		if ordem - 1 == 1:
			yn1 = u[1] + (1/2)*h*u[2] + (1/2)*h*expr.subs([(t, tn), (y, u[1])])
		elif ordem - 1 == 2:
			yn1 = u[2] + (5/12)*h*u[3] + (2/3)*h*expr.subs([(t, tn + 2*h), (y, u[2])]) + (-1/12)*h*expr.subs([(t, tn + h), (y, u[1])])
		elif ordem - 1 == 3:
			yn1 = u[3] + (3/8)*h*u[4] + (19/24)*h*expr.subs([(t, tn + 3*h), (y, u[3])])+ (-5/24)*h*expr.subs([(t, tn + 2*h), (y, u[2])]) + (1/24)*h*expr.subs([(t, tn + h), (y, u[1])])
		elif ordem - 1 == 4:
			yn1 = u[4] + (251/720)*h*u[5] + (323/360)*h*expr.subs([(t, tn + 4*h), (y, u[4])]) + (-11/30)*h*expr.subs([(t, tn + 3*h), (y, u[3])]) + (53/360)*h*expr.subs([(t, tn + 2*h), (y, u[2])]) + (-19/720)*h*expr.subs([(t, tn + h), (y, u[1])])
		elif ordem - 1 == 5:
			yn1 = u[5] + (95/288)*h*u[6] + (1427/1440)*h*expr.subs([(t, tn + 5*h), (y, u[5])]) + (-133/240)*h*expr.subs([(t, tn + 4*h), (y, u[4])]) + (241/720)*h*expr.subs([(t, tn + 3*h), (y, u[3])]) + (-173/1440)*h*expr.subs([(t, tn + 2*h), (y, u[2])]) + (3/160)*h*expr.subs([(t, tn + h), (y, u[1])])
		elif ordem - 1 == 6:
			yn1 = u[6] + (19087/60480)*h*u[7] + (2713/2520)*h*expr.subs([(t, tn + 6*h), (y, u[6])]) + (-15487/20160)*h*expr.subs([(t, tn + 5*h), (y, u[5])]) + (586/945)*h*expr.subs([(t, tn + 4*h), (y, u[4])]) + (-6737/20160)*h*expr.subs([(t, tn + 3*h), (y, u[3])]) + (263/2520)*h*expr.subs([(t, tn + 2*h), (y, u[2])]) + (-863/60480)*h*expr.subs([(t, tn + h), (y, u[1])])
		elif ordem - 1 == 7:
			yn1 = u[7] + (5257/17280)*h*u[8] + (139849/120960)*h*expr.subs([(t, tn + 7*h), (y, u[7])]) + (-4511/4480)*h*expr.subs([(t, tn + 6*h), (y, u[6])]) + (123133/120960)*h*expr.subs([(t, tn + 5*h), (y, u[5])]) + (-88547/120960)*h*expr.subs([(t, tn + 4*h), (y, u[4])]) + (1537/4480)*h*expr.subs([(t, tn + 3*h), (y, u[3])]) + (-11351/120960)*h*expr.subs([(t, tn + 2*h), (y, u[2])]) + (275/24192)*h*expr.subs([(t, tn + h), (y, u[1])])

		yn = u[1]
		for i in range(1, ordem - 1):
			u[i] = u[i+1]
		u[ordem - 1] = yn1
		tn += h
		u[ordem] = getValorInicial(valorInicial, yn1, tn + ordem*h, h, expr, 2)[1]

		saida.write(str(x) + " " + str(yn1) + "\n")
	return

def formula_inversa(y0, t0, h, qtd, expr, ordem, metodoInicial, valorInicial):
	yn = y0	
	tn = t0

	u = [0]

	if metodoInicial == true:
		if valorInicial == "euler":
			saida.write("Metodo Formula Inversa de Diferenciacao por Euler ( ordem = " + str(ordem) + " )\n")
		elif valorInicial == "euler_inverso":
			saida.write("Metodo Formula Inversa de Diferenciacao por Euler Inverso ( ordem = "+ str(ordem) +" )\n")
		elif valorInicial == "euler_aprimorado":
			saida.write("Metodo Formula Inversa de Diferenciacao por Euler Aprimorado ( ordem = " + str(ordem) + " )\n")
		elif valorInicial == "runge_kutta":
			saida.write("Metodo Formula Inversa de Diferenciacao por Runge-Kutta ( ordem = " + str(ordem) + " )\n")

		u = getValorInicial(valorInicial, yn, tn, h, expr, ordem+1)
	else:
		saida.write("Metodo Formula Inversa de Diferenciacao ( ordem = " + str(ordem) + " )\n")
		u = lista
		u.insert(ordem, getValorInicial("runge_kutta", u[ordem-1], tn + (ordem-1)*h, h, expr, 2)[1])

	saida.write("y(" + str(tn) + ") = " + str(yn) + "\n")
	saida.write("h = " + str(h) + "\n")
	saida.write("0 " + str(yn) + "\n")

	for x in range(1, len(u)-1):
		saida.write(str(x) + " " + str(u[x]) + "\n")

	for x in range(ordem, qtd+1):
		if ordem == 2:
			yn1 = (2/3)*h*expr.subs([(t, tn + 2*h), (y, u[2])]) + (4/3)*u[1] - (1/3)*yn
		elif ordem == 3:
			yn1 = (6/11)*h*expr.subs([(t, tn + 3*h), (y, u[3])]) + (18/11)*u[2] - (9/11)*u[1] + (2/11)*yn
		elif ordem == 4:
			yn1 = (12/25)*h*expr.subs([(t, tn + 4*h), (y, u[4])]) + (48/25)*u[3] - (36/25)*u[2] + (16/25)*u[1] - (3/25)*yn
		elif ordem == 5:
			yn1 = (60/137)*h*expr.subs([(t, tn + 5*h), (y, u[5])]) + (300/137)*u[4] - (300/137)*u[3] + (200/137)*u[2] - (75/137)*u[1] + (12/137)*yn
		elif ordem == 6:
			yn1 = (60/147)*h*expr.subs([(t, tn + 6*h), (y, u[6])]) + (360/147)*u[5] - (450/147)*u[4] + (400/147)*u[3] - (225/147)*u[2] + (72/147)*u[1] - (10/147)*yn
		
		yn = u[1]
		for i in range(1, ordem -1):
			u[i] = u[i+1]
		u[ordem - 1] = yn1
		tn += h
		if metodoInicial == true:
			u[ordem] = getValorInicial(valorInicial, yn1, tn + ordem*h, h, expr, 2)[1]
		else:
			u[ordem] = getValorInicial("runge_kutta", yn1, tn + ordem*h, h, expr, 2)[1]
		saida.write(str(x) + " " + str(yn1) + "\n")	
			
	return

entrada = open("entrada.txt", "r")
saida.write("///\n")
if entrada.mode == 'r':
	contents=entrada.readlines()
	transformations = standard_transformations + (implicit_application,)
	for index, line in enumerate(contents):
		if index != 0 and index != len(contents)-1:
			comando = (line.split('\n')[0]).split(' ')

			metodo = comando[0].split("_by_")

			if metodo[0] == "adam_bashforth" or metodo[0] == "adam_multon" or metodo[0] == "formula_inversa":
				y0 = float(comando[1])
				ordem = int(comando[len(comando)-1])
				
				if len(metodo) > 1:
					t0 = float(comando[2])
					h = float(comando[3])
					qtd = int(comando[4])
					func = comando[5]
					expr = parse_expr(func, transformations=transformations)

					if metodo[0] == "adam_bashforth":
						adam_bashforth(y0, t0, h, qtd, expr, ordem, true, metodo[1])
					elif metodo[0] == "adam_multon":
						adam_multon(y0, t0, h, qtd, expr, ordem, true, metodo[1])
					else:
						formula_inversa(y0, t0, h, qtd, expr, ordem, true, metodo[1])
				else:
					lista = [0]
					for i in range(1, ordem):
						lista.insert(i, float(comando[i+1]))

					t0 = float(comando[ordem + 1])
					h = float(comando[ordem + 2])
					qtd = int(comando[ordem + 3])
					func = comando[ordem + 4]
					expr = parse_expr(func, transformations=transformations)

					if metodo[0] == "adam_bashforth":
						adam_bashforth(y0, t0, h, qtd, expr, ordem, false, lista)
					elif metodo[0] == "adam_multon":
						adam_multon(y0, t0, h, qtd, expr, ordem, false, lista)
					else:
						formula_inversa(y0, t0, h, qtd, expr, ordem, false, lista)
			else:
				y0 = float(comando[1])
				t0 = float(comando[2])
				h = float(comando[3])
				qtd = int(comando[4])
				func = comando[5]
				expr = parse_expr(func, transformations=transformations)

				if metodo[0] == "euler":
					euler(y0, t0, h, qtd, expr, true)
				elif metodo[0] == "euler_inverso":
					euler_inverso(y0, t0, h, qtd, expr, true)
				elif metodo[0] == "euler_aprimorado":
					euler_aprimorado(y0, t0, h, qtd, expr, true)
				elif metodo[0] == "runge_kutta":
					runge_kutta(y0, t0, h, qtd, expr, true)

			if index < len(contents)-2:
				saida.write("\n")
saida.write("///\n")
saida.close()
