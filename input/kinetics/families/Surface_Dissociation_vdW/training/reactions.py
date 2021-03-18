#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 7,
    label = "NH3_X + Cu4 <=> NH2_X + H*",
    degeneracy = 3,
    kinetics = SurfaceArrhenius(
        A = (5.723e22, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (78.99, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
    Micro-kinetic modeling of NH3 decomposition on Ni and its application to solid oxide fuel cells
    Deutschmann et al
    doi: 10.1016/j.ces.2011.07.007

    This is R7
""",
    metal = "Ni",
)

entry(
    index = 13,
    label = "COOH* + H* <=> HCOOH* + Cu4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(2.308e18, 'm^2/(mol*s)'),
        n = 0.,
        Ea=(16.8342, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 13 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
6.793e13 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 2.308e18 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 14,
    label = "H2O* + Cu4 <=> OH* + H*",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A=(4.879e15, 'm^2/(mol*s)'),
        n = 0.,
        Ea=(4.84271508, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 14 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.436e11 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 4.879e15 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 19,
    label = "HCOO* + H* <=> HCOOH_1* + Cu4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(4.424e18, 'm^2/(mol*s)'),
        n = 0.,
        Ea=(20.9850987, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 19 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.302e14 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 4.424e18 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 25,
    label = "CH3O* + H* <=> CH3OH_2* + Cu4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(4.349e22, 'm^2/(mol*s)'),
        n = 0.,
        Ea=(10.8384576, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 25 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.28e18 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 4.349e22 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 30,
    label = "HCO* + H* <=> CH2O* + Cu4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.932e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea=(10.8384576, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 30 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
5.685e12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 1.932e17 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 33,
    label = "CH2OH* + H* <=> CH3OH_1* + Cu4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(2.783e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea=(37.5886933, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 33 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
8.189e12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 2.783e17 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 34,
    label = "HCOOH_2* + Cu4 <=> HCO* + OH_2*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.781e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea=(37.5886933, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 34 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
5.242e12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 1.781e17 m^2/(mol*s)
""",
    metal = "Cu",
)
entry(
    index = 35,
    label = "Cu4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(3.46e+20,'cm^2/(mol*s)'), n=0, Ea=(93,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Pt111
Original entry: NH3_X + X <=> NH2_X + H_X
"Ammonia Dissociation on Pt(100), Pt(111), and Pt(211): A Comparative Density Functional Theory Study"
W. K. Offermans, A. P. J. Jansen, R. A. van Santen, G. Novell-Leruth, J. M. Ricart, and J. Pérez-Ramírez
The Journal of Physical Chemistry C 2007 111 (47), 17551-17557
https://doi.org/10.1021/jp073083f
This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 8.6E11(1/s)/2.483E-9(mol/cm^2)
The value is for NH3_X(rot/vib), for NH3_X(vib), A = 5.6E11(1/s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 36,
    label = "Cu4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(9.49e+19,'cm^2/(mol*s)'), n=0, Ea=(110.92,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Ni111_decomposition
Original entry: NH3_X + X <=> NH2_X + H_X
A factor is calculated by the Ea and the rate constant from table 2 in 
"Structure sensitivity of ammonia decomposition over Ni catalysts:
A computational and experimental study", Xuezhi Duan et al.
doi:10.1016/j.fuproc.2012.05.030

A factor from paper / surface site density of Ni111
2.32E7 s^-1 / 3.148E-9 mol/cm^2 = 9.49E19 cm^2/(mol*s)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 37,
    label = "Cu4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(5.5e+19,'cm^2/(mol*s)'), n=0, Ea=(63.66,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Ni211_decomposition
Original entry: NH3_X + X <=> NH2_X + H_X
A factor is calculated by the Ea and the rate constant from table 2 in 
"Structure sensitivity of ammonia decomposition over Ni catalysts:
A computational and experimental study", Xuezhi Duan et al.
doi:10.1016/j.fuproc.2012.05.030

A factor from paper / surface site density of Ni211
1.84E11 s^-1 / 3.339E-9 mol/cm^2 = 5.50E19 cm^2/(mol*s)
""",
    metal = "Ni",
    facet = "211",
)

