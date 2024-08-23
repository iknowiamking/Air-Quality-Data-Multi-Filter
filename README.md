
---

# Air Quality Data Multi Filter
## Video Demo:  <https://youtu.be/gAd8qIqV2Us>
## Description
### Overview

This script provides functionality to query and filter air quality data from an **API by the Indian Gov**. The user can filter records based on city names and pollutants, and retrieve a specific number of records from the API.
- This Project takes the raw air pollution data through api by the indian gov which contains all the information about air index in multiple loacations across the country.
- This project aim mainly to return the city , station(where the air index is checked) , pollutant , and the avg of the pollutant although many can be included by minor change in the script.
- This code can return all the records or filtered by city or filtered by pollutant or combination of both and the signature feature: it can take multiple filtering as well in one go.
- The code is run only through command line.

---
### Features

1. **Filter by City**: Retrieve air quality data for specified city/cities.
2. **Filter by Pollutant**: Retrieve air quality data for specified pollutant(s).
3. **Filter by Both City and Pollutant**: Retrieve data that matches both city/cities and pollutant(s) criteria.
4. **Display All Data**: Retrieve and display a specified number of records.
---
### Usage

To run the script, use command-line arguments to specify the filtering criteria and data limits.

#### Command-Line Arguments

- `-l, --limit`: Number of records to fetch from the API. Default is 10,000.
- `-s, --search`: List of cities to filter by.
- `-p, --pollutant`: List of pollutants to filter by.

#### Example Commands

- Retrieve all records (default limit of 10,000):
  ```bash
  python script.py
  ```

- Retrieve records for specific cities:
  ```bash
  python script.py -s city1 city2
  ```

- Retrieve records for specific pollutants:
  ```bash
  python script.py -p pollutant1 pollutant2
  ```

- Retrieve records for specific cities and pollutants:
  ```bash
  python script.py -s city1 -p pollutant1
  ```

- Retrieve records for specific number of cities and pollutants:
  ```bash
  python script.py -s city1 city2 -p pollutant1 pollutant2
  ```

- Retrieve a specific number of records with filters:
  ```bash
  python script.py -l 5000 -s city1 -p pollutant1
  ```
---
### Code Documentation

#### `main()`

The main function of the script that orchestrates the workflow:
- Parses command-line arguments.
- Makes API requests and retrieves data.
- Applies filters based on user input.
- Displays the results.

#### `connection(limit)`

Handles API requests to fetch air quality data:
- **Parameters**:
  - `limit`: Number of records to fetch.
- **Returns**: JSON object containing the data from the API.
- **Exits**: If `limit` is less than 1, it exits with an error message.

#### `input_parser(args)`

Parses command-line arguments using `argparse`:
- **Parameters**:
  - `args`: List of command-line arguments.
- **Returns**: Tuple of `(limit, search, pollutant)`.

#### `filter_by_city(json_obj, search_string)`

Filters records by city names:
- **Parameters**:
  - `json_obj`: JSON object containing the records.
  - `search_string`: List of city names to filter by.
- **Returns**: Count of records matching the criteria.

#### `filter_by_pollutant(json_obj, search_string)`

Filters records by pollutants:
- **Parameters**:
  - `json_obj`: JSON object containing the records.
  - `search_string`: List of pollutants to filter by.
- **Returns**: Count of records matching the criteria.

#### `filter_by_city_and_pollutant(json_obj, search_string, pollutant)`

Filters records by both city names and pollutants:
- **Parameters**:
  - `json_obj`: JSON object containing the records.
  - `search_string`: List of city names to filter by.
  - `pollutant`: List of pollutants to filter by.
- **Returns**: Count of records matching the criteria.
---
### Error Handling

- If no command-line arguments are provided, the script exits with a message to use `-h` for help.
- If the `limit` parameter is less than 1, the script exits with an error message.
---
### Dependencies

- `requests`: Library to handle HTTP requests.

Make sure to install the required dependencies using:
```bash
pip install requests
```

---
---

# Testing File Documentation

## Overview

> [!CAUTION]
> The test may fail if the original data has changed , so these tests are time centric and manual test is needed.

This testing file contains unit tests for functions from the `project` module. It uses the `pytest` framework to ensure the correctness of the functions:

- `connection()`
- `input_parser()`
- `filter_by_city()`
- `filter_by_pollutant()`
- `filter_by_city_and_pollutant()`

## Test Cases

### `test_connection()`

Tests the `connection()` function, which fetches air quality data from an API.

- **Objective**: Verify that the function handles valid and invalid limits correctly.
- **Cases Tested**:
  - **Valid Limit**: A limit greater than 0 (not tested directly in this function).
  - **Invalid Limits**: Limits of 0 and -1 should raise a `SystemExit` exception.

### `test_input_parser()`

Tests the `input_parser()` function, which parses command-line arguments.

- **Objective**: Ensure that the function correctly handles valid and invalid command-line arguments.
- **Cases Tested**:
  - **No Arguments**: Should raise a `SystemExit` exception when no arguments are provided.
  - **Incomplete Arguments**: Should raise a `SystemExit` exception when required arguments are missing.

### `test_filter_by_city()`

Tests the `filter_by_city()` function, which filters records by city names.

- **Objective**: Validate that the function correctly filters records based on city names.
- **Cases Tested**:
  - **Non-Existent City**: Should return 0 records for cities that do not exist in the dataset.
  - **Existing Cities**:
    - For "raipur": The expected count is 27 (to be verified with actual data).
    - For "chennai": The expected count is 52 (to be verified with actual data).
    - For both "chennai" and "raipur": The combined count is 79 (to be verified with actual data).

### `test_filter_by_pollutant()`

Tests the `filter_by_pollutant()` function, which filters records by pollutants.

- **Objective**: Ensure the function correctly filters records based on pollutant types.
- **Cases Tested**:
  - **Non-Existent Pollutant**: Should return 0 records for pollutants not present in the dataset.
  - **Existing Pollutants**:
    - For "nh3": The expected count is 430 (to be verified with actual data).
    - For "ozone": The expected count is 463 (to be verified with actual data).
    - For both "ozone" and "nh3": The combined count is 893 (to be verified with actual data).

### `filter_by_city_and_pollutant()`

Tests the `filter_by_city_and_pollutant()` function, which filters records based on both city names and pollutants.

- **Objective**: Validate that the function correctly filters records that match both criteria.
- **Cases Tested**:
  - **Non-Existent City and Pollutant**: Should return 0 records if neither the city nor the pollutant exists.
  - **Existing Cities and Pollutants**:
    - For cities "chennai" and "raipur" with pollutants "ozone" and "nh3": The expected count is 22 (to be verified with actual data).

## Usage

1. **Installation**: Ensure `pytest` is installed. You can install it using:
   ```bash
   pip install pytest
   ```

2. **Running Tests**: Save the file as `test_project.py` and run:
   ```bash
   pytest test_project.py
   ```

3. **Verification**: Check the output to ensure all tests pass. Adjust expected values based on your actual dataset if needed.

## Dependencies

- **pytest**: Testing framework used for writing and running tests.

---

