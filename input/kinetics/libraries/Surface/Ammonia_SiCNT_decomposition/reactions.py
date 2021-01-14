#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_SiCNT_decomposition"
shortDesc = u""
longDesc = u"""
Based primarily on "Catalytic decomposition of ammonia 
over silicon-carbide nanotube: a DFT study"
https://doi.org/10.1007/s11224-014-0542-z
"""
#The catalyst is silicon-carbide rather than Pt
entry(
    index = 1,
    label = "NH3_X + X <=> NH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (6.215E12, 'm^2/(mol*s)'),
        n = 0,
        Ea=(1.2, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
    metal = 'Pt',
)

entry(
    index = 2,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (6.213E12, 'm^2/(mol*s)'),
        n = 0,
        Ea=(55.7, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
    metal = 'Pt',
)

entry(
    index = 3,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (6.206E12, 'm^2/(mol*s)'),
        n = 0,
        Ea=(70.4, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
    metal = 'Pt',
)