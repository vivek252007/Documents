# import data_helpers as dh

# # print (dh.load_glove(50))
# # x_raw, y_test = dh.load_test('test.xlsx')
# # dh.load_data('data.xlsx','output_file.xlsx')
# print (dh.load_data('AAPL.xlsx','AAPL_output.xlsx') )

from scipy import linspace
from scipy import pi,sqrt,exp
from scipy.special import erf

from pylab import plot,show

def pdf(x):
    return 1/sqrt(2*pi) * exp(-x**2/2)

def cdf(x):
    return (1 + erf(x/sqrt(2))) / 2

def skew(x,e=0,w=1,a=0):
    t = (x-e) / w
    return 2 / w * pdf(t) * cdf(a*t)
    # You can of course use the scipy.stats.norm versions
    # return 2 * norm.pdf(t) * norm.cdf(a*t)


n = 2**10

e = 1.0 # location
w = 2.0 # scale

x = linspace(-10,10,n) 

for a in range(-3,4):
    p = skew(x,e,w,a)
    plot(x,p)

show()