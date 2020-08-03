#!/usr/bin/env python
# encoding: utf-8

name = "Retroene/training"
shortDesc = "Retroene reaction family"
longDesc = """
Training reactions for retroene reaction family.
Some species are marked as '(rxnX)' to allow it to match different template.
"""
entry(
    index = 0,
    label = "nBA <=> C4H8-1 + AcOH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3496.64,'s^-1'), n=2.72265, Ea=(192.668,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.90869, dn = +|- 0.0858988, dEa = +|- 0.439996 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 by Xiaorui Dong.""",
)

entry(
    index = 1,
    label = "iBA <=> iC4H8(rxn2) + AcOH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.16053e+06,'s^-1'), n=1.87467, Ea=(202.966,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.39386, dn = +|- 0.0441278, dEa = +|- 0.226034 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 by Xiaorui Dong.""",
)

entry(
    index = 2,
    label = "sBA(rxn1) <=> C4H8-1 + AcOH",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3.8952e+07,'s^-1'), n=1.63805, Ea=(190.506,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.44153, dn = +|- 0.0485968, dEa = +|- 0.248926 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 by Xiaorui Dong.""",
)

entry(
    index = 3,
    label = "tBA <=> iC4H8(rxn1) + AcOH",
    degeneracy = 9.0,
    kinetics = Arrhenius(A=(3.89757e+09,'s^-1'), n=1.19379, Ea=(176.117,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 200 data points; dA = *|/ 1.13961, dn = +|- 0.0173664, dEa = +|- 0.0889553 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 by Xiaorui Dong.""",
)

entry(
    index = 4,
    label = "sBA(rxn2) <=> C4H8-2 + AcOH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.16601e+09,'1/s'), n=1.07561, Ea=(193.552,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to Multiple Arrhenius kinetics over range 300.0-2000.0 K. """),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 by Xiaorui Dong.""",
    longDesc = 
"""
There are two different TS conformers (cis and trans) related to different H atom
reacting. The kinetics is fitted from the sum of the individual rate coeffs.
""",
)

entry(
    index = 5,
    label = "C5H10 <=> C3H6 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(8.7e+11,'1/s'), n=0, Ea=(233,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3 by Florence Vermeire""",
)

entry(
    index = 6,
    label = "C6H12 <=> C3H6 + C3H6",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(7.1e+11,'1/s'), n=0, Ea=(226,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3 by Florence Vermeire""",
)

entry(
    index = 7,
    label = "C6H12-2 <=> C4H8 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(9.7e+11,'1/s'), n=0, Ea=(238,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3 by Florence Vermeire""",
)

entry(
    index = 8,
    label = "C7H12 <=> C3H6 + C4H6",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(9.1e+11,'1/s'), n=0, Ea=(205,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3 by Florence Vermeire""",
)

entry(
    index = 9,
    label = "C8H14O2 <=> C3H6 + C5H8O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1e+12,'1/s'), n=0, Ea=(223,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3 by Florence Vermeire""",
)

entry(
    index = 10,
    label = "C7H12O2 <=> C3H6 + C4H6O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(6.7e+10,'1/s'), n=0, Ea=(198,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3 by Florence Vermeire""",
)

entry(
    index = 11,
    label = "C8H14O2-2 <=> C4H8 + C4H6O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.3e+11,'1/s'), n=0, Ea=(205,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3 by Florence Vermeire""",
)

entry(
    index = 12,
    label = "C4H6O2-2 <=> C3H4O + CH2O",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(8.4e+12,'1/s'), n=0, Ea=(272,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3 by Florence Vermeire""",
)

entry(
    index = 13,
    label = "C4H9N <=> C3H6 + CH3N",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2.34423e+11,'1/s'), n=0, Ea=(181.5,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 9,
    shortDesc = """Measured from experiment""",
    longDesc=
"""
Cited from: Vitins P, Egger K W. The thermochemical kinetics of the retro-‘ene’reactions of
molecules with the general structure (allyl) XYH in the gas phase. Part IX.
Unimolecular thermal decompostion of allylmethylamine[J]. Journal of the Chemical
Society, Perkin Transactions 2, 1974 (11): 1289-1291.
""",
)

entry(
    index = 14,
    label = "C4H8O <=> C3H6 + CH2O",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.23027e+11,'1/s'), n=0, Ea=(174.05,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 9,
    shortDesc="""Measured from experiment""",
    longDesc="""
Cited from: Kwart H, Sarner S F, Slutsky J. Mechanisms of thermolytic fragmentation of allyl
ethers. I[J]. Journal of the American Chemical Society, 1973, 95(16): 5234-5242.
""",
)

entry(
    index = 15,
    label = "C4H8S <=> C3H6 + CH2S",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.69824e+11,'1/s'), n=0, Ea=(160,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 9,
    shortDesc="""Measured from experiment""",
    longDesc="""
Cited from: Kwart H, Sarner S F, Slutsky J. Mechanisms of thermolytic fragmentation of allyl
ethers. I[J]. Journal of the American Chemical Society, 1973, 95(16): 5234-5242.
""",
)

entry(
    index = 16,
    label = "C4H8O-2 <=> C2H4O + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1e+08,'1/s'), n=1.2, Ea=(44,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3""",
    longDesc="""
Cited from: Jarvis, M. W., Daily, J. W., Carstensen, H. H., Dean, A. M., Sharma, S., Dayton,
D. C., ... & Nimlos, M. R. (2011). Direct detection of products from the pyrolysis
of 2-phenethyl phenyl ether. The Journal of Physical Chemistry A, 115(4), 428-438.
""",
)

entry(
    index = 17,
    label = "C8H10O <=> C6H6O + C2H4",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(5.5e+07,'1/s'), n=1.6, Ea=(54,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3""",
    longDesc="""
Cited from: Jarvis, M. W., Daily, J. W., Carstensen, H. H., Dean, A. M., Sharma, S., Dayton,
D. C., ... & Nimlos, M. R. (2011). Direct detection of products from the pyrolysis
of 2-phenethyl phenyl ether. The Journal of Physical Chemistry A, 115(4), 428-438.
""",
)

entry(
    index = 18,
    label = "C5H10O2 <=> AcOH + C3H6-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(7.94328e+12,'1/s'), n=0, Ea=(44.7,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 19,
    label = "C14H14O <=> C6H6O + C8H8",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(2.2e+06,'1/s'), n=0.9, Ea=(49,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at CBS-QB3""",
    longDesc="""
Cited from: Jarvis, M. W., Daily, J. W., Carstensen, H. H., Dean, A. M., Sharma, S., Dayton,
D. C., ... & Nimlos, M. R. (2011). Direct detection of products from the pyrolysis
of 2-phenethyl phenyl ether. The Journal of Physical Chemistry A, 115(4), 428-438.
""",
)

entry(
    index = 20,
    label = "C7H14O2 <=> AcOH + C5H10-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(8.91251e+12,'1/s'), n=0, Ea=(39.4,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc="""Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 21,
    label = "C7H14O2-2 <=> C3H6O2 + iC4H8(rxn1)",
    degeneracy = 9.0,
    kinetics = Arrhenius(A=(1.25893e+13,'1/s'), n=0, Ea=(40,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc="""Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 22,
    label = "C7H12O3 <=> AcOH + C5H8O",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3.98107e+11,'1/s'), n=0, Ea=(36.6,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc="""Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 23,
    label = "C7H12O2-2 <=> AcOH + C5H8",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2.51189e+12,'1/s'), n=0, Ea=(43.9,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc="""Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 24,
    label = "C7H12O2-3 <=> AcOH + C5H8-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.98107e+12,'1/s'), n=0, Ea=(43.9,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc="""Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 25,
    label = "C4H6O3 <=> AcOH + C2H2O",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(3.98107e+12,'1/s'), n=0, Ea=(36.1,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc="""Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 26,
    label = "C10H12O2 <=> AcOH + C8H8-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3.98107e+12,'1/s'), n=0, Ea=(43.7,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc="""Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 27,
    label = "C10H12O2-2 <=> AcOH + C8H8",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.58489e+12,'1/s'), n=0, Ea=(45.1,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc="""Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 28,
    label = "C16H16O2 <=> AcOH + C14H12",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.51189e+12,'1/s'), n=0, Ea=(41.7,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 3,
    shortDesc="""Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 29,
    label = "C4H8O2 <=> CH2O2 + C3H6-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(6.30957e+12,'1/s'), n=0, Ea=(44.8,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc="""Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 30,
    label = "C5H10O2-2 <=> CH2O2 + iC4H8(rxn1)",
    degeneracy = 9.0,
    kinetics = Arrhenius(A=(1e+13,'1/s'), n=0, Ea=(39.3,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc="""Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 31,
    label = "C5H10O2-3 <=> AcOH + C3H6-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.99526e+12,'1/s'), n=0, Ea=(47.4,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc="""Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 32,
    label = "C7H14O2-3 <=> AcOH + C5H10-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.58489e+12,'1/s'), n=0, Ea=(46.4,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc="""Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 33,
    label = "C7H14O2-4 <=> AcOH + C5H10-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.58489e+12,'1/s'), n=0, Ea=(46.4,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc="""Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 34,
    label = "C8H16O2 <=> AcOH + C6H12-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.94328e+11,'1/s'), n=0, Ea=(45.8,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc="""Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 35,
    label = "C5H10O3 <=> AcOH + C3H6O",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.58489e+12,'1/s'), n=0, Ea=(48.6,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc="""Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 36,
    label = "C6H12O3 <=> AcOH + C4H8O-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.58489e+12,'1/s'), n=0, Ea=(48.3,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc="""Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 37,
    label = "C7H14O2-5 <=> AcOH + C5H10-5",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.23872e+12,'1/s'), n=0, Ea=(43.8,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc="""Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 38,
    label = "C7H14O2-6 <=> AcOH + C5H10-6",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3.98107e+12,'1/s'), n=0, Ea=(43.8,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc="""Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 39,
    label = "C7H14O2-7 <=> AcOH + C5H10-7",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(7.94328e+12,'1/s'), n=0, Ea=(44.1,'kcal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc="""Estimated by group additivity approach""",
    longDesc="""
Cited from: O'Neal, H., & Benson, S. (1967). A method for estimating the Arrhenius a factors for
four-and six-center unimolecular reactions. The Journal of Physical Chemistry, 71(9), 2903-2921.
""",
)

entry(
    index = 40,
    label = "C3H6O2-2 <=> CH2O2 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.19e+11,'1/s'), n=0.59, Ea=(49800,'cal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """calculated at CCSD(T)/CBS//M06-2X/cc-pVTZ""",
    longDesc = 
"""
Cited from: Sun, W., Tao, T., Zhang, R., Liao, H., Huang, C., Zhang, F., ... & Yang, B. (2017).
Experimental and modeling efforts towards a better understanding of the high-temperature
combustion kinetics of C3C5 ethyl esters. Combustion and Flame, 185, 173-187. The original data
is P-dep, and the rate coeff. recorded in this library is the rate coeff. for 100 atm.
""",
)

entry(
    index = 41,
    label = "C4H8O2-2 <=> AcOH + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.36e+14,'1/s'), n=-0.3, Ea=(49900,'cal/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """calculated at CCSD(T)/CBS//M06-2X/cc-pVTZ""",
    longDesc = 
"""
Cited from: Sun, W., Tao, T., Zhang, R., Liao, H., Huang, C., Zhang, F., ... & Yang, B. (2017).
Experimental and modeling efforts towards a better understanding of the high-temperature
combustion kinetics of C3C5 ethyl esters. Combustion and Flame, 185, 173-187. The original data
is P-dep, and the rate coeff. recorded in this library is the rate coeff. for 100 atm.
""",
)

entry(
    index = 42,
    label = "C5H10O2-4 <=> C3H6O2 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(6.93e+08,'1/s'), n=1.27, Ea=(48500,'cal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """calculated at CCSD(T)/CBS//M06-2X/cc-pVTZ""",
    longDesc = 
"""
Cited from: Sun, W., Tao, T., Zhang, R., Liao, H., Huang, C., Zhang, F., ... & Yang, B. (2017).
Experimental and modeling efforts towards a better understanding of the high-temperature
combustion kinetics of C3C5 ethyl esters. Combustion and Flame, 185, 173-187. The original data
is P-dep, and the rate coeff. recorded in this library is the rate coeff. for 100 atm.
""",
)

entry(
    index = 43,
    label = "C7H12O3-2 <=> C5H8O3 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2.0893e+13,'1/s'), n=0, Ea=(49518,'cal/mol'), T0=(1,'K'), Tmin=(900,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """calculated at G3//MP2/aug-cc-pVDZ""",
    longDesc = 
"""
AlAbbad, M., Giri, B. R., Szőri, M., & Farooq, A. (2017). On the high-temperature
unimolecular decomposition of ethyl levulinate. Proceedings of the Combustion
Institute, 36(1), 187-193.
""",
)

entry(
    index = 44,
    label = "C5H10O3-2 <=> C3H6O3 + C2H4",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(348015,'1/s'), n=0.286, Ea=(158771,'J/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(1300,'K')),
    rank = 5,
    shortDesc = """calculated at G3//MP2/aug-cc-pVDZ""",
    longDesc = 
"""
AlAbbad, M., Giri, B. R., Szőri, M., Viskolcz, B., & Farooq, A. (2017). A high
temperature kinetic study for the thermal unimolecular decomposition of diethyl
carbonate. Chemical Physics Letters, 684, 390-396.
""",
)

