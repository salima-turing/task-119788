import pytest
from aggregate_data import aggregate_data

@pytest.mark.parametrize("data, expected_mean", [
    ([1, 2, 3], 2.0),
    ([-1, 0, 1], 0.0),
    ([0.5, 1.5, 2.5], 1.5),
])
def test_aggregate_data_positive(data, expected_mean):
    """Test that the aggregate_data function returns the correct mean for positive test cases."""
    assert aggregate_data(data) == expected_mean

def test_aggregate_data_empty_list():
    """Test that the aggregate_data function raises a ValueError for an empty list."""
    with pytest.raises(ValueError, match="Cannot calculate mean of an empty list."):
        aggregate_data([])

@pytest.mark.parametrize("data", [
    ["a", "b", "c"],
    [1, "2", 3],
    [True, False, True],
])
def test_aggregate_data_non_numeric_values(data):
    """Test that the aggregate_data function raises a TypeError for non-numeric values."""
    with pytest.raises(TypeError, match="All values must be numeric."):
        aggregate_data(data)

def test_aggregate_data_performance():
    """Test the performance of the aggregate_data function."""
    data = list(range(100000))
    assert aggregate_data(data) == 49999.5

def test_aggregate_data_consistency():
    """Test the consistency of the aggregate_data function."""
    data = [1, 2, 3]
    for _ in range(10):
        assert aggregate_data(data) == 2.0

if __name__ == "__main__":
    pytest.main()
