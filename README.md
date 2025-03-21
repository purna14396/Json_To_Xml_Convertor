# JSON to XML Converter

## Overview
This project provides a Python script that converts JSON data into XML format. The script reads a JSON file, processes the data, and generates an equivalent XML file with structured elements.

## Features
- Converts JSON objects, arrays, strings, numbers, booleans, and null values into XML format.
- Handles nested JSON structures.
- Supports different data types such as dictionaries, lists, integers, floats, strings, booleans, and null values.

## Requirements
- Python 3.x

## Installation
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-name>
   ```
2. Ensure Python is installed on your system.

## Usage
1. Run the script:
   ```sh
   python json_to_xml.py
   ```
2. Enter the path of the JSON file when prompted.
3. The script will generate an XML file named `Output_Xml_file.xml` in the same folder as the input JSON file.

## Code Explanation
The script follows these steps:
1. Reads the JSON file.
2. Recursively processes the JSON data and converts it into an XML structure.
3. Writes the XML data to an output file.

### Example
#### Input JSON File (`data.json`):
```json
{
    "name": "John",
    "age": 30,
    "is_student": false,
    "courses": ["Math", "Science"],
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}
```
#### Output XML File (`Output_Xml_file.xml`):
```xml
<object>
    <string name="name">John</string>
    <number name="age">30</number>
    <boolean name="is_student">false</boolean>
    <array>
        <string>Math</string>
        <string>Science</string>
    </array>
    <object>
        <string name="city">New York</string>
        <string name="zip">10001</string>
    </object>
</object>
```

## License
This project is open-source and available under the MIT License.

## Contributions
Contributions are welcome! Feel free to submit a pull request or report issues.

## Contact
For any queries, feel free to reach out via GitHub issues.
