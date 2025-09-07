import pytest
from app.app import summarize

@pytest.fixture
def sample():
    return ["1", "2", "3"]

def test_ok(sample):
    result = summarize(sample)
    assert result["count"] == 3.0
    assert result["sum"] == 6.0
    assert result["avg"] == 2.0

def test_empty():
    # Un solo número
    result = summarize(["5"])
    assert result["count"] == 1
    assert result["sum"] == 5.0
    assert result["avg"] == 5.0

    # Números decimales
    result = summarize(["1.5", "2.5", "2.0"])
    assert result["count"] == 3.0
    assert result["sum"] == 6.0
    assert result["avg"] == 2.0

    # Números negativos
    result = summarize(["-3", "-2", "-1"])
    assert result["count"] == 3.0
    assert result["sum"] == -6.0
    assert result["avg"] == -2.0

def test_non_numeric():
    # Lista vacía
    with pytest.raises(ValueError, match="no puede estar vacía"):
        summarize([])
    
    # Elementos no numéricos
    with pytest.raises(ValueError, match="no numérico"):
        summarize(["a", "2"])
    
    with pytest.raises(ValueError, match="no numérico"):
        summarize(["1", "abc", "3"])
    
    # Mezcla de válidos e inválidos
    with pytest.raises(ValueError, match="no numérico"):
        summarize(["1", "2", "xyz"])