#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

# reverse of 16, below
# entry(
#     index = 34,
#     label = "H2O* + O* <=> OH_2* + OH_4*",
#     degeneracy = 2,
#     kinetics = SurfaceArrhenius(
#         A = (8.14E20, 'm^2/(mol*s)'),
#         n = -0.274,
#         Ea = (218400, 'J/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     rank = 10,
#     shortDesc = u"""Default""",
#     longDesc = u"""R34
#     test surface mechanism: based upon Olaf Deutschmann's work:
#     "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
#     Delgado et al
#     Catalysts, 2015, 5, 871-904""",
# 	  metal = "Ni",
# )

# reverse of 34, above
entry(
    index = 16,
    label = "OH_2* + OH_4* <=> H2O* + O*",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (5.691e16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (14.0669343, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 16 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.675e12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 5.691e16 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 21,
    label = "CH4* + O* <=> CH3* + OH_4*",
    degeneracy = 4,
    kinetics = SurfaceArrhenius(
        A = (5.62E20, 'm^2/(mol*s)'),
        n = -0.101,
        Ea = (92700, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R21
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	metal = "Ni",
)

entry(
    index = 40,
    label = "OH_2* + HCO* <=> H2O* + CO*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (3.261e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (6.9181644, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 40 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
9.597e12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 3.261e17 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 41,
    label = "HCOO_1* + HCO* <=> HCOOH* + CO*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (7.475e18, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (13.8363288, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 41 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
2.2e14 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 7.475e18 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 45,
    label = "CH3O* + HCO* <=> CH3OH* + CO*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (6.572e16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (8.76300824, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 45 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.934e12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 6.572e16 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 46,
    label = "CH3O* + HCOO_5* <=> HCOOCH3* + O*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (2.356e16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (28.5950795, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 46 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
6.934e11 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 2.356e16 m^2/(mol*s)
""",
    metal = "Cu",
)
entry(
    index = 47,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(1.557e+21,'cm^2/(mol*s)'), n=0, Ea=(55964,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Pt211_oxidation
Original entry: NH3_X +O_X <=> NH2_X + OH_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251
This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 4.1E12(1/s)/2.634E-9(mol/cm^2)
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 48,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(1.007e+21,'cm^2/(mol*s)'), n=0, Ea=(67543,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Pt111_oxidation
Original entry: NH3_X +O_X <=> NH2_X + OH_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251
This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 5.2E12(1/s)/2.483E-9(mol/cm^2)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 49,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(4.83e+20,'cm^2/(mol*s)'), n=0, Ea=(42,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Pt111
Original entry: NH3_X +O_X <=> NH2_X + OH_X
"Ammonia Dissociation on Pt(100), Pt(111), and Pt(211): A Comparative Density Functional Theory Study"
W. K. Offermans, A. P. J. Jansen, R. A. van Santen, G. Novell-Leruth, J. M. Ricart, and J. Pérez-Ramírez
The Journal of Physical Chemistry C 2007 111 (47), 17551-17557
https://doi.org/10.1021/jp073083f
This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.2E12(1/s)/2.483E-9(mol/cm^2)
""",
    metal = "Pt",
    facet = "111",
)

