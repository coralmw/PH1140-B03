import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.optimize as opt

def linear(x,p0,p1) : 
    return p0*x+p1

def quadratic(x,p0,p1,p2) : 
    return p0*x**2+p1*x+p2 

def exponential(x,p0,p1) :
    return p0*np.exp(p1*x)

def hyperbolic(x,p0,p1) :
    return p0*np.exp(p1*x)

def gaussian(x,p0,p1,p2) : 
    return p0/(p2*np.sqrt(2*np.pi))*np.exp(-(x-p1)**2/(2*p2**2)) 

def cosine(x, p0, p1):
    return x**p0*np.cos(p1*x)

fitters = {"linear":linear, "quadratic":quadratic, "exponential":exponential, "gaussian":gaussian, 'cosine':cosine}

def plot(x, y, fitstyle=None, xerr=None, yerr=None, p0=None):
    if fitstyle:
        popt, pcov = opt.curve_fit(fitters[fitstyle], x, y, p0=p0)
        fit_x = np.linspace(min(x), max(x), 1000)
        fit_y = np.apply_along_axis( lambda xv: fitters[fitstyle](xv, *popt), 0, fit_x)
        print("intercept", fitters[fitstyle](0, *popt))
        plt.plot(fit_x, fit_y)
        print("fit params", popt)
        print("Fit parameters errors = '" ,np.sqrt(np.diag(pcov)))

    plt.errorbar(x, y, yerr=yerr, xerr=xerr, marker='o', linestyle=' ') 

    if fitstyle:
        return popt, pcov
    
def combine_error(da, a, db, b, out):
    return out * np.sqrt( (da/a)**2 + (db/b)**2 )
