from facts import Facts, Fact


def test_facts_get_types():
    facts = Facts([
        Fact('first', [], ['a', 'b']),
        Fact('first', [], ['a', 'c']),
        Fact('first', [], ['a']),
    ])
    assert facts.get_types() == {'a', 'b', 'c'}


def test_facts_get_tags():
    facts = Facts([
        Fact('first', ['a', 'b'], []),
        Fact('first', ['a', 'c'], []),
        Fact('first', ['a'], []),
    ])
    assert facts.get_tags() == {'a', 'b', 'c'}


def test_facts_is_empty():
    facts = Facts([])
    assert facts.is_empty()