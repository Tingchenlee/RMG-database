#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "X + H3N <=> H3NX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.025, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Pt211_oxidation
Original entry: NH3 + X <=> NH3_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251
The pressure of adsorption processes: P= 1 bar = 10E5 Pa
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 2,
    label = "X + H2O <=> H2OX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.024, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Pt211_oxidation
Original entry: H2O + X <=> H2O_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251
The pressure of adsorption processes: P= 1 bar = 10E5 Pa
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 3,
    label = "X + N2O <=> N2OX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.016, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Double/Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Pt211_oxidation
Original entry: N2O + X <=> N2O_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251
The pressure of adsorption processes: P= 1 bar = 10E5 Pa
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 4,
    label = "X + H3N <=> H3NX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.025, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Pt111_oxidation
Original entry: NH3 + X <=> NH3_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251
The pressure of adsorption processes: P= 1 bar = 10E5 Pa
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 5,
    label = "X + H2O <=> H2OX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.024, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Pt111_oxidation
Original entry: H2O + X <=> H2O_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251
The pressure of adsorption processes: P= 1 bar = 10E5 Pa
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 6,
    label = "X + N2O <=> N2OX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.016, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Double/Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Pt111_oxidation
Original entry: N2O + X <=> N2O_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251
The pressure of adsorption processes: P= 1 bar = 10E5 Pa
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 5,
    label = "H2O + X <=> H2OX",
    kinetics = StickingCoefficient(
        A = 1.0E-1,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R5
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	metal = "Ni",
)

entry(
    index = 7,
    label = "CO2 + X <=> CO2X",
    kinetics = StickingCoefficient(
        A = 7.0E-6,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R7
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	metal = "Ni",
)

entry(
    index = 11,
    label = "CH4 + X <=> CH4X",
    kinetics = StickingCoefficient(
        A = 8.0E-3,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R11
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	metal = "Ni",
)
