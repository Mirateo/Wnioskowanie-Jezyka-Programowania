from tools.dbService import generateDatabase
from pickledb import PickleDB

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
        self.languagesDB = generateDatabase()
        # test data
        if self.languagesDB.totalkeys() != 20:
            print("Database failure")
            exit()

    def run(self):
        scores = {
            language: self.calculateScore(language)
            for language in self.languagesDB.getall()
        }
        sorted_languages = sorted(scores, key=lambda lang: scores[lang], reverse=True)
        print(scores)
        return [
            self.parseLanguage(index + 1, sorted_languages[index])
            for index in range(5)
        ]

    def calculateScore(self, language):
        languageData = self.languagesDB.get(language)
        score = 0

        if (self.userData["projectType"] == 0 or
            self.userData["projectType"] in languageData["Project type"]):
            score += 1
        if (self.userData["modernity"] != None):
            score += self.userData["modernity"] * languageData["Modernity"] * 0.1
        if (self.userData["performance"] != None):
            score += self.userData["performance"] * languageData["Performance"] * 0.1
        if (self.userData["complexity"] is None or (len(languageData["Complexity"]) and
            self.userData["complexity"] == languageData["Complexity"])):
            score += 1
        else:
            for complexity in languageData["Complexity"]:
                if self.userData["complexity"] in [complexity + 1, complexity - 1]:
                    score += 0.5
                    break
        if self.userData["scalability"] != None:
            score += self.userData["scalability"] * languageData["Scalability"] * 0.1
        if self.userData["popularity"] != None:
            score += self.userData["popularity"] * languageData["Popularity"] * 0.1
        if self.userData["lenType"] is None or\
                self.userData["lenType"] == languageData["Language type"]:
            score += 5
        if (self.userData["experienced"] != None and self.userData["experienced"] and
                language in self.userData["experience"]):
            score += self.userData["experience"][language]/100

        return score

    def parseLanguage(self, index, language):
        langDict = self.languagesDB.get(language)
        match langDict['Language type']:
            case 0:
                langDict['Language type'] = "scripted"
            case 1:
                langDict['Language type'] = "complied"
            case 2:
                langDict['Language type'] = "interpreted"
        complexity = []
        for complex in langDict['Complexity']:
            match complex:
                case 0:
                    complexity.append("tiny")
                case 1:
                    complexity.append("small")
                case 2:
                    complexity.append("regular")
                case 3:
                    complexity.append("big")
        langDict['Complexity'] = complexity
        types = []
        for type in langDict['Project type']:
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

        langDict['Project type'] = types

        return (f"{index}. {language} |\n\tTOP#{langDict['PopularityTop']} in January 2024, type: "
                f"{langDict['Language type']}, modernity: {langDict['Modernity']}/10, "
                f"performance: {langDict['Performance']}/10, scalability:"
                f"{langDict['Scalability']}/10,\n\tRecommended for {langDict['Complexity']}"
                f"{langDict['Project type']} projects")
