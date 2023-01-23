import os
import sys

from lxml import etree
from unittest import TestCase

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from ..arxml_parser import ArxmlHandler


class TestArxmlHandler(TestCase):
    """Test for Arxml Handler class"""

    FAKER_ARXML = "tests/fakers/EcuExtract.arxml"

    list_of_exps = ["//*[local-name() = 'APPLICATION-SW-COMPONENT-TYPE']/*[local-name() = 'SHORT-NAME']/text()",
                    "//*[local-name() = 'IMPLEMENTATION-DATA-TYPE']/*[local-name() = 'SHORT-NAME']/text()",
                    "count(//*[local-name() = 'APPLICATION-SW-COMPONENT-TYPE'])"]

    def test_return_instance(self):
        """ Test to validate the returned instance"""

        get_data = ArxmlHandler(self.FAKER_ARXML, self.list_of_exps)
        data = get_data.extract_data()
        self.assertIsInstance(data, list)

    def test_no_xml_file(self):
        """Test to validate xml syntax"""

        faker_no_xml = "tests/fakers/NoXMLSyntax.xml"
        self.assertRaises(etree.XMLSyntaxError, ArxmlHandler, faker_no_xml, self.list_of_exps)

    def test_file_does_not_exist(self):
        """Test to validate file does not exist"""

        self.assertRaises(FileNotFoundError, ArxmlHandler, "ThisFileDoesNotExist.xml", self.list_of_exps)

    def test_boolean_inputs(self):
        """Test to validate boolean inputs"""

        self.assertRaises(TypeError, ArxmlHandler, True, self.list_of_exps)
        self.assertRaises(TypeError, ArxmlHandler, self.FAKER_ARXML, False)

    def test_integer_inputs(self):
        """Test to validate integer inputs"""

        self.assertRaises(TypeError, ArxmlHandler, 42, self.list_of_exps)
        self.assertRaises(TypeError, ArxmlHandler, self.FAKER_ARXML, 42)

    def test_float_inputs(self):
        """Test to validate float inputs"""

        self.assertRaises(TypeError, ArxmlHandler, 42.0, self.list_of_exps)
        self.assertRaises(TypeError, ArxmlHandler, self.FAKER_ARXML, 42.0)

    def test_dict_inputs(self):
        """Test to validate dict as inputs"""

        dict_for_test = {"Don't Panic": 42}

        self.assertRaises(TypeError, ArxmlHandler, dict_for_test, self.list_of_exps)
        self.assertRaises(TypeError, ArxmlHandler, self.FAKER_ARXML, dict_for_test)

    def test_list_input_as_file(self):
        """Test to validate list input as file"""

        list_for_test = [self.FAKER_ARXML]
        self.assertRaises(TypeError, ArxmlHandler, list_for_test, self.list_of_exps)

    def test_none_as_exp_input(self):
        """Test to validate NoneType as expressions input"""

        self.assertRaises(TypeError, ArxmlHandler, self.FAKER_ARXML, None)
