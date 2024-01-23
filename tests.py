import pytest
import os
from inferenceApp import LanguageInferenceSystem, DB_PATH

# Ensure the test database does not interfere with the real database
TEST_DB_PATH = './test_database.db'

@pytest.fixture
def setup_database(monkeypatch):
    # Arrange: Redirect DB_PATH to the test database path
    monkeypatch.setattr('inferenceApp.DB_PATH', TEST_DB_PATH)
    # Ensure any existing test database is removed
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)
    return LanguageInferenceSystem()

@pytest.mark.parametrize("test_id, project_type, modernity, performance, complexity, scalability, popularity, experienced, len_type, experience, expected_top_language", [
    # Happy path tests
    ("HP-1", 1, 5, 5, None, 5, 5, True, 2, {'Python': 100}, 'Python'),
    ("HP-2", 2, 8, 8, 2, 8, 8, False, None, {}, 'C'),
    ("HP-3", 3, 7, 7, 1, 7, 7, True, 1, {'C#': 50}, 'C#'),
    # Edge cases
    ("EC-1", 0, None, None, None, None, None, None, None, {}, 'Python'),  # All None or default values
    ("EC-2", 7, 10, 10, 3, 10, 10, True, 2, {'Javascript': 100}, 'Javascript'),  # Max values
    # Error cases
    ("ER-1", 9, 5, 5, 1, 5, 5, True, 1, {'InvalidLang': 100}, 'Python'),  # Invalid project type
    ("ER-2", 1, -1, 5, 1, 5, 5, True, 1, {'Python': 100}, 'Python'),  # Negative modernity
])
def test_calculate_score(setup_database, test_id, project_type, modernity, performance, complexity, scalability, popularity, experienced, len_type, experience, expected_top_language):
    system = setup_database
    # Arrange: Set user data
    system.userData.update({
        "projectType": project_type,
        "modernity": modernity,
        "performance": performance,
        "complexity": complexity,
        "scalability": scalability,
        "popularity": popularity,
        "experienced": experienced,
        "lenType": len_type,
        "experience": experience
    })

    # Act: Run the system to get the results
    results = system.run()

    # Assert: Check if the top language is as expected
    assert expected_top_language in results[0], f"Test ID {test_id}: Expected top language to be {expected_top_language}, but got {results[0]}"
