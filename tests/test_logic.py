from logic import get_topic_data


def test_get_topic_data_valid():
    result = get_topic_data("alpha")
    assert result is not None
    assert "explanation" in result


def test_get_topic_data_invalid():
    result = get_topic_data("unknown topic")
    assert result is None


def test_get_topic_data_empty():
    result = get_topic_data("")
    assert result is None