import helloworld3

expected_output= """Hello, Rifi !
How are you, Rifi ?
Hello, Fifi !
How are you, Fifi ?
Hello, Loulou !
How are you, Loulou ?
Goodbye, Rifi !
Goodbye, Fifi !
Goodbye, Loulou !
"""

def test_demo3(capfd):
    helloworld3.demo3()  # Writes to stdout
    out, err = capfd.readouterr()
    assert out == expected_output
