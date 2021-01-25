#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Pt_Al2O3_oxidation2"
shortDesc = u""
longDesc = u"""
Based primarily on "Experimental and modeling study of selective ammonia oxidation on multi-functional washcoated monolith catalysts"
https://doi.org/10.1016/j.cej.2015.01.015
"""
entry(
    index = 1,
    label = " NH3 + X <=> NH3_X ",
    kinetics = StickingCoefficient(
        A = 2E1,                
        n = 0,
        Ea = (0, 'kJ/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
    metal = "Pt" ,
)

entry(
    index = 2,
    label = "O2 + X + X <=> O_X + O_X",
    kinetics = StickingCoefficient(
        A = 2.7E2,
        n = 0,
        Ea = (0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
    metal = 'Pt',
)

entry(
    index = 3,
    label = "N_X + N_X <=> N2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (1.2E19, 'm^2/(mol*s)'),
        n = 0,
        Ea = (185, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
	metal = "Pt",
)

entry(
    index = 4,
    label = "NO + X <=> NO_X",
    kinetics = StickingCoefficient(
        A = 2.9E2,
        n = 0,
        Ea = (0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""efault""",
	metal = "Pt",
)

entry(
    index = 5,
    label = "N_X + O_X <=> NO_X + X",
    kinetics = SurfaceArrhenius(
        A = (2.8E13, 'm^2/(mol*s)'),
        n = 0,
        Ea = (128, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
	metal = "Pt",
)

entry(
    index = 6,
    label = "NO_X + N_X <=> N2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (9.8E19, 'm^2/(mol*s)'),
        n = 0,
        Ea = (140, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
	metal = "Pt",
)

entry(
    index = 7,
    label = "NO_X + O_X <=> NO2_X + X",
    kinetics = SurfaceArrhenius(
        A = (6.6E14, 'm^2/(mol*s)'),
        n = 0,
        Ea = (110, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
	metal = "Pt",
)

entry(
    index = 8,
    label = "NO2_X  <=> NO2 + X",
    kinetics = SurfaceArrhenius(
        A = (1.3E14, 'm^2/(mol*s)'),
        n = 0,
        Ea = (107, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
	metal = "Pt",
)