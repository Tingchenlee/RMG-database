#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_H_ZSM5_2"
shortDesc = u""
longDesc = u"""
Based primarily on "Detailed Kinetic Modeling of NH3 and H2O Adsorption, and NH3 Oxidation over Cu-ZSM-5"
https://doi.org/10.1021/jp802449s
J. Phys. Chem. C 2009, 113, 1393–1405
Hanna Sjovall, Richard J. Blint, and Louise Olsson
"""
#entry(
#    index = 10,
#    label = "H2O + X <=> H2O_X",
#    kinetics = StickingCoefficient(
#        A = 1.18E3,
#        n = 0,
#        Ea = (0, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""R10""",
#    longDesc = u"""Surface_Adsorption""",
#	metal = "Pt",
#)

#entry(
#    index = 11,
#    label = "NH3 + X <=> NH3_X",
#    kinetics = StickingCoefficient(
#        A = 1.15E3,
#        n = 0,
#        Ea = (0, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""R11""",
#    longDesc = u"""Surface_Adsorption_vdW """,
#    metal = 'Pt',
#)

entry(
    index = 57,
    label = "H2O_X <=> H2O + X",
    kinetics = SurfaceArrhenius(
        A = (1.23E13, '1/s'),  
        n = 0.0,
        Ea = (119070, 'J/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R10""",
    longDesc = u"""Surface_Adsorption""",
	metal = "Pt",
)

entry(
    index = 58,
    label = "NH3_X <=> NH3 + X",
    kinetics = SurfaceArrhenius(
        A = (1.23E13, '1/s'),  
        n = 0.0,
        Ea = (117920, 'J/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R11""",
    longDesc = u"""Surface_Adsorption_vdW """,
    metal = 'Pt',
)

