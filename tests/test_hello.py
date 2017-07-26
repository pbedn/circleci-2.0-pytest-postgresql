from app.my_app import hello


def test_hello():
    assert hello() == "Hello world"
