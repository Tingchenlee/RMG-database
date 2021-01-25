#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Pt2Ir1_eletro_oxidation"
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
        A = (8.55E5, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (107.1, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 2,
    label = " NH2_X + X <=> NH_X + H_X ",
    kinetics = SurfaceArrhenius(
        A = (1.36E10, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (131.23, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 3,
    label = " NH_X + X <=> N_X + H_X ",
    kinetics = SurfaceArrhenius(
        A = (2.65E7, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (115.79, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 4,
    label = " N_X + N_X <=> N2_X + X ",
    kinetics = SurfaceArrhenius(
        A = (1.21E42, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (316.49, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 5,
    label = " NH2_X + NH2_X <=> N2H4_X + X ",
    kinetics = SurfaceArrhenius(
        A = (2.94E45, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (334.82, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)