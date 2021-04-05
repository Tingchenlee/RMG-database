#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Pt100_oxidation3"
shortDesc = u""
longDesc = u"""
Based primarily on "Ammonia Oxidation over Polycrystalline Platinum: Surface Morphology and Kinetics at Atmospheric Pressure."
Krähnert, Ralph(2005) A Doctoral Thesis.
http://dx.doi.org/10.14279/depositonce-1270
"""

entry(
    index = 24,
    label = "N_X + O_X <=> NO_X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
""",
    metal = "Pt",
)

entry(
    index = 49,
    label = "N_X + N_X <=> N2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
""",
    metal = "Pt",
)

entry(
    index = 50,
    label = "O_X + O_X <=> O2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""O2 Surface_Adsorption_Dissociative""",
    longDesc = u"""

""",
	metal = "Pt",
)

entry(
    index = 58,
    label = "NH3_X <=> NH3 + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""

""",
    metal = "Pt",
)

entry(
    index = 76,
    label = "NO_X <=> NO + X",
    kinetics = SurfaceArrhenius(
        A = (, '1/s'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""

""",
    metal = "Pt",
)

entry(
    index = 80,
    label = "N_X + NO_X <=> N2O + X + X",
    kinetics = SurfaceArrhenius(
        A = (, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""""",
    metal = "Pt",
)