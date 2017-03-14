# coding: utf-8

"""
    Phone.com API

    This is a Phone.com api Swagger definition

    OpenAPI spec version: 1.0.0
    Contact: apisupport@phone.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Member(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, extension=None, phone_number=None):
        """
        Member - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'extension': 'ExtensionSummary',
            'phone_number': 'str'
        }

        self.attribute_map = {
            'extension': 'extension',
            'phone_number': 'phone_number'
        }

        self._extension = extension
        self._phone_number = phone_number

    @property
    def extension(self):
        """
        Gets the extension of this Member.
        Extension that this member refers to. Output is an Extension Summary Object. Input must be an Extension Lookup Object.

        :return: The extension of this Member.
        :rtype: ExtensionSummary
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """
        Sets the extension of this Member.
        Extension that this member refers to. Output is an Extension Summary Object. Input must be an Extension Lookup Object.

        :param extension: The extension of this Member.
        :type: ExtensionSummary
        """

        self._extension = extension

    @property
    def phone_number(self):
        """
        Gets the phone_number of this Member.
        Phone number

        :return: The phone_number of this Member.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this Member.
        Phone number

        :param phone_number: The phone_number of this Member.
        :type: str
        """

        self._phone_number = phone_number

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Member):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other