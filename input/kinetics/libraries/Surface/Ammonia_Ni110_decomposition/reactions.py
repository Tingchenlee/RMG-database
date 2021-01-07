#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Ni110_decomposition"
shortDesc = u""
longDesc = u"""
Based primarily on "First-principles calculations of ammonia decomposition on Ni(110) surface"
https://doi.org/10.1016/j.susc.2011.11.030
"""

entry(
    index = 1,
    label = " N_X + N_X <=> N2 + X + X ",
    kinetics = SurfaceArrhenius(
        A=(9.72E10, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (158.24, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
    metal = "Ni" ,
)

entry(
    index = 2,
    label = " NH3_X + X <=> NH2_X + H_X ",
    kinetics = SurfaceArrhenius(
        A=(2.52E6, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (77.19, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
    metal = "Ni" ,
)

entry(
    index = 3,
    label = " NH2_X + X <=> NH_X + H_X ",
    kinetics = SurfaceArrhenius(
        A=(9.84E5, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (136.05, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
    metal = "Ni" ,
)

entry(
    index = 4,
    label = " NH_X + X <=> N_X + H_X ",
    kinetics = SurfaceArrhenius(
        A=(5.27E7, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (67.54, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
    metal = "Ni" ,
)
