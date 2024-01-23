from pickledb import PickleDB
import os

DB_PATH = './database.db'

class EnumPrType():
    OTHER = 0
    DATA_SCIENCE = 1
    DATABASE = 2
    DESKTOP = 3
    GAME = 4
    MOBILE = 5
    SCRIPT = 6
    WEB = 7
    EMBEDED = 8

class EnumUI():
    MAIN = 0
    PR_TYPE = 1
    FORM = 2
    EXP = 3
    RESULTS = 4

class EnumLenType():
    SCRIPTED = 0
    COMPILED = 1
    INTERPRETED = 2

class EnumSize():
    TINY = 0
    SMALL = 1
    REGULAR = 2
    BIG = 3

class LanguageInferenceSystem:
    languagesDB: PickleDB
    userData = {"projectType": None,
                "modernity": None,
                "performance": None,
                "complexity": None,
                "scalability": None,
                "popularity": None,
                "experienced": None,
                "lenType": None,
                "experience": {}}

    def __init__(self):
        if os.path.exists(DB_PATH):
            # Load existing database
            self.languagesDB = PickleDB(DB_PATH, auto_dump=True, sig=True)
            print(f"Loaded existing database '{DB_PATH}'")
        else:
            self.languagesDB = self.generateDatabase()

        # test data
        if self.languagesDB.totalkeys() != 20:
            print("Database failure")
            exit()

    def run(self):
        scores = {}
        results=[]
        for language in self.languagesDB.getall():
            scores[language] = self.calculateScore(language)

        sorted_languages = sorted(scores, key=lambda lang: scores[lang], reverse=True)
        print(scores)
        for index in range(0, 5):
            results.append(self.parseLanguage(index+1, sorted_languages[index]))
        return results
    
    def calculateScore(self, language):
        languageData = self.languagesDB.get(language)
        score = 0

        if self.userData["projectType"] == 0 or self.userData["projectType"] in languageData["Project type"]:
            score += 1
        if self.userData["modernity"] != None:
            score += self.userData["modernity"] * languageData["Modernity"] * 0.1
        if self.userData["performance"] != None:
            score += self.userData["performance"] * languageData["Performance"] * 0.1
        if self.userData["complexity"] is None or (len(languageData["Complexity"]) and self.userData["complexity"] == languageData["Complexity"]):
            score += 1
        else:
            for complexity in languageData["Complexity"]:
                if self.userData["complexity"] == complexity + 1 or self.userData["complexity"] == complexity - 1:
                    score += 0.5
                    break
        if self.userData["scalability"] != None:
            score += self.userData["scalability"] * languageData["Scalability"] * 0.1
        if self.userData["popularity"] != None:
            score += self.userData["popularity"] * languageData["Popularity"] * 0.1
        if self.userData["lenType"] is None or self.userData["lenType"] == languageData["Language type"]:
            score += 5
        if self.userData["experienced"] != None and self.userData["experienced"] and language in self.userData["experience"]:
            score += self.userData["experience"][language]/100
        
        return score

    def parseLanguage(self, index, language):
        dict = self.languagesDB.get(language)
        match dict['Language type']:
            case 0:
                dict['Language type'] = "scripted"
            case 1:
                dict['Language type'] = "complied"
            case 2:
                dict['Language type'] = "interpreted"
        complexity = []
        for complex in dict['Complexity']:
            match complex:
                case 0:
                    complexity.append("tiny")
                case 1:
                    complexity.append("small")
                case 2:
                    complexity.append("regular")
                case 3:
                    complexity.append("big")
        dict['Complexity'] = complexity
        types = []
        for type in dict['Project type']:
            match type:
                case 1:
                    types.append("data science")
                case 2:
                    types.append("database")
                case 3:
                    types.append("desktop")
                case 4:
                    types.append("game")
                case 5:
                    types.append("mobile")
                case 6:
                    types.append("script")
                case 7:
                    types.append("web")
                case 8:
                    types.append("embeded/IoT")

        dict['Project type'] = types

        output = (f"{index}. {language} |\n\tTOP#{dict['PopularityTop']} in January 2024, type: {dict['Language type']}, modernity: {dict['Modernity']}/10, "
        f"performance: {dict['Performance']}/10, scalability: {dict['Scalability']}/10,\n\tRecommended for {dict['Complexity']} {dict['Project type']} projects")
        return output

    def generateDatabase(self):
        # Create a database instance
        db = PickleDB(DB_PATH, auto_dump=True, sig=True)

        # Insert data
        db.set('Python', {'Language type': EnumLenType.INTERPRETED, 'Modernity': 9, 'Performance': 8, 'Complexity': [EnumSize.TINY, EnumSize.SMALL, EnumSize.REGULAR], 'Scalability': 7, 'Popularity': 10.0, 'PopularityTop': 1, 'Project type': [EnumPrType.DATA_SCIENCE, EnumPrType.DATABASE, EnumPrType.DESKTOP, EnumPrType.GAME, EnumPrType.MOBILE, EnumPrType.SCRIPT, EnumPrType.WEB, EnumPrType.EMBEDED]})
        db.set('C', {'Language type': EnumLenType.COMPILED, 'Modernity': 5, 'Performance': 9, 'Complexity': [EnumSize.SMALL, EnumSize.REGULAR, EnumSize.BIG], 'Scalability': 8, 'Popularity': 8.18, 'PopularityTop': 2, 'Project type': [EnumPrType.DATABASE, EnumPrType.DESKTOP, EnumPrType.EMBEDED]})
        db.set('C++', {'Language type': EnumLenType.COMPILED, 'Modernity': 7, 'Performance': 8, 'Complexity': [EnumSize.REGULAR, EnumSize.BIG], 'Scalability': 7, 'Popularity': 7.13, 'PopularityTop': 3, 'Project type': [EnumPrType.DATABASE, EnumPrType.DESKTOP, EnumPrType.GAME, EnumPrType.EMBEDED]})
        db.set('Java', {'Language type': EnumLenType.COMPILED, 'Modernity': 8, 'Performance': 7, 'Complexity': [EnumSize.REGULAR, EnumSize.BIG], 'Scalability': 8, 'Popularity': 5.63, 'PopularityTop': 4, 'Project type': [EnumPrType.DATABASE, EnumPrType.DESKTOP, EnumPrType.MOBILE, EnumPrType.WEB, EnumPrType.EMBEDED]})
        db.set('C#', {'Language type': EnumLenType.COMPILED, 'Modernity': 7, 'Performance': 7, 'Complexity': [EnumSize.SMALL, EnumSize.REGULAR, EnumSize.BIG], 'Scalability': 7, 'Popularity': 5.13, 'PopularityTop': 5, 'Project type': [EnumPrType.DATABASE, EnumPrType.DESKTOP, EnumPrType.MOBILE, EnumPrType.SCRIPT, EnumPrType.WEB, EnumPrType.EMBEDED]})
        db.set('Javascript', {'Language type': EnumLenType.INTERPRETED, 'Modernity': 8, 'Performance': 6, 'Complexity': [EnumSize.TINY, EnumSize.SMALL, EnumSize.REGULAR], 'Scalability': 6, 'Popularity': 1.98, 'PopularityTop': 6, 'Project type': [EnumPrType.DATABASE, EnumPrType.MOBILE, EnumPrType.SCRIPT, EnumPrType.WEB, EnumPrType.EMBEDED]})
        db.set('PHP', {'Language type': EnumLenType.SCRIPTED, 'Modernity': 6, 'Performance': 5, 'Complexity': [EnumSize.TINY, EnumSize.SMALL, EnumSize.REGULAR], 'Scalability': 6, 'Popularity': 1.28, 'PopularityTop': 7, 'Project type': [EnumPrType.DATABASE, EnumPrType.WEB]})
        db.set('VisualBasic', {'Language type': EnumLenType.COMPILED, 'Modernity': 4, 'Performance': 5, 'Complexity': [EnumSize.TINY, EnumSize.SMALL], 'Scalability': 4, 'Popularity': 1.15, 'PopularityTop': 8, 'Project type': [EnumPrType.DESKTOP]})
        db.set('SQL', {'Language type': EnumLenType.SCRIPTED, 'Modernity': 6, 'Performance': 7, 'Complexity': [EnumSize.TINY, EnumSize.SMALL], 'Scalability': 8, 'Popularity': 1.05, 'PopularityTop': 9, 'Project type': [EnumPrType.DATABASE]})
        db.set('Scratch', {'Language type': EnumLenType.INTERPRETED, 'Modernity': 8, 'Performance': 4, 'Complexity': [EnumSize.TINY], 'Scalability': 3, 'Popularity': 1.03, 'PopularityTop': 10, 'Project type': [EnumPrType.GAME]})
        db.set('GO', {'Language type': EnumLenType.COMPILED, 'Modernity': 8, 'Performance': 8, 'Complexity': [EnumSize.SMALL, EnumSize.REGULAR], 'Scalability': 9, 'Popularity': 0.99, 'PopularityTop': 11, 'Project type': [EnumPrType.DATABASE, EnumPrType.SCRIPT, EnumPrType.WEB, EnumPrType.EMBEDED]})
        db.set('Fortran', {'Language type': EnumLenType.COMPILED, 'Modernity': 2, 'Performance': 8, 'Complexity': [EnumSize.REGULAR, EnumSize.BIG], 'Scalability': 5, 'Popularity': 0.78, 'PopularityTop': 12, 'Project type': [EnumPrType.DATA_SCIENCE]})
        db.set('Delphi', {'Language type': EnumLenType.COMPILED, 'Modernity': 3, 'Performance': 6, 'Complexity': [EnumSize.SMALL, EnumSize.REGULAR], 'Scalability': 4, 'Popularity': 0.78, 'PopularityTop': 13, 'Project type': [EnumPrType.DESKTOP]})
        db.set('MATLAB', {'Language type': EnumLenType.INTERPRETED, 'Modernity': 6, 'Performance': 6, 'Complexity': [EnumSize.TINY, EnumSize.SMALL, EnumSize.REGULAR], 'Scalability': 6, 'Popularity': 0.69, 'PopularityTop': 14, 'Project type': [EnumPrType.DATA_SCIENCE]})
        db.set('Assembly', {'Language type': EnumLenType.COMPILED, 'Modernity': 2, 'Performance': 9, 'Complexity': [EnumSize.TINY, EnumSize.SMALL], 'Scalability': 4, 'Popularity': 0.66, 'PopularityTop': 15, 'Project type': [EnumPrType.EMBEDED]})
        db.set('Swift', {'Language type': EnumLenType.COMPILED, 'Modernity': 8, 'Performance': 7, 'Complexity': [EnumSize.REGULAR, EnumSize.BIG], 'Scalability': 7, 'Popularity': 0.64, 'PopularityTop': 16, 'Project type': [EnumPrType.MOBILE]})
        db.set('Kotlin', {'Language type': EnumLenType.COMPILED, 'Modernity': 7, 'Performance': 7, 'Complexity': [EnumSize.REGULAR, EnumSize.BIG], 'Scalability': 7, 'Popularity': 0.61, 'PopularityTop': 17, 'Project type': [EnumPrType.MOBILE, EnumPrType.WEB]})
        db.set('Ruby', {'Language type': EnumLenType.INTERPRETED, 'Modernity': 7, 'Performance': 5, 'Complexity': [EnumSize.TINY, EnumSize.SMALL, EnumSize.REGULAR], 'Scalability': 6, 'Popularity': 0.57, 'PopularityTop': 18, 'Project type': [EnumPrType.SCRIPT, EnumPrType.WEB]})
        db.set('Rust', {'Language type': EnumLenType.COMPILED, 'Modernity': 8, 'Performance': 8, 'Complexity': [EnumSize.REGULAR, EnumSize.BIG], 'Scalability': 8, 'Popularity': 0.57, 'PopularityTop': 19, 'Project type': [EnumPrType.DESKTOP, EnumPrType.EMBEDED]})
        db.set('COBOL', {'Language type': EnumLenType.COMPILED, 'Modernity': 1, 'Performance': 4, 'Complexity': [EnumSize.BIG], 'Scalability': 4, 'Popularity': 0.56, 'PopularityTop': 20, 'Project type': [EnumPrType.DATABASE]})
        print(f"Database created '{DB_PATH}'")

        return db
    