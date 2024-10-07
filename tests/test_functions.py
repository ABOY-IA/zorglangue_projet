import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from components.functions import zorglangue

def test_zorglangue():
    assert zorglangue("Bonjour") == "ruojnoB"
    assert zorglangue("Vive Zorglub !") == "eviV bulgroZ !"
    assert zorglangue("Ceci est un message secret.") == "iceC tse nu egassem terces."