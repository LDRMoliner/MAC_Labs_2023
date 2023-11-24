def list_minisat2list_our_sat(name_file):
    in_data = open(name_file).readlines()
    l = [ [ int(n) for n in line.split() if n != '0' ] for line in in_data if line[0] not in ('c', 'p') ]
    
    num_variables = max([abs(sublist[-1]) for sublist in l])
    
    return (num_variables, l)

