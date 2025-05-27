from task2.solution import count_by_letter


def mock_get_category_members(category, cmcontinue=None):
    members = [{'title': f'Dog{i}'} for i in range(10)]
    return members, 'Nah'


def test_latin_streak_stops(monkeypatch):
    monkeypatch.setattr(
        'task2.solution.get_category_members', mock_get_category_members
    )
    result = count_by_letter('Категория:Животные по алфавиту')
    assert result == {}
