def prendolistainput(n):
	l = []
	for i in range(n):
		l.append(int(input("Inserisci l'elemento della lista\n")))
	return l

def moltiplicatore(n):
	s = 1
	for e in n:
		s*=e
	return s
"hello"

l = prendolistainput(int(input("Inserisci numero elementi\n")))
print(f"Il risultato è {moltiplicatore(l)}")
