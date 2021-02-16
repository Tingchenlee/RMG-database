#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Ir100_decompostion"
shortDesc = u""
longDesc = u"""
Based primarily on "Mechanism of Ammonia Decomposition and Oxidation on Ir(100): A First-Principles Study"
https://doi.org/10.1021/jp305399g
"""

entry(
    index = 2,
    label = " NH3_X +O_X <=> NH2_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A = (1.1E9, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (27.97, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Ir" ,
)

entry(
    index = 4,
    label = " NH_X +O_X <=> N_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A = (4.34E4, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (25.08, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Ir" ,
)

entry(
    index = 6,
    label = " NH2_X + OH_X <=> NH_X + H2O + X  ", #This paper proposes for a gas phase H2O
    kinetics = SurfaceArrhenius(
        A = (4.99E11, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (102.24, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Ir" ,
)

entry(
    index = 11,
    label = " N_X + N_X  <=>  N2 + X + X ",
    kinetics = SurfaceArrhenius(
        A = (6.74E7, 'm^2/(mol*s)'),  
        n = 0.0,
        Ea = (51.12, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Ir" ,
)

entry(
    index = 9,
    label = " N_X + O_X  <=>  NO_X + X ",
    kinetics = SurfaceArrhenius(
        A = (3.86E6, 'm^2/(mol*s)'),  
        n = 0.0,
        Ea = (61.73, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Ir" ,
)

entry(
    index = 8,
    label = " NO_X <=> NO + X ",
    kinetics = SurfaceArrhenius(
        A = (5.66E-8, 'm^2/(mol*s)'),   
        n = 0.0,
        Ea = (225.69, 'kJ/mol'), 
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Ir" ,
)