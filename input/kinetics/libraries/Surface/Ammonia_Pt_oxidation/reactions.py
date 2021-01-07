#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Pt_oxidation"
shortDesc = u""
longDesc = u"""
Based primarily on "Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
https://doi.org/10.1016/S1385-8947(02)00068-2
"""

entry(
    index = 1,
    label = " NH3 + X <=> NH3_X ",
    kinetics = StickingCoefficient(
        A = 2e8,
        n = 0,
        Ea=(0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = 'Cattype',
)


entry(
    index = 2,
    label = " NH3_X + O_X <=> NH2_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A = (1.7E15, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (157, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 3,
    label = " NO_X + X <=> N_X + O_X ",
    kinetics = SurfaceArrhenius(
        A = (1.6E13, 'm^2/(mol*s)'),
        n = 0,
        Ea = (116.8, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = 'Cattype',
)

entry(
    index = 4,
    label = " N_X + N_X  <=>  N2 + X + X ",
    kinetics = SurfaceArrhenius(
        A = (1E11, 'm^2/(mol*s)'),  
        n = 0.0,
        Ea = (79.1, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
""",
    metal = "Pt" ,
)

entry(
    index = 5,
    label = " N_X + NO_X   <=>  N2O_X + X ",
    kinetics = SurfaceArrhenius(
        A = (1E11, 'm^2/(mol*s)'),  
        n = 0.0,
        Ea = (92.9, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 6,
    label = " N2O + X <=>  N2 + O_X ",
    kinetics = SurfaceArrhenius(
        A = (2.5E8, 'm^2/(mol*s)'),  
        n = 0.0,
        Ea = (72.2, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 7,
    label = " NO_X <=> NO + X ",
    kinetics = SurfaceArrhenius(
        A = (1E16, 'm^2/(mol*s)'),   
        n = 0.0,
        Ea = (151, 'kJ/mol'), 
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 8,
    label = " NH_X + OH_X <=> N_X + H2O_X ",
    kinetics = SurfaceArrhenius(
        A = (1E11, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (46, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)