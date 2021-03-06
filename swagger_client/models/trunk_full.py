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


class TrunkFull(object):
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
        'name': 'str',
        'uri': 'str',
        'max_concurrent_calls': 'int',
        'max_minutes_per_month': 'int',
        'greeting': 'MediaSummary',
        'error_message': 'MediaSummary',
        'codecs': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'uri': 'uri',
        'max_concurrent_calls': 'max_concurrent_calls',
        'max_minutes_per_month': 'max_minutes_per_month',
        'greeting': 'greeting',
        'error_message': 'error_message',
        'codecs': 'codecs'
    }

    def __init__(self, id=None, name=None, uri=None, max_concurrent_calls=None, max_minutes_per_month=None, greeting=None, error_message=None, codecs=None):
        """
        TrunkFull - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._uri = None
        self._max_concurrent_calls = None
        self._max_minutes_per_month = None
        self._greeting = None
        self._error_message = None
        self._codecs = None

        self.id = id
        self.name = name
        self.uri = uri
        self.max_concurrent_calls = max_concurrent_calls
        self.max_minutes_per_month = max_minutes_per_month
        self.greeting = greeting
        self.error_message = error_message
        self.codecs = codecs

    @property
    def id(self):
        """
        Gets the id of this TrunkFull.
        Integer Trunk ID. Read-only.

        :return: The id of this TrunkFull.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TrunkFull.
        Integer Trunk ID. Read-only.

        :param id: The id of this TrunkFull.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this TrunkFull.
        Name. Required.

        :return: The name of this TrunkFull.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TrunkFull.
        Name. Required.

        :param name: The name of this TrunkFull.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def uri(self):
        """
        Gets the uri of this TrunkFull.
        Fully-qualified SIP URI. Required.

        :return: The uri of this TrunkFull.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this TrunkFull.
        Fully-qualified SIP URI. Required.

        :param uri: The uri of this TrunkFull.
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")

        self._uri = uri

    @property
    def max_concurrent_calls(self):
        """
        Gets the max_concurrent_calls of this TrunkFull.
        Max concurrent calls. Default is 10.

        :return: The max_concurrent_calls of this TrunkFull.
        :rtype: int
        """
        return self._max_concurrent_calls

    @max_concurrent_calls.setter
    def max_concurrent_calls(self, max_concurrent_calls):
        """
        Sets the max_concurrent_calls of this TrunkFull.
        Max concurrent calls. Default is 10.

        :param max_concurrent_calls: The max_concurrent_calls of this TrunkFull.
        :type: int
        """
        if max_concurrent_calls is None:
            raise ValueError("Invalid value for `max_concurrent_calls`, must not be `None`")

        self._max_concurrent_calls = max_concurrent_calls

    @property
    def max_minutes_per_month(self):
        """
        Gets the max_minutes_per_month of this TrunkFull.
        Max minutes per month. Default is 750.

        :return: The max_minutes_per_month of this TrunkFull.
        :rtype: int
        """
        return self._max_minutes_per_month

    @max_minutes_per_month.setter
    def max_minutes_per_month(self, max_minutes_per_month):
        """
        Sets the max_minutes_per_month of this TrunkFull.
        Max minutes per month. Default is 750.

        :param max_minutes_per_month: The max_minutes_per_month of this TrunkFull.
        :type: int
        """
        if max_minutes_per_month is None:
            raise ValueError("Invalid value for `max_minutes_per_month`, must not be `None`")

        self._max_minutes_per_month = max_minutes_per_month

    @property
    def greeting(self):
        """
        Gets the greeting of this TrunkFull.
        Greeting. Output is a Media Summary Object. Input must be a Media Lookup Object. Must refer to a media recording that has is_hold_music set to FALSE.

        :return: The greeting of this TrunkFull.
        :rtype: MediaSummary
        """
        return self._greeting

    @greeting.setter
    def greeting(self, greeting):
        """
        Sets the greeting of this TrunkFull.
        Greeting. Output is a Media Summary Object. Input must be a Media Lookup Object. Must refer to a media recording that has is_hold_music set to FALSE.

        :param greeting: The greeting of this TrunkFull.
        :type: MediaSummary
        """
        if greeting is None:
            raise ValueError("Invalid value for `greeting`, must not be `None`")

        self._greeting = greeting

    @property
    def error_message(self):
        """
        Gets the error_message of this TrunkFull.
        Error Message. Output is a Media Summary Object. Input must be a Media Lookup Object. Must refer to a media recording that has is_hold_music set to FALSE.

        :return: The error_message of this TrunkFull.
        :rtype: MediaSummary
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this TrunkFull.
        Error Message. Output is a Media Summary Object. Input must be a Media Lookup Object. Must refer to a media recording that has is_hold_music set to FALSE.

        :param error_message: The error_message of this TrunkFull.
        :type: MediaSummary
        """
        if error_message is None:
            raise ValueError("Invalid value for `error_message`, must not be `None`")

        self._error_message = error_message

    @property
    def codecs(self):
        """
        Gets the codecs of this TrunkFull.
        Custom audio codec configuration, if any is needed. If provided, must be a simple array containing the prioritized list of desired codecs. Supported codecs are: g711u 64k, g711u 56k, g711a 64k, g711a 56k, g7231, g728, g729, g729A, g729B, g729AB, gms full, rfc2833, t38, ilbc, h263, g722, g722_1, g729D, g729E, amr, amr_wb, efr, evrc, h264, mpeg4, red, cng, SIP Info to 2833

        :return: The codecs of this TrunkFull.
        :rtype: list[str]
        """
        return self._codecs

    @codecs.setter
    def codecs(self, codecs):
        """
        Sets the codecs of this TrunkFull.
        Custom audio codec configuration, if any is needed. If provided, must be a simple array containing the prioritized list of desired codecs. Supported codecs are: g711u 64k, g711u 56k, g711a 64k, g711a 56k, g7231, g728, g729, g729A, g729B, g729AB, gms full, rfc2833, t38, ilbc, h263, g722, g722_1, g729D, g729E, amr, amr_wb, efr, evrc, h264, mpeg4, red, cng, SIP Info to 2833

        :param codecs: The codecs of this TrunkFull.
        :type: list[str]
        """
        if codecs is None:
            raise ValueError("Invalid value for `codecs`, must not be `None`")

        self._codecs = codecs

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
        if not isinstance(other, TrunkFull):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
