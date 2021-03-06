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


class SortIdNamePhoneNumber(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'phone_number': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'phone_number': 'phone_number'
    }

    def __init__(self, id=None, name=None, phone_number=None):
        """
        SortIdNamePhoneNumber - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._phone_number = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if phone_number is not None:
          self.phone_number = phone_number

    @property
    def id(self):
        """
        Gets the id of this SortIdNamePhoneNumber.

        :return: The id of this SortIdNamePhoneNumber.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SortIdNamePhoneNumber.

        :param id: The id of this SortIdNamePhoneNumber.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this SortIdNamePhoneNumber.

        :return: The name of this SortIdNamePhoneNumber.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SortIdNamePhoneNumber.

        :param name: The name of this SortIdNamePhoneNumber.
        :type: str
        """

        self._name = name

    @property
    def phone_number(self):
        """
        Gets the phone_number of this SortIdNamePhoneNumber.

        :return: The phone_number of this SortIdNamePhoneNumber.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this SortIdNamePhoneNumber.

        :param phone_number: The phone_number of this SortIdNamePhoneNumber.
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
        if not isinstance(other, SortIdNamePhoneNumber):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
