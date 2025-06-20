import subprocess

# Boilerplate function - include this in every test below!
def prepare_variables(input_array, output_array):
    # Prepare Variables
    input_string = '\n'.join(input_array)
    input_data = input_string.encode('utf-8')
    expected_output = '\n'.join(output_array)

    # Get Actual Output from Input Data
    output_data = subprocess.run(['python', 'main.py'], input=input_data, stdout=subprocess.PIPE)
    output_bytes = output_data.stdout.strip()
    output_string = output_bytes.decode("utf-8")

    # Windows outputs CR, remove it
    actual_output = output_string.replace('\r\n', '\n')

    # Test if Expected Output is found in Actual Output
    return expected_output, actual_output

# Test 1
def test_one_six():
    # Inputs
    input_array = [
        '1',
        '6'
    ]

    # Outputs
    output_array = [
        '7'
    ]

    # Test if Input results in Output
    expected_output, actual_output = prepare_variables(input_array, output_array)
    assert expected_output in actual_output

# Test 2
def test_eleven_fifteen():
    # Inputs
    input_array = [
        '11',
        '15'
    ]

    # Outputs
    output_array = [
        '26'
    ]

    # Test if Input results in Output
    expected_output, actual_output = prepare_variables(input_array, output_array)
    assert expected_output in actual_output
