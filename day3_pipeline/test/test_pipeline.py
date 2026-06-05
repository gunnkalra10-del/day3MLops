from data_loader import load_data
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_load_data():
    data = load_data()
    assert data is not None
    assert hasattr(data, "data")
    assert hasattr(data, "target")
    assert len(data.data) > 0
    assert len(data.target) > 0
