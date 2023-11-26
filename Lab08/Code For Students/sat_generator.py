import random

def generate(c,lm):

    sat = []

    for i in range(c):
        cla = []
        varc  = random.randint(1,lm)

        for j in range(varc):

            var = random.randint(1,lm)
            cflip = random.randint(0,1)

            if (cflip):
                cla.append(var*-1)
            else:
                cla.append(var)


        cla2 = list(set(cla))
        sat.append(cla2)
        
        for i in sat:
            st = ""

        for j in i:
            st += str(j)
            st += " "


    return sat


def generate_formula(num_clauses, num_vars):
 
    sats = [generate(num_clauses, num_vars) for i in range(1)]

    # Elimina los posibles repetidos

    sats = [[list(set(x)) for x in elem] for elem in sats]

    return sats[0]


