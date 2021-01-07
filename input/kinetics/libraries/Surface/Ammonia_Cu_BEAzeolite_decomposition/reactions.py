#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Cu_BEAzeolite_decomposition"
shortDesc = u""
longDesc = u"""
Based primarily on "Comparative study on the direct decomposition
 of nitrous oxide over M (Fe, Co, Cu)–BEA zeolites"
https://doi.org/10.1016/j.jcat.2012.07.008
"""

entry(
    index = 1,
    label = " N2O + X <=> N2O_X ",
    kinetics = StickingCoefficient(
        A=1.05E18,
        n = 0.,
        Ea = (0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
    metal = "Cu" ,
)

entry(
    index = 2,
    label = " N2O_X + X <=> N2_X + O_X ",
    kinetics = SurfaceArrhenius(
        A = (5.17E12, 'm^2/(mol*s)'),
        n = 0,
        Ea=(97.2, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = 'Cu',
)

entry(
    index = 3,
    label = " N2 + X <=> N2_X ",
    kinetics = StickingCoefficient(
        A =  8.23E15,
        n = 0,
        Ea=(0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = 'Cu',
)

entry(
    index = 4,
    label = " O2 + X <=> O2_X ",
    kinetics = StickingCoefficient(
        A =  1.59E10,
        n = 0,
        Ea=(0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = 'Cu',
)