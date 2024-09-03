import pytest
import luas_isipadu_tangki_air

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
