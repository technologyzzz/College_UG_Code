#Topik 1

#Topik 2

#Topik 3


# himpunan dengan matplotlib
from matplotlib import pyplot as plt
from matplotlib_venn import venn2

Basket = {'Andi', 'Eko', 'Anto', 'Zara'}
Voli = {'Julia', 'Kirana', 'Deby', 'Anto'}
        
plt.figure(1)
venn2([Basket,Voli],set_labels = ('Basket', 'Voli'))
plt.show() 

