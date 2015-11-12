from sys import *

tokens = []
num_stack = []
symbols = {}

def open_file(filename):
	data = open(filename,"r").read()
	data += "<EOF>"
	return data


def lex(filecontents):
	filecontents = list(filecontents)
	tok = ""
	state = 0
	isexpr = 0
	varStarted = 0
	polStarted = 0
	termStarted = 0
	polCounter = 0
	function = 0
	negative = 0
	error = 0
	eStarted = 0
	isPolExpr = False
	evaluate = False
	undefinedToken = False
	var = ""
	string = ""
	expr = ""
	n = ""
	pol = ""
	polExpr = ""
	for char in filecontents:
		tok += char
		if tok == " ":
			if state == 0:
				tok = ""
			else:
				tok = " "
		elif tok == "\n" or tok == "<EOF>":
			if expr != "" and isexpr == 1:
				tokens.append("expr:" + expr)
				expr = ""
				isexpr = 0
			elif pol != "" and polCounter == 1 and isPolExpr == True:
				tokens.append("PolExpr:" + pol)
				pol = ""
				polCounter = 0
			elif expr != "" and isexpr == 0:
				tokens.append("num:" + expr)
				expr = ""
				isexpr = 1
			elif pol != "" and polCounter == 0 and isPolExpr == True:
				tokens.append("pol:" + pol)
				pol = ""
				polCounter = 0
			elif var != "":
				tokens.append("var:" + var)
				var = ""
				varStarted = 0
			elif pol !="" and polStarted == 0 and isPolExpr == False:
				tokens.append("pol:" + pol)
				pol = ""	
			tok = ""
			isPolExpr = False
			polCounter = 0
		elif tok == "=" and state == 0:
			if var != "":
				tokens.append("var:" + var)
				var = ""
				varStarted = 0
			tokens.append("equals")
			tok = ""
		elif tok == "$" and state == 0:
			varStarted = 1
			var += tok
			tok = ""
		elif varStarted == 1:
			if tok == "<" or tok == ">":
				if var!= "":
					tokens.append("var:" + var)
					var = ""
					varStarted = 0
			var += tok
			tok = ""
		elif tok == "print" or tok == "PRINT":
			tokens.append("print")
			tok = ""
		elif eStarted == 0 and polStarted == 0 and state == 0 and (tok == "0" or tok == "1" or tok == "2" or tok == "3" or tok == "4" or tok == "5" or tok == "6" or tok == "7" or tok == "8" or tok == "9"):
			expr += tok
			tok =""
		elif negative == 0 and polCounter == 0 and (tok == "+" or tok == "-" or tok == "/" or tok == "*"):
			expr += tok
			tok = ""
			isexpr = 1
		elif polCounter == 1 and (tok == "+" or tok == "-" or tok == "/" or tok == "*" or tok =="#" or tok == "@"):
			if(tok == "@"):
				evaluate = True
			pol += tok
			tok = ""
			isPolExpr = True
		elif tok == "[":
			pol += tok
			polStarted = 1
			tok = ""
		elif evaluate == False and tok == "(" and polStarted == 1:
				pol += tok
				tok = ""
				termStarted = 1
				negative = 1
		elif termStarted == 1:
			if tok == "0" or tok == "1" or tok == "2" or tok == "3" or tok == "4" or tok == "5" or tok == "6" or tok == "7" or tok == "8" or tok == "9":
				pol += tok
				tok = ""
				negative = 0
				error = 0
			elif tok == "-" and negative == 1:
				pol += tok
				tok = ""
				negative = 0
				error = 1
			elif tok == ",":
				if error == 1:
					print("Syntax Error: No Number after Negative Sign!!")
					exit()
				pol += tok
				tok = ""
			elif tok == ")":
				pol += tok
				tok = ""
				termStarted = 0
		elif tok == "]" and termStarted == 0:
			pol += tok
			tok = ""
			polStarted =0
			polCounter = 1
		elif evaluate == True and tok == "(":
			pol += tok
			tok = ""
			eStarted = 1
			negative = 1
		elif eStarted == 1:
			if tok == "0" or tok == "1" or tok == "2" or tok == "3" or tok == "4" or tok == "5" or tok == "6" or tok == "7" or tok == "8" or tok == "9":
				pol += tok
				tok = ""
				negative = 0
			elif tok == "-" and negative == 1:
				pol += tok
				tok = ""
				negative = 0
			elif tok == ")":
				pol += tok
				tok = ""
				eStarted = 0
				evaluate = False
		elif tok == "\"":
			if state == 0:
				state = 1
			elif state == 1:
				tokens.append("string:" + string + "\"")
				string = ""
				state = 0
				tok = ""
		elif state == 1:
			string += tok
			tok = ""
	#print(tokens)
	#return ''
	return tokens


def evalExpression(expr):
	return eval(expr)
	# expr = "," + expr

	# i = len(expr) - 1
	# num = ""

	# while i >= 0:
	# 	if (expr[i] == "+" or expr[i] == "-" or expr[i] == "/" or expr[i] == "*" or expr[i] == "%"):
	# 		num = num[::-1]
	# 		num_stack.append(num)
	# 		num_stack.append(expr[i])
	# 		num = ""
	# 	elif (expr[i] == ","):
	# 		num = num[::-1]
	# 		num_stack.append(num)
	# 		num = ""
	# 	else:
	# 		num += expr[i]
	# 	i-=1
	# print(num_stack)

def doPrint(toPrint):
	if(toPrint[0:6] == "string"):
		toPrint = toPrint[8:]
		toPrint = toPrint[:-1]
	elif(toPrint[0:3] == "num"):
		toPrint = toPrint[4:]
	elif(toPrint[0:4] == "expr"):
		toPrint = evalExpression(toPrint[5:])
	elif(toPrint[0:3] == "pol"):
		toPrint = polynomialPrint(toPrint[4:])
	elif(toPrint[0:7] == "PolExpr"):
		toPrint = polynomialFunctions(toPrint[8:])
	print(toPrint)


def polynomialPrint(pol):
	return "Aqui se hara el print del polinomio"


def polynomialFunctions(PolExpr):
	return "Aqui se haran las funciones"
	# PolExpr = "," + PolExpr

	# i = len(PolExpr) - 1
	# num = ""

	# while i >= 0:
	# 	if (PolExpr[i] == "+" or PolExpr[i] == "-" or PolExpr[i] == "/" or PolExpr[i] == "*" or PolExpr[i] == "%" or PolExpr[i] == "(" or PolExpr[i] == ")" or  PolExpr[i] == "[" or PolExpr[i] == "]" ):
	# 		num = num[::-1]
	# 		num_stack.append(num)
	# 		num_stack.append(PolExpr[i])
	# 		num = ""
	# 	elif (PolExpr[i] == ","):
	# 		num = num[::-1]
	# 		num_stack.append(num)
	# 		num = ""
	# 	else:
	# 		num += PolExpr[i]
	# 	i-=1
	# print(num_stack)




def doAssign(varName,varValues):
	symbols[varName[4:]] = varValues




def getVariable(varName):
	varName = varName[4:]
	if varName in symbols:
		return symbols[varName]
	else:
		return "Variable ERROR: Undefined Variable"
		exit()

def parse(toks):
	i = 0
	while(i < len(toks)):
		if toks[i] + " " + toks[i+1][0:6] == "print string" or toks[i] + " " + toks[i+1][0:3] == "print num" or toks[i] + " " + toks[i+1][0:4] == "print expr" or toks[i] + " " + toks[i+1][0:3] == "print var" or toks[i] + " " + toks[i+1][0:3] == "print pol" or toks[i] + " " + toks[i+1][0:7] == "print PolExpr":
			if toks[i+1][0:6] == "string":
				doPrint(toks[i+1])
			elif toks[i+1][0:3] == "num":
				doPrint(toks[i+1])
			elif toks[i+1][0:4] == "expr":
				doPrint(toks[i+1])
			elif toks[i+1][0:3] == "var":
				doPrint(getVariable(toks[i+1]))
			elif toks[i+1][0:3] == "pol":
				doPrint(toks[i+1])
			elif toks[i+1][0:7] == "PolExpr":
				doPrint(toks[i+1])
			i+= 2
		elif toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:6] == "var equals string" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] == "var equals num" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:4] == "var equals expr" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] == "var equals var" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] == "var equals pol" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:7] == "var equals PolExpr":
			if toks[i+2][0:6] == "string":
				doAssign(toks[i],toks[i+2])
			elif toks[i+2][0:3] == "num":
				doAssign(toks[i],toks[i+2])
			elif toks[i+2][0:4] == "expr":
				doAssign(toks[i],"num:" + str(evalExpression(toks[i+2][5:])))
			elif toks[i+2][0:3] == "var":
				doAssign(toks[i],getVariable(toks[i+2]))
			elif toks[i+2][0:3] == "pol":
				doAssign(toks[i],toks[i+2])
			elif toks[i+2][0:7] == "PolExpr":
				doAssign(toks[i],toks[i+2])
			i+=3
	#print(symbols)

def run():
	data = open_file(argv[1])
	toks = lex(data)
	parse(toks)

run()