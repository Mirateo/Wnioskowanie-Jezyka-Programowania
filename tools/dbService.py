from pickledb import PickleDB
import os
from .Enums import EnumLenType, EnumPrType, EnumSize

DB_PATH = './database.db'

"""
generateDatabase function.

This function generates a database of programming languages with their attributes such as
language type, modernity, performance, complexity, scalability, popularity, popularity top rank
and project type.

Returns:
    PickleDB: The generated database of programming languages.
"""
def generateDatabase():
    # Load existing database if exists
    if os.path.exists(DB_PATH):
        languagesDB = PickleDB(DB_PATH, auto_dump=True, sig=True)
        print(f"Loaded existing database '{DB_PATH}'")
        return languagesDB

    # Create a database instance
    db = PickleDB(DB_PATH, auto_dump=True, sig=True)

    # Insert data
    db.set(
        "Python",
        {
            "Language type": EnumLenType.INTERPRETED,
            "Modernity": 9,
            "Performance": 8,
            "Complexity": [EnumSize.TINY, EnumSize.SMALL, EnumSize.REGULAR],
            "Scalability": 7,
            "Popularity": 10.0,
            "PopularityTop": 1,
            "Project type": [
                EnumPrType.DATA_SCIENCE,
                EnumPrType.DATABASE,
                EnumPrType.DESKTOP,
                EnumPrType.GAME,
                EnumPrType.MOBILE,
                EnumPrType.SCRIPT,
                EnumPrType.WEB,
                EnumPrType.EMBEDDED,
            ],
        },
    )
    db.set(
        "C",
        {
            "Language type": EnumLenType.COMPILED,
            "Modernity": 5,
            "Performance": 9,
            "Complexity": [EnumSize.SMALL, EnumSize.REGULAR, EnumSize.BIG],
            "Scalability": 8,
            "Popularity": 8.18,
            "PopularityTop": 2,
            "Project type": [EnumPrType.DATABASE, EnumPrType.DESKTOP, EnumPrType.EMBEDDED],
        },
    )
    db.set(
        "C++",
        {
            "Language type": EnumLenType.COMPILED,
            "Modernity": 7,
            "Performance": 8,
            "Complexity": [EnumSize.REGULAR, EnumSize.BIG],
            "Scalability": 7,
            "Popularity": 7.13,
            "PopularityTop": 3,
            "Project type": [
                EnumPrType.DATABASE,
                EnumPrType.DESKTOP,
                EnumPrType.GAME,
                EnumPrType.EMBEDDED,
            ],
        },
    )
    db.set(
        "Java",
        {
            "Language type": EnumLenType.COMPILED,
            "Modernity": 8,
            "Performance": 7,
            "Complexity": [EnumSize.REGULAR, EnumSize.BIG],
            "Scalability": 8,
            "Popularity": 5.63,
            "PopularityTop": 4,
            "Project type": [
                EnumPrType.DATABASE,
                EnumPrType.DESKTOP,
                EnumPrType.MOBILE,
                EnumPrType.WEB,
                EnumPrType.EMBEDDED,
            ],
        },
    )
    db.set(
        "C#",
        {
            "Language type": EnumLenType.COMPILED,
            "Modernity": 7,
            "Performance": 7,
            "Complexity": [EnumSize.SMALL, EnumSize.REGULAR, EnumSize.BIG],
            "Scalability": 7,
            "Popularity": 5.13,
            "PopularityTop": 5,
            "Project type": [
                EnumPrType.DATABASE,
                EnumPrType.DESKTOP,
                EnumPrType.MOBILE,
                EnumPrType.SCRIPT,
                EnumPrType.WEB,
                EnumPrType.EMBEDDED,
            ],
        },
    )
    db.set(
        "Javascript",
        {
            "Language type": EnumLenType.INTERPRETED,
            "Modernity": 8,
            "Performance": 6,
            "Complexity": [EnumSize.TINY, EnumSize.SMALL, EnumSize.REGULAR],
            "Scalability": 6,
            "Popularity": 1.98,
            "PopularityTop": 6,
            "Project type": [
                EnumPrType.DATABASE,
                EnumPrType.MOBILE,
                EnumPrType.SCRIPT,
                EnumPrType.WEB,
                EnumPrType.EMBEDDED,
            ],
        },
    )
    db.set(
        "PHP",
        {
            "Language type": EnumLenType.SCRIPTED,
            "Modernity": 6,
            "Performance": 5,
            "Complexity": [EnumSize.TINY, EnumSize.SMALL, EnumSize.REGULAR],
            "Scalability": 6,
            "Popularity": 1.28,
            "PopularityTop": 7,
            "Project type": [EnumPrType.DATABASE, EnumPrType.WEB],
        },
    )
    db.set(
        "VisualBasic",
        {
            "Language type": EnumLenType.COMPILED,
            "Modernity": 4,
            "Performance": 5,
            "Complexity": [EnumSize.TINY, EnumSize.SMALL],
            "Scalability": 4,
            "Popularity": 1.15,
            "PopularityTop": 8,
            "Project type": [EnumPrType.DESKTOP],
        },
    )
    db.set(
        "SQL",
        {
            "Language type": EnumLenType.SCRIPTED,
            "Modernity": 6,
            "Performance": 7,
            "Complexity": [EnumSize.TINY, EnumSize.SMALL],
            "Scalability": 8,
            "Popularity": 1.05,
            "PopularityTop": 9,
            "Project type": [EnumPrType.DATABASE],
        },
    )
    db.set(
        "Scratch",
        {
            "Language type": EnumLenType.INTERPRETED,
            "Modernity": 8,
            "Performance": 4,
            "Complexity": [EnumSize.TINY],
            "Scalability": 3,
            "Popularity": 1.03,
            "PopularityTop": 10,
            "Project type": [EnumPrType.GAME],
        },
    )
    db.set(
        "GO",
        {
            "Language type": EnumLenType.COMPILED,
            "Modernity": 8,
            "Performance": 8,
            "Complexity": [EnumSize.SMALL, EnumSize.REGULAR],
            "Scalability": 9,
            "Popularity": 0.99,
            "PopularityTop": 11,
            "Project type": [
                EnumPrType.DATABASE,
                EnumPrType.SCRIPT,
                EnumPrType.WEB,
                EnumPrType.EMBEDDED,
            ],
        },
    )
    db.set(
        "Fortran",
        {
            "Language type": EnumLenType.COMPILED,
            "Modernity": 2,
            "Performance": 8,
            "Complexity": [EnumSize.REGULAR, EnumSize.BIG],
            "Scalability": 5,
            "Popularity": 0.78,
            "PopularityTop": 12,
            "Project type": [EnumPrType.DATA_SCIENCE],
        },
    )
    db.set(
        "Delphi",
        {
            "Language type": EnumLenType.COMPILED,
            "Modernity": 3,
            "Performance": 6,
            "Complexity": [EnumSize.SMALL, EnumSize.REGULAR],
            "Scalability": 4,
            "Popularity": 0.78,
            "PopularityTop": 13,
            "Project type": [EnumPrType.DESKTOP],
        },
    )
    db.set(
        "MATLAB",
        {
            "Language type": EnumLenType.INTERPRETED,
            "Modernity": 6,
            "Performance": 6,
            "Complexity": [EnumSize.TINY, EnumSize.SMALL, EnumSize.REGULAR],
            "Scalability": 6,
            "Popularity": 0.69,
            "PopularityTop": 14,
            "Project type": [EnumPrType.DATA_SCIENCE],
        },
    )
    db.set(
        "Assembly",
        {
            "Language type": EnumLenType.COMPILED,
            "Modernity": 2,
            "Performance": 9,
            "Complexity": [EnumSize.TINY, EnumSize.SMALL],
            "Scalability": 4,
            "Popularity": 0.66,
            "PopularityTop": 15,
            "Project type": [EnumPrType.EMBEDDED],
        },
    )
    db.set(
        "Swift",
        {
            "Language type": EnumLenType.COMPILED,
            "Modernity": 8,
            "Performance": 7,
            "Complexity": [EnumSize.REGULAR, EnumSize.BIG],
            "Scalability": 7,
            "Popularity": 0.64,
            "PopularityTop": 16,
            "Project type": [EnumPrType.MOBILE],
        },
    )
    db.set(
        "Kotlin",
        {
            "Language type": EnumLenType.COMPILED,
            "Modernity": 7,
            "Performance": 7,
            "Complexity": [EnumSize.REGULAR, EnumSize.BIG],
            "Scalability": 7,
            "Popularity": 0.61,
            "PopularityTop": 17,
            "Project type": [EnumPrType.MOBILE, EnumPrType.WEB],
        },
    )
    db.set(
        "Ruby",
        {
            "Language type": EnumLenType.INTERPRETED,
            "Modernity": 7,
            "Performance": 5,
            "Complexity": [EnumSize.TINY, EnumSize.SMALL, EnumSize.REGULAR],
            "Scalability": 6,
            "Popularity": 0.57,
            "PopularityTop": 18,
            "Project type": [EnumPrType.SCRIPT, EnumPrType.WEB],
        },
    )
    db.set(
        "Rust",
        {
            "Language type": EnumLenType.COMPILED,
            "Modernity": 8,
            "Performance": 8,
            "Complexity": [EnumSize.REGULAR, EnumSize.BIG],
            "Scalability": 8,
            "Popularity": 0.57,
            "PopularityTop": 19,
            "Project type": [EnumPrType.DESKTOP, EnumPrType.EMBEDDED],
        },
    )
    db.set(
        "COBOL",
        {
            "Language type": EnumLenType.COMPILED,
            "Modernity": 1,
            "Performance": 4,
            "Complexity": [EnumSize.BIG],
            "Scalability": 4,
            "Popularity": 0.56,
            "PopularityTop": 20,
            "Project type": [EnumPrType.DATABASE],
        },
    )
    print(f"Database created '{DB_PATH}'")
    return db
