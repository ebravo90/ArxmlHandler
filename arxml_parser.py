"""
This module provides the `ArxmlHandler` class, which can be used to extract data from an ARXML file using
XPath expressions.
The class takes in a file name and a list of XPath expressions during initialization, and provides a method to extract
data from the file using those expressions.
"""
# pylint: disable=c-extension-no-member, too-few-public-methods

import os
import logging

from lxml import etree


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class ArxmlHandler:
    """
    The ArxmlHandler class provides functionality to extract data from an ARXML file using XPath expressions.
    It takes in a file name and a list of XPath expressions during initialization and provides a method to extract
    data from the file using those expressions.
    """

    def __init__(self, file_name: str, xpath_expressions: list):

        if type(file_name) not in [str]:
            raise TypeError("File input should be a string")

        if not os.path.exists(file_name):
            raise FileNotFoundError("The file does not exist")

        if type(xpath_expressions) not in [list]:
            raise TypeError("Expressions should be given in a list")

        self.file_name = file_name
        self.xpath_expressions = xpath_expressions

    def extract_data(self) -> list:
        """
        Extract data from the arxml file using the provided xpath expressions.


        :return: A list of lists, containing the data extracted from the arxml file for each xpath expression.
        :rtype: list
        """

        extracted_data = []
        tree = self._parse_file()
        if not tree:
            return None

        for expression in self.xpath_expressions:
            xpath_data = tree.xpath(expression)
            if xpath_data:
                extracted_data.append(xpath_data)
        if extracted_data:
            return extracted_data
        return None

    def _parse_file(self) -> etree._ElementTree:
        """
        Parse the arxml file and return the etree._ElementTree object.

        :return: An ElementTree object representing the parsed arxml file.
        :rtype: etree._ElementTree
        """
        try:
            with open(self.file_name, "r", encoding="utf-8") as file_to_parse:
                arxml_tree = etree.parse(file_to_parse)
                print(type(arxml_tree))
                return arxml_tree
        except etree.XMLSyntaxError as exception:
            logging.error("Unable to parse file: %s", exception)
            return None



if __name__ == "__main__":

    # NoXMLSyntax.xml
    get_data = ArxmlHandler("tests/fakers/NoXMLSyntax.xml",
                            ["uyhjh"])
    data = get_data.extract_data()
    logging.info(data)
