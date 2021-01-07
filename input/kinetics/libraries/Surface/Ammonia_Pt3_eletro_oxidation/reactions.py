#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Pt3_eletro_oxidation"
shortDesc = u""
longDesc = u"""
Based primarily on:
"Ammonia oxidation kinetics on bimetallic clusters of platinum and iridium_ 
A theoretical approach _ Elsevier Enhanced Reade"
https://doi.org/10.1016/j.mcat.2017.11.025
"""
#The values of the A factor and Ea are calculated in the excel file
#The reaction mechanisms of ammonia oxidation are not similar to other papers
entry(
    index = 1,
    label = " NH3_X + X <=> NH2_X + H_X ",
    kinetics = SurfaceArrhenius(
        A = (1.21E12, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (142.81, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 2,
    label = " NH2_X + NH2_X <=> N2H4_X + X ",
    kinetics = SurfaceArrhenius(
        A = (1.21E23, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (206.49, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 3,
    label = " N2H4_X + X <=> N2H3_X + H_X ",
    kinetics = SurfaceArrhenius(
        A = (2.5E7, 'm^2/(mol*s)'), 
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
    label = " N2H3_X + X <=> N2H2_X + H_X ",
    kinetics = SurfaceArrhenius(
        A = (1.31E5, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (103.24, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 5,
    label = " N2H2_X + X <=> N2H_X + H_X ",
    kinetics = SurfaceArrhenius(
        A = (3.76E11, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (139.91, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

#The A factor and Ea of this mechanism is really difference
entry(
    index = 6,
    label = " N2H_X + X <=> N2_X + H_X ",
    kinetics = SurfaceArrhenius(
        A = (2.49E-13, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (0.96, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 7,
    label = " NH2_X + X <=> NH_X + H_X ",
    kinetics = SurfaceArrhenius(
        A = (4.81E23, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (209.38, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 8,
    label = " NH_X + X <=> N_X + H_X ",
    kinetics = SurfaceArrhenius(
        A = (4.57E16, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (168.86, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)