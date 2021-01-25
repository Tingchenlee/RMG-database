#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Pt1Ir2_eletro_oxidation"
shortDesc = u""
longDesc = u"""
Based primarily on:
"Ammonia oxidation kinetics on bimetallic clusters of platinum and iridium_ 
A theoretical approach _ Elsevier Enhanced Reade"
https://doi.org/10.1016/j.mcat.2017.11.025
"""
#The values of the A factor and Ea are calculated in the excel file
##The values of the A factor and Ea in index = 4 and index = 5 are really large
entry(
    index = 1,
    label = " NH3_X + X <=> NH2_X + H_X ",
    kinetics = SurfaceArrhenius(
        A = (4.35, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (77.19, 'kJ/mol'),
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
        A = (1.96E10, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (132.19, 'kJ/mol'),
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
        A = (6.54E1, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (83.95, 'kJ/mol'),
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
        A = (7.19E41, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (313.59, 'kJ/mol'),
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
        A = (1.49E35, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (275.96, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Ir" ,
)