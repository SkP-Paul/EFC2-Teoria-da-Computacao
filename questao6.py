from __future__ import print_function
 
def run_utm(regras = []):
    R = "000"
    REstados = []
    RAlfa = []
    estados = []
    alfa = []
    
    x = "1"        
    y = "1"
    i = 0
    for regra in regras:
        if(i > 0):
            R = R + "00"
        if(regra[0] not in estados):
            estados.append(regra[0])
            REstados.append(x)
            x = x + "1"
        if(regra[4] not in estados):
            estados.append(regra[4])
            REstados.append(x)
            x = x + "1"
        if(regra[1] not in alfa):
            alfa.append(regra[1])
            RAlfa.append(y)
            y = y + "1"
        if(regra[2] not in alfa):
            alfa.append(regra[2])
            RAlfa.append(y)
            y = y + "1"
        posicaoEstado = estados.index(regra[0])
        R = R + REstados[posicaoEstado] + "0"
        posicaoAlfa = alfa.index(regra[1])
        R = R + RAlfa[posicaoAlfa] + "0"
        posicaoEstado = estados.index(regra[4])
        R = R + REstados[posicaoEstado] + "0"
        posicaoAlfa = alfa.index(regra[2])
        R = R + RAlfa[posicaoAlfa] + "0"
        if(regra[3] == "L"):
            R = R + "1"
        elif(regra[3] == "R"):
            R = R + "11"
        elif(regra[3] == "S"):
            R = R + "111"
        i = i + 1
    
    R = R + "000"
    print(R)
 
 
# EXAMPLES
run_utm(
	regras = map(tuple, 
               ["q0 1 1 R q0".split(),
		        "q0 B 1 S qf".split()]
        )
    )
