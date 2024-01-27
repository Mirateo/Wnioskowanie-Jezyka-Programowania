"""
======================= START OF LICENSE NOTICE =======================
  Copyright (C) 2024 Mateusz Murawski. All Rights Reserved
======================== END OF LICENSE NOTICE ========================
"""
"""
EnumPrType class.
This class represents an enumeration of project types.
"""
class EnumPrType():
    OTHER = 0
    DATA_SCIENCE = 1
    DATABASE = 2
    DESKTOP = 3
    GAME = 4
    MOBILE = 5
    SCRIPT = 6
    WEB = 7
    EMBEDDED = 8

"""
EnumUI class.

This class represents an enumeration of user interface states.
"""
class EnumUI():
    MAIN = 0
    PR_TYPE = 1
    FORM = 2
    EXP = 3
    RESULTS = 4

"""
EnumLenType class.

This class represents an enumeration of language types.
"""
class EnumLenType():
    SCRIPTED = 0
    COMPILED = 1
    INTERPRETED = 2

"""
EnumSize class.

This class represents an enumeration of size categories.
"""
class EnumSize():
    TINY = 0
    SMALL = 1
    REGULAR = 2
    BIG = 3