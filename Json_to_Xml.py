

# importing json and Xml element tree

import json
import xml.etree.ElementTree as ET

# defining function with root and json object

def json_to_xml(json_obj, root=None):
    if root is None:
        root = ET.Element("object")
    
    # based on the type of Object we are parsing the json and converting it into following Xml formate
    
    if isinstance(json_obj, dict):
        
        for key, value in json_obj.items():
            
            if isinstance(value, dict):     # for Key value based data
                obj = ET.SubElement(root, "object")
                json_to_xml(value, obj)
                
            elif isinstance(value, list):   # for list type data usually known as array
                array = ET.SubElement(root, "array")
                json_to_xml(value, array)
                
            elif isinstance(value, bool):   # for boolean data
                bool_node = ET.SubElement(root, "boolean", name=key)
                bool_node.text = str(value).lower()
                
            elif value is None:             # for None values
                null_node = ET.SubElement(root, "null", name=key)
                
            else:                           # for numberic as well as string type of data
                if isinstance(value, int) or isinstance(value, float):
                    num_node = ET.SubElement(root, "number", name=key)
                    num_node.text = str(value)
                else:
                    str_node = ET.SubElement(root, "string", name=key)
                    str_node.text = value
                    
    elif isinstance(json_obj, list):
        for item in json_obj:
            json_to_xml(item, root)
            
    else:
        if isinstance(json_obj, int) or isinstance(json_obj, float):
            num_node = ET.SubElement(root, "number")
            num_node.text = str(json_obj)
        elif isinstance(json_obj, bool):
            bool_node = ET.SubElement(root, "boolean")
            bool_node.text = str(json_obj).lower()
        elif json_obj is None:
            null_node = ET.SubElement(root, "null")
        else:
            str_node = ET.SubElement(root, "string")
            str_node.text = json_obj

    return root

def convert_json_to_xml(json_file, xml_file):
    with open(json_file, 'r') as f:
        json_obj = json.load(f)

    root = json_to_xml(json_obj)
    tree = ET.ElementTree(root)
    tree.write(xml_file)
    
print()
json_file = input("Give the ( Json File Path ) :: ")
output_file = 'Output_Xml_file.xml'

# pass the file names to function

convert_json_to_xml(json_file, output_file)

print("XMl file Created Successfully !! ")
print(f"Check the   '{output_file}'   in the Same folder of Json file located")
