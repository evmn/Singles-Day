#!/usr/bin/python3

from pylab import plot,legend,savefig,show
years = range(2009,2019)
sales = [0.5,9.36,52.0,191.0,350.0,571.0,912.0,1207.0,1682.69,2135.0]
x = range(2009,2026)
Q = []
C = []

for year in range(2009,2026):
    quadratic = 30.0950757563*year**2\
                - 120956.004555409*year\
                + 121534455.999401
    Q.append(quadratic)

    cubic = 0.154308467952835*year**3\
            - 902.005224902955*year**2\
            + 1755825.69018305*year\
            - 1138095823.60156
    C.append(cubic)

plot(years, sales, 'yo', ms=18, label='Official data') 
plot(x, Q, marker='X', color='red', ms=12, linewidth=3, label='Quadratic simultaneous')
plot(x, C, marker='d', color='black', ms=10, linewidth=2, label='Cubic simultaneous')

legend(loc='upper left')
savefig('sales.png')
show()
