import requests

# Define the base URL for your API
base_url = 'http://localhost:8000/api/'  # Replace with your API's URL

# Function to send GET requests and print responses
def test_get_person_by_name(name):
    response = requests.get(base_url + f'persons/?name={name}')
    print(f'GET /persons/?name={name} Response:')
    print(response.json())

# Function to send POST requests and print responses
def test_create_person(data):
    response = requests.post(base_url + 'persons/', json=data)
    print('POST /persons/ Response:')
    print(response.json())

# Function to send PUT requests and print responses
def test_update_person(name, updated_data):
    response = requests.put(base_url + f'persons/{name}/', json=updated_data)
    print(f'PUT /persons/{name}/ Response:')
    print(response.json())

# Function to send DELETE requests and print responses
def test_delete_person(name):
    response = requests.delete(base_url + f'persons/{name}/')
    print(f'DELETE /persons/{name}/ Response:')
    print(response.status_code)  # Expecting 204 for successful delete

if __name__ == '__main__':
    # Test CREATE operation
    new_person_data = {
        'name': 'chisom',
        
        # Include other required fields here
    }
    test_create_person(new_person_data)

    # Test READ operation
    test_get_person_by_name('Chisom')

    # Test UPDATE operation
    updated_person_data = {
        'new_name': 'Updated Name',
        
        # Include other fields to update
    }
    test_update_person('Chisom', updated_person_data)

    # Test DELETE operation
    test_delete_person('Updated Name')
