#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Bidentate_Dissociation/rules"
shortDesc = u""
longDesc = u"""
"""
entry(
    index = 1,
    label = "Combined",
    kinetics = SurfaceArrheniusBEP(
<<<<<<< HEAD
        A = (1.0e9, '1/s'),
        n = 0,
=======
        A = (8.96e10, '1/s'),
        n = 0.422,
>>>>>>> ca4001e75f0bbcc01f0b784dabd361d5203b5a53
        alpha = 0,
        E0 = (0.0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
Pre-exponential value, n and E0 are from R42 in Table 1 of "A Catalytic Reaction Mechanism for Methane 
Partial Oxidation at Short ContactTimes, Reforming, and Combustion, and 
for Oxygenate Decomposition and Oxidation on Platinum"
Authors:  A.B. Mhadeshwar and D.G. Vlachos
doi:10.1021/ie070322c

The reaction is
   HCOO** -> CO2* + H*
They report a nonlinear dependence of the activation energy on specific coverage (of H*)
and temperature, but don't say what this dependence is.
Note that this reaction is not actually an example of this reaction family!
It the dissociation of a bidentate adsorbate, but the H* that ends up adsorbed was not 
one of the initial adatoms.
However, in the absence of better data, it is currently our best estimate. (KB, CFG, RHW, 2020-11-30).
"""
)



