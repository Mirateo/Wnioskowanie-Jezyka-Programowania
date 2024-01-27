"""
======================= START OF LICENSE NOTICE =======================
  Copyright (C) 2024 Mateusz Murawski. All Rights Reserved
======================== END OF LICENSE NOTICE ========================
"""
import pytest
from InferenceSystem import LanguageInferenceSystem

@pytest.fixture
def system():
    return LanguageInferenceSystem()


def test_calculateScore(system):
    # Arrange
    system.userData = {
        "projectType": 1,
        "modernity": 0.6,
        "performance": 0.6,
        "complexity": 2,
        "scalability": 0.6,
        "popularity": 1,
        "experienced": True,
        "lenType": 1,
        "experience": {"Python": 80}
    }
    language = "Python"

    # Act
    score = system.calculateScore(language)

    # Assert
    assert isinstance(score, float)
    assert score >= 0 and score <= 12

def test_calculateScore_max(system):
    # Arrange
    system.userData = {
        "projectType": 1,
        "modernity": 1,
        "performance": 1,
        "complexity": 1,
        "scalability": 1,
        "popularity": 1,
        "experienced": True,
        "lenType": 1,
        "experience": {"TEST": 100}
    }
    system.languagesDB.set(
        "TEST",
        {
            "Language type": 1, "Modernity": 10, "Performance":10, "Complexity": [1],
            "Scalability": 10,"Popularity": 10.0, "PopularityTop": 1, "Project type": [1],
        }
    )
    language = "TEST"
    # Act
    score = system.calculateScore(language)
    # Assert
    assert isinstance(score, float)
    assert score == 13
    # Teardown
    system.languagesDB.drem("TEST")

    assert system.languagesDB.totalkeys() == 20

def test_calculateScore_min(system):
    # Arrange
    system.userData = {
        "projectType": 1,
        "modernity": 1,
        "performance": 1,
        "complexity": 1,
        "scalability": 1,
        "popularity": 1,
        "experienced": True,
        "lenType": 1,
        "experience": {"TEST": 0}
    }
    system.languagesDB.set(
        "TEST",
        {
            "Language type": 3, "Modernity": 0, "Performance":0, "Complexity": [4],
            "Scalability": 0,"Popularity": 0, "PopularityTop": 21, "Project type": [2],
        }
    )
    language = "TEST"
    # Act
    score = system.calculateScore(language)
    # Assert
    assert isinstance(score, float)
    assert score == 0
    # Teardown
    system.languagesDB.drem("TEST")
    assert system.languagesDB.totalkeys() == 20

def test_parseLanguage_sunny(system):
    # Arrange
    index = 1
    language = "Python"

    # Act
    result = system.parseLanguage(index, language)
    # Assert
    assert isinstance(result, str)
    assert result.startswith(f"{index}. {language}\n"
        "\tTOP#1 in January 2024, type: interpreted, modernity: 9/10, performance: 8/10, scalability:7/10,\n"
        "\tRecommended for ['tiny', 'small', 'regular']['data science', 'database', 'desktop', 'game', 'mobile', 'script', 'web', 'embeded/IoT'] projects")

def test_parseLanguage_rainy(system):
    # Arrange
    index = 1
    language = "Polish"

    # Act and Assert
    with pytest.raises(TypeError) as e:
        result = system.parseLanguage(index, language)
    assert str(e.value) == "'bool' object is not subscriptable"

def test_run(system):
    # Arrange
    system.userData = {
        "projectType": None,
        "modernity": 1,
        "performance": None,
        "complexity": None,
        "scalability": None,
        "popularity": None,
        "experienced": False,
        "lenType": None,
        "experience": {}
    }
    # Act
    results = system.run()
    # Assert
    assert isinstance(results[0], str)
    assert results[0].startswith("1. Python")
    # Arrange
    system.userData = {
        "projectType": None,
        "modernity": None,
        "performance": 1,
        "complexity": None,
        "scalability": None,
        "popularity": None,
        "experienced": False,
        "lenType": None,
        "experience": {}
    }
    # Act
    results = system.run()
    # Assert
    assert isinstance(results[0], str)
    assert results[0].startswith("1. C")
    # Arrange
    system.userData = {
        "projectType": None,
        "modernity": None,
        "performance": None,
        "complexity": None,
        "scalability": 1,
        "popularity": None,
        "experienced": False,
        "lenType": None,
        "experience": {}
    }
    # Act
    results = system.run()
    # Assert
    assert isinstance(results[0], str)
    assert results[0].startswith("1. GO")
    # Arrange
    system.userData = {
        "projectType": None,
        "modernity": None,
        "performance": None,
        "complexity": None,
        "scalability": None,
        "popularity": True,
        "experienced": False,
        "lenType": None,
        "experience": {}
    }
    # Act
    results = system.run()
    # Assert
    assert isinstance(results[0], str)
    assert results[0].startswith("1. Python")
    # Arrange
    system.userData = {
        "projectType": None,
        "modernity": None,
        "performance": None,
        "complexity": None,
        "scalability": None,
        "popularity": None,
        "experienced": True,
        "lenType": None,
        "experience": {}
    }
    # Act
    results = system.run()
    # Assert
    assert isinstance(results[0], str)
    assert results[0].startswith("1. Python")
