# coding: utf-8

"""
    Phone.com API

    This is a Phone.com api Swagger definition

    OpenAPI spec version: 1.0.0
    Contact: apisupport@phone.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.expressservicecodes_api import ExpressservicecodesApi


class TestExpressservicecodesApi(unittest.TestCase):
    """ ExpressservicecodesApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.expressservicecodes_api.ExpressservicecodesApi()

    def tearDown(self):
        pass

    def test_get_account_express_srv_code(self):
        """
        Test case for get_account_express_srv_code

        Show details of an account Express Service Code
        """
        pass

    def test_list_account_express_srv_codes(self):
        """
        Test case for list_account_express_srv_codes

        Get the Express Service Code associated with your account in list format.
        """
        pass


if __name__ == '__main__':
    unittest.main()
