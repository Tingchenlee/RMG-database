#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Fe_BEAzeolite_decomposition"
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
        A=1.3E20,
        n = 0.,
        Ea = (0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
    metal = "Fe" ,
)

entry(
    index = 2,
    label = " N2O_X + X <=> N2_X + O_X ",
    kinetics = SurfaceArrhenius(
        A = (3.1E14, 'm^2/(mol*s)'),
        n = 0,
        Ea=(37.4, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = 'Fe',
)

entry(
    index = 3,
    label = " N2 + X <=> N2_X ",
    kinetics = StickingCoefficient(
        A = 8.4E14,
        n = 0,
        Ea=(0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = 'Fe',
)

entry(
    index = 4,
    label = " O2 + X <=> O2_X ",
    kinetics = StickingCoefficient(
        A =  7.53E10,
        n = 0,
        Ea=(0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = 'Fe',
)