def puiss(c,liste):
  a= [x**c for x  in liste]
  return a 

d = puiss(3,[4,5])
print (d) 

def puiss_etoile(nb, b ,**options):
  li= [x**nb for x  in options]
  return li 

assert puiss_etoile(2,4,5) == [16, 25]
