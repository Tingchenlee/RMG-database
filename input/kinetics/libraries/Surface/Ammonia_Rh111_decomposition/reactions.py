#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Rh111_decomposition"
shortDesc = u""
longDesc = u"""
Based primarily on "Ab initio density-functional theory study of NHx dehydrogenation and reverse reactions
on the Rh(111) surface"
https://doi.org/10.1103/PhysRevB.74.155428
"""

entry(
    index = 59,
    label = "NH2_X + H_X <=> NH3_X + X",
    kinetics = SurfaceArrhenius(
        A = (1.9E15, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (106.10, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R12""",
    longDesc = u"""Surface_Dissociation_vdW""",
    metal = "Rh",
)


entry(
    index = 60,
    label = "NH_X + H_X <=> NH2_X + X",
    kinetics = SurfaceArrhenius(
        A = (5.03E13, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (93.56, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R13""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Rh",
)

entry(
    index = 61,
    label = "N_X + H_X <=> NH_X + X",
    kinetics = SurfaceArrhenius(
        A = (2.6E13, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (72.34, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R14""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Rh",
)