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


class ExpressServiceCodeFull(object):
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
        'id': 'int',
        'express_service_code': 'str',
        'expire_date': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'express_service_code': 'express_service_code',
        'expire_date': 'expire_date'
    }

    def __init__(self, id=None, express_service_code=None, expire_date=None):
        """
        ExpressServiceCodeFull - a model defined in Swagger
        """

        self._id = None
        self._express_service_code = None
        self._expire_date = None

        if id is not None:
          self.id = id
        if express_service_code is not None:
          self.express_service_code = express_service_code
        if expire_date is not None:
          self.expire_date = expire_date

    @property
    def id(self):
        """
        Gets the id of this ExpressServiceCodeFull.
        ID

        :return: The id of this ExpressServiceCodeFull.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExpressServiceCodeFull.
        ID

        :param id: The id of this ExpressServiceCodeFull.
        :type: int
        """

        self._id = id

    @property
    def express_service_code(self):
        """
        Gets the express_service_code of this ExpressServiceCodeFull.
        An 8-digit number in string format

        :return: The express_service_code of this ExpressServiceCodeFull.
        :rtype: str
        """
        return self._express_service_code

    @express_service_code.setter
    def express_service_code(self, express_service_code):
        """
        Sets the express_service_code of this ExpressServiceCodeFull.
        An 8-digit number in string format

        :param express_service_code: The express_service_code of this ExpressServiceCodeFull.
        :type: str
        """

        self._express_service_code = express_service_code

    @property
    def expire_date(self):
        """
        Gets the expire_date of this ExpressServiceCodeFull.
        UNIX time stamp representing the UTC time that the Express Service Code expires. Please note that every time this service is executed, the expire_date is set to now + 24 hours.

        :return: The expire_date of this ExpressServiceCodeFull.
        :rtype: list[int]
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        """
        Sets the expire_date of this ExpressServiceCodeFull.
        UNIX time stamp representing the UTC time that the Express Service Code expires. Please note that every time this service is executed, the expire_date is set to now + 24 hours.

        :param expire_date: The expire_date of this ExpressServiceCodeFull.
        :type: list[int]
        """

        self._expire_date = expire_date

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
        if not isinstance(other, ExpressServiceCodeFull):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
