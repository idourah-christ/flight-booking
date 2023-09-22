import requests
import xml.etree.ElementTree as ET

def download_currency_rate(url):
    try:
        response = requests.get(url)

        # Check if the request was successful (status code 200).
        if response.status_code == 200:
            # Replace 'output.xml' with the desired file name for saving the XML file.
            with open('currency.xml', 'wb') as file:
                file.write(response.content)
            print("XML file downloaded successfully.")
        else:
            print(f"Failed to download XML file. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def get_currency(currecy_file_path):
    currency_list = []
    tree = ET.parse(currecy_file_path)
    root = tree.getroot()
    for cube in root.findall('Cube'):
        for rate in cube.findall('Cube'):
            currency = rate.get("currency")
            rate_value = rate.get("rate")
            currency_object = {"currency":currency,"value":rate_value}
            currency_list.append(currency_object)
    return currency_list
