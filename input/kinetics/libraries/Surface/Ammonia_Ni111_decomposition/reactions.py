#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Ni111_decomposition"
shortDesc = u""
longDesc = u"""
Based primarily on "Structure sensitivity of ammonia decomposition over Ni catalysts: A computational and experimental study"
https://doi.org/10.1016/j.fuproc.2012.05.030
"""

entry(
    index = 1,
    label = " N_X + N_X <=> N2 + X + X ",
    kinetics = SurfaceArrhenius(
        A = (2.13E1, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (189.04, 'kJ/mol'),
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
        A = (5.43, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (110.92, 'kJ/mol'),
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
        A = (1.04E8, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (57.87, 'kJ/mol'),
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
        A = (3.06E4, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (106.10, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
    metal = "Ni" ,
)
