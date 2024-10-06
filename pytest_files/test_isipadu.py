import pytest
from isipadu_tangki_air import *
#import isipadu_tangki_air

pi = 3.142

def test_dapat_jejari_tinggi(monkeypatch):
    # Simulate user input for jejari and tinggi
    inputs = iter(["3.5", "7.2"])  # Mock input values
    
    # Mock the input() function
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Run the function and check the output
    result = dapat_jejari_tinggi()
    assert result == (3.5, 7.2)

@pytest.mark.parametrize(
    "radius, height, expected_volume",  # Test parameter names
    [
        (3, 5, pi * 3**2 * 5),    
        (4, 6, pi * 4**2 * 6),               
    ]
)
def test_kira_isipadu(radius, height, expected_volume):
    assert kira_isipadu(radius, height) == expected_volume

# def test_kira_isipadu():
#     radius = 3
#     height = 5
#     expected_volume = pi * radius**2 * height
#     assert kira_isipadu(radius, height) == expected_volume 

def test_main(monkeypatch, capsys):
    # Define a function to simulate multiple user inputs
    user_inputs = ["3","4"]

    def mock_input(_):
        return user_inputs.pop(0)

    # Use the function to simulate user input
    monkeypatch.setattr('builtins.input', mock_input)

    main()

    # Capture the printed output
    captured = capsys.readouterr()
    assert captured.out.strip() == "Isipadu tangki air = 113.11"
