#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Ir3_eletro_oxidation"
shortDesc = u""
longDesc = u"""
Based primarily on:
"Ammonia oxidation kinetics on bimetallic clusters of platinum and iridium_ 
A theoretical approach _ Elsevier Enhanced Reade"
https://doi.org/10.1016/j.mcat.2017.11.025
"""
#The values of the A factor and Ea are calculated in the excel file
#The values of the A factor and Ea in index = 4 and index = 5 are really large
entry(
    index = 1,
    label = " NH3_X + X <=> NH2_X + H_X ",
    kinetics = SurfaceArrhenius(
        A = (1.15E2, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (84.91, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Ir" ,
)

entry(
    index = 2,
    label = " NH2_X + X <=> NH_X + H_X ",
    kinetics = SurfaceArrhenius(
        A = (1.34E18, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (177.54, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Ir" ,
)

entry(
    index = 3,
    label = " NH_X + X <=> N_X + H_X ",
    kinetics = SurfaceArrhenius(
        A = (3.92E7, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (116.75, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Ir" ,
)

entry(
    index = 4,
    label = " N_X + N_X <=> N2_X + X ",
    kinetics = SurfaceArrhenius(
        A = (5.81E47, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (347.36, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Ir" ,
)

entry(
    index = 5,
    label = " NH2_X + NH2_X <=> N2H4_X + X ",
    kinetics = SurfaceArrhenius(
        A = (6.9E49, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (325.17, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Ir" ,
)