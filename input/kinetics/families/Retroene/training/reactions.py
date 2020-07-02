#!/usr/bin/env python
# encoding: utf-8

name = "Retroene/training"
shortDesc = "Retroene reaction family"
longDesc = """
Data of retroene reactions which are calculated by Xiaorui Dong.
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
    kinetics=Arrhenius(A=(3.16053e+06, 's^-1'), n=1.87467, Ea=(202.966, 'kJ/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(
        2000, 'K'), comment="""Fitted to 200 data points; dA = *|/ 1.39386, dn = +|- 0.0441278, dEa = +|- 0.226034 kJ/mol"""),
    rank = 5,
    shortDesc = """Calculated at CBS-QB3 by Xiaorui Dong.""",
)

entry(
    index = 2,
    label = "sBA(rxn1) <=> C4H8-1 + AcOH",
    degeneracy = 3.0,
    kinetics=Arrhenius(A=(3.8952e+07, 's^-1'), n=1.63805, Ea=(190.506, 'kJ/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(
        2000, 'K'), comment="""Fitted to 200 data points; dA = *|/ 1.44153, dn = +|- 0.0485968, dEa = +|- 0.248926 kJ/mol"""),
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

