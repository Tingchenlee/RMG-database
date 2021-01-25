#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_ASC_Pt111"
shortDesc = u""
longDesc = u"""
Based primarily on "Optimizing the dual-layer Pt/Al2O3 + Cu/SSZ-13 washcoated monolith: Selective oxidation of NH3 to N2"
https://doi.org/10.1016/j.cattod.2020.01.017
"""
#Similar to Ammonia_Pt_Al2O3_oxidation2
entry(
    index = 1,
    label = "NH3 + X <=> NH3_X",
    kinetics = StickingCoefficient(
        A = 4.2E1,                
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
        A = 2.8E2,
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
        Ea = (181.9, 'kJ/mol'),
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
        A = 3E2,
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
        A = (1.6E14, 'm^2/(mol*s)'),
        n = 0,
        Ea = (136.5, 'kJ/mol'),
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
        A = (93.1E19, 'm^2/(mol*s)'),
        n = 0,
        Ea = (137.8, 'kJ/mol'),
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
        A = (6.68E14, 'm^2/(mol*s)'),
        n = 0,
        Ea = (107.5, 'kJ/mol'),
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
        Ea = (124.8, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
	metal = "Pt",
)