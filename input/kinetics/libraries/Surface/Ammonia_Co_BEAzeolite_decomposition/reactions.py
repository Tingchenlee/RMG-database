#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Co_BEAzeolite_decomposition"
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
        A=3.53E20,
        n = 0.,
        Ea = (0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
    metal = "Co" ,
)

entry(
    index = 2,
    label = " N2O_X + X <=> N2_X + O_X ",
    kinetics = SurfaceArrhenius(
        A = (1.51E12, 'm^2/(mol*s)'),
        n = 0,
        Ea=(38.24, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = 'Co',
)

entry(
    index = 3,
    label = " N2 + X <=> N2_X ",
    kinetics = StickingCoefficient(
        A =  2.31E-16,
        n = 0,
        Ea=(98.54, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = 'Co',
)

entry(
    index = 4,
    label = " O2 + X <=> O2_X ",
    kinetics = StickingCoefficient(
        A =  5.44E-25,
        n = 0,
        Ea=(0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = 'Co',
)