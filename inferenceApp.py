# The `LanguageInferenceSystem` class is a language recommendation system that calculates scores for
# different programming languages based on user input and returns the top 5 recommended languages.
from tools.dbService import generateDatabase
from pickledb import PickleDB

"""
LanguageInferenceSystem class.

This class represents a language inference system that recommends programming languages based on user input.

Attributes:
    languagesDB (PickleDB): The database of programming languages.
    userData (dict): User input data.

Methods:
    __init__(): Initializes the LanguageInferenceSystem object.
    run(): Runs the language inference system and returns the top 5 recommended languages.
    calculateScore(language): Calculates the score for a given language based on user input.
    parseLanguage(index, language): Parses the language data and returns a formatted string.

"""
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

    """
    run method.

    Runs the language inference system and returns the top 5 recommended languages.

    Args:
        self: The LanguageInferenceSystem object.

    Returns:
        list: The top 5 recommended languages.
    """
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

    """
    calculateScore method.

    Calculates the score for a given language based on user input.

    Args:
        self: The LanguageInferenceSystem object.
        language: The language for which the score is calculated.

    Returns:
        float: The calculated score for the language.

    """
    def calculateScore(self, language):
        languageData = self.languagesDB.get(language)
        score = 0

        if (self.userData["projectType"] == 0 or
            self.userData["projectType"] in languageData["Project type"]):
            score += 1
        if self.userData["modernity"] is not None:
            score += self.userData["modernity"] * languageData["Modernity"] * 0.1
        if self.userData["performance"] is not None:
            score += self.userData["performance"] * languageData["Performance"] * 0.1
        if (self.userData["complexity"] is None or (len(languageData["Complexity"]) and
            self.userData["complexity"] == languageData["Complexity"])):
            score += 1
        else:
            for complexity in languageData["Complexity"]:
                if self.userData["complexity"] in [complexity + 1, complexity - 1]:
                    score += 0.5
                    break
        if self.userData["scalability"] is not None:
            score += self.userData["scalability"] * languageData["Scalability"] * 0.1
        if self.userData["popularity"] is not None:
            score += self.userData["popularity"] * languageData["Popularity"] * 0.1
        if self.userData["lenType"] is None or\
                self.userData["lenType"] == languageData["Language type"]:
            score += 5
        if (self.userData["experienced"] is not None and self.userData["experienced"] and
                language in self.userData["experience"]):
            score += self.userData["experience"][language]/100

        return score

    """
    parseLanguage method.

    Parses the language data and returns a formatted string.

    Args:
        self: The LanguageInferenceSystem object.
        index: The index of the language.
        language: The language to parse.

    Returns:
        str: The formatted string representing the language information.

    """
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
