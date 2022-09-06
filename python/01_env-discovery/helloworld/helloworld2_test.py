import helloworld2


def test_helloworld_true():
    assert helloworld2.helloworld("Bob") == "Hello World, Bob !"


def test_helloworld_false():
    assert helloworld2.helloworld("Bob") != "Hello World,Bob !"
