dict = {tuple([0,0]):1, tuple([0,1]):2, tuple([0,3]):3}
x = dict[tuple([0,1])]
#bisogna convertire la lista in tupla, cioè un hashable data data-type, il dizionario non lo è, perchè può variare
print(x)