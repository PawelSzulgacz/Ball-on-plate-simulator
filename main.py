import math
from bokeh.io import output_notebook, show
from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.io import export_png
import os

square = 0.20 #wielkosc planszy
r = 2 #promien kuli
g = 9.81 #stala grawitacyjna
t = 0 #czas
t_p = 0.05 #chwila próbkowania
s = 5 #czas eksperymentu w sekundach
up = 180*t_p #maksymalna szybkosc podnoszenia w stopniach
maxk = 15 #maksymalny kąt podniesienia
tab = []

k_p = 5
t_i = 0.3
t_d = 0.5
sumaex = 0
sumaey = 0
ex = []
ux = []
ey = []
uy = []
ux_pd = 0
uy_pd = 0
umin = -10
umax = 10
alfzmx = 0
alfzmy = 0

alfax = [] #kat nachylenia platformy wzgledem osi x
alfay = [] #kat nachylenia platformy wzgldem osi y
x = [] #odleglosc kuli od srodak wzgledem osi x
xa = [] #przyspieszenie kuli w punkcie wzgledem osi x m/s
xp = [] #predkosc kuli wzgledem osi x
y = [] #odleglosc kuli od srodka wzgledem osi y
ya = [] #przyspieszenie kuli wzgledem osi y
yp = [] #predkosc kuli wzgledem osi y

def obsin(a):
    return math.sin(math.radians(a))
#---------------------------
#wartości z zakresu 0 - 0.2
xzad = 0.1
yzad = 0.1
ypocz = 0.02 ##miejsce rozpoczecia kuli na osi y
xpocz = 0.13 #miejsce rozpoczecia kuli na osi x
#------------------------
x.append(xpocz)
y.append(ypocz)


xp.append(0)
yp.append(0)
n = s/t_p
xa.append(0)
ex.append(xzad - x[0])
ey.append(yzad - y[0])
ux.append(0)
tab.append(0)
alfax.append(0)
alfay.append(0)
maks = 0
# + (t_p/t_i)*sumaex
file = open("mx.txt", "w")
for i in range(1,int(n)):
    tab.append(i*t_p)

    ex.append(xzad - x[i-1])
    ux_pd = k_p * (ex[i-1] +(t_d/t_p)*(ex[i-1]-ex[i-2])) # pd
    ux.append(min(umax,max(umin,ux_pd)))
    if abs(ux_pd*10) < up: alfzmx = ux_pd * 10 #czy nie przekracza maksymalnego odchylenia ramienia
    elif ux_pd < 0: alfzmx = -up
    else: alfzmx = up
    alfax.append(alfzmx) #nowe odchylenie alfy
    xp.append(xp[i - 1] + (5 / 7 * g * obsin(alfax[i - 1]) * t_p))
    #przyspieszenie = predkosc - przyspieszenie*czas probkowania w sekundach
    x.append(x[i-1]+xp[i-1]*t_p)
    #miejsce - poprzednie miejsce plus predkosc razy ilosc czasu

    ey.append(yzad - y[i-1])
    uy_pd = k_p * (ey[i-1] +(t_d/t_p)*(ey[i-1]-ey[i-2])) # pid
    uy.append(min(umax,max(umin,uy_pd)))
    if abs(uy_pd*10) < up: alfzmy = uy_pd * 10
    elif uy_pd < 0: alfzmy = -up
    else: alfzmy = up
    alfay.append(alfzmy)
    yp.append(yp[i - 1] + (5 / 7 * g * obsin(alfay[i - 1]) * t_p))
    y.append(y[i-1]+yp[i-1]*t_p)
    zm = "{:.17f} {:.17f} {:.17f} {:.17f} ".format(x[i-1],y[i-1],alfax[i-1],alfay[i-1])
    file.write(zm)






p = figure(plot_width=300,y_range=(0,0.2), plot_height=300, title="Odległość kuli od osi x")
p.line(tab, x, line_width=2)
s = figure(plot_width=300, plot_height=300, title="Ruch ramienia x")
s.line(tab, alfax, line_width=2)
export_png(row(p,s), filename="plotx.png")
l = figure(plot_width=300,y_range=(0,0.2), plot_height=300, title="Odległość kuli od osi y")
l.line(tab, y, line_width=2)
t = figure(plot_width=300, plot_height=300, title="Ruch ramienia y")
t.line(tab, alfay, line_width=2)
export_png(row(l,t), filename="ploty.png")
