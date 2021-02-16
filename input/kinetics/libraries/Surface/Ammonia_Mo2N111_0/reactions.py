#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Mo2N111_0"
shortDesc = u""
longDesc = u"""
Based primarily on "Anisotropic N-Modification of the Mo4 Ensemble for Efficient Ammonia Synthesis on Molybdenum Nitrides"
https://doi.org/10.1021/acs.jpcc.9b09405
"""

entry(
    index = 48,
    label = "H_X + H_X <=> H2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (6.06, 'm^2/(mol*s)'),  
        n = 0.0,
        Ea = (187110, 'J/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R1""",
    longDesc = u"""H2 Surface_Adsorption_Dissociative""",
    metal = 'Mo',
)

entry(
    index = 49,
    label = "N_X + N_X <=> N2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (4.39E2, 'm^2/(mol*s)'),  
        n = 0.0,
        Ea = (158180, 'J/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R2""",
    longDesc = u"""N2 Surface_Adsorption_Dissociative""",
    metal = 'Mo',
)

entry(
    index = 52,
    label = "N2_X <=> N2 + X",
    kinetics = SurfaceArrhenius(
        A = (8.38, '1/s'),  
        n = 0.0,
        Ea = (218940, 'J/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R5""",
    longDesc = u"""N2 Surface_Adsorption_vdW""",
    metal = 'Mo',
)

entry(
    index = 58,
    label = "NH3_X <=> NH3 + X",
    kinetics = SurfaceArrhenius(
        A = (1.75E1, '1/s'),  
        n = 0.0,
        Ea = (196760, 'J/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R11""",
    longDesc = u"""Surface_Adsorption_vdW """,
    metal = 'Mo',
)

entry(
    index = 59,
    label = "NH2_X + H_X <=> NH3_X + X",
    kinetics = SurfaceArrhenius(
        A = (1.63, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (168790, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R12""",
    longDesc = u"""Surface_Dissociation_vdW""",
    metal = "Mo",
)

entry(
    index = 60,
    label = "NH_X + H_X <=> NH2_X + X",
    kinetics = SurfaceArrhenius(
        A = (2.9, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (159140, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R13""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Mo",
)

entry(
    index = 61,
    label = "N_X + H_X <=> NH_X + X",
    kinetics = SurfaceArrhenius(
        A = (6.4E1, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (137920, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R14""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Mo",
)