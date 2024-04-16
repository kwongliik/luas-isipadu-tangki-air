import pytest
import luas_isipadu_tangki_air
# import sys

# def test_myoutput(capsys):  # or use "capfd" for fd-level
#     print("hello")
#     sys.stderr.write("world\n")
#     captured = capsys.readouterr()
#     assert captured.out == "hello\n"
#     assert captured.err == "world\n"
#     print("next")
#     captured = capsys.readouterr()
#     assert captured.out == "next\n"

def test_luas(monkeypatch, capsys):
    # Define a function to simulate multiple user inputs
    user_inputs = ["3","4"]

    def mock_input(_):
        return user_inputs.pop(0)

    # Use the function to simulate user input
    monkeypatch.setattr('builtins.input', mock_input)

    # Call the main function, which uses input() and prints the result
    luas_isipadu_tangki_air.luas()

    # Capture the printed output
    captured = capsys.readouterr()
    assert captured.out.strip() == "Luas tangki air = 131.96"

def test_isipadu(monkeypatch, capsys):
    # Define a function to simulate multiple user inputs
    user_inputs = ["3","4"]

    def mock_input(_):
        return user_inputs.pop(0)

    # Use the function to simulate user input
    monkeypatch.setattr('builtins.input', mock_input)

    luas_isipadu_tangki_air.isipadu()

    # Capture the printed output
    captured = capsys.readouterr()
    assert captured.out.strip() == "Isipadu tangki air = 113.11"
