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


class RuleSetForwardItem(object):
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
        'type': 'str',
        'extension': 'ExtensionSummary',
        'number': 'str',
        'screening': 'bool',
        'caller_id': 'str',
        'voice_tag': 'str',
        'distinctive_ring': 'str'
    }

    attribute_map = {
        'type': 'type',
        'extension': 'extension',
        'number': 'number',
        'screening': 'screening',
        'caller_id': 'caller_id',
        'voice_tag': 'voice_tag',
        'distinctive_ring': 'distinctive_ring'
    }

    def __init__(self, type=None, extension=None, number=None, screening=False, caller_id='calling_number', voice_tag=None, distinctive_ring=None):
        """
        RuleSetForwardItem - a model defined in Swagger
        """

        self._type = None
        self._extension = None
        self._number = None
        self._screening = None
        self._caller_id = None
        self._voice_tag = None
        self._distinctive_ring = None

        if type is not None:
          self.type = type
        if extension is not None:
          self.extension = extension
        if number is not None:
          self.number = number
        if screening is not None:
          self.screening = screening
        if caller_id is not None:
          self.caller_id = caller_id
        if voice_tag is not None:
          self.voice_tag = voice_tag
        if distinctive_ring is not None:
          self.distinctive_ring = distinctive_ring

    @property
    def type(self):
        """
        Gets the type of this RuleSetForwardItem.
        Required. Must equal phone_number or extension.

        :return: The type of this RuleSetForwardItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this RuleSetForwardItem.
        Required. Must equal phone_number or extension.

        :param type: The type of this RuleSetForwardItem.
        :type: str
        """
        if type is not None and not re.search('phone_number|extension', type):
            raise ValueError("Invalid value for `type`, must be a follow pattern or equal to `/phone_number|extension/`")

        self._type = type

    @property
    def extension(self):
        """
        Gets the extension of this RuleSetForwardItem.
        Required if type = \"extension\". Extension that callers should be directed to. Output is an Extension Summary Object. Input must be an Extension Lookup Object.

        :return: The extension of this RuleSetForwardItem.
        :rtype: ExtensionSummary
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """
        Sets the extension of this RuleSetForwardItem.
        Required if type = \"extension\". Extension that callers should be directed to. Output is an Extension Summary Object. Input must be an Extension Lookup Object.

        :param extension: The extension of this RuleSetForwardItem.
        :type: ExtensionSummary
        """

        self._extension = extension

    @property
    def number(self):
        """
        Gets the number of this RuleSetForwardItem.
        Required if type = \"phone_number\". Phone number that callers should be directed to. Must be a string in E.164 format.

        :return: The number of this RuleSetForwardItem.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this RuleSetForwardItem.
        Required if type = \"phone_number\". Phone number that callers should be directed to. Must be a string in E.164 format.

        :param number: The number of this RuleSetForwardItem.
        :type: str
        """

        self._number = number

    @property
    def screening(self):
        """
        Gets the screening of this RuleSetForwardItem.
        Boolean. Optional. Default is FALSE. Use this to activate call screening. If TRUE, the timeout on the parent action should be at least 30 seconds.

        :return: The screening of this RuleSetForwardItem.
        :rtype: bool
        """
        return self._screening

    @screening.setter
    def screening(self, screening):
        """
        Sets the screening of this RuleSetForwardItem.
        Boolean. Optional. Default is FALSE. Use this to activate call screening. If TRUE, the timeout on the parent action should be at least 30 seconds.

        :param screening: The screening of this RuleSetForwardItem.
        :type: bool
        """

        self._screening = screening

    @property
    def caller_id(self):
        """
        Gets the caller_id of this RuleSetForwardItem.
        Optional. Must equal calling_number or called_number. Defines which phone number should be used for Caller ID. Default is calling_number.

        :return: The caller_id of this RuleSetForwardItem.
        :rtype: str
        """
        return self._caller_id

    @caller_id.setter
    def caller_id(self, caller_id):
        """
        Sets the caller_id of this RuleSetForwardItem.
        Optional. Must equal calling_number or called_number. Defines which phone number should be used for Caller ID. Default is calling_number.

        :param caller_id: The caller_id of this RuleSetForwardItem.
        :type: str
        """
        if caller_id is not None and not re.search('calling_number|called_number', caller_id):
            raise ValueError("Invalid value for `caller_id`, must be a follow pattern or equal to `/calling_number|called_number/`")

        self._caller_id = caller_id

    @property
    def voice_tag(self):
        """
        Gets the voice_tag of this RuleSetForwardItem.
        Optional string. If screening = TRUE, this value will be passed into our Text-To-Speech engine and used to inform the caller of who they have reached.

        :return: The voice_tag of this RuleSetForwardItem.
        :rtype: str
        """
        return self._voice_tag

    @voice_tag.setter
    def voice_tag(self, voice_tag):
        """
        Sets the voice_tag of this RuleSetForwardItem.
        Optional string. If screening = TRUE, this value will be passed into our Text-To-Speech engine and used to inform the caller of who they have reached.

        :param voice_tag: The voice_tag of this RuleSetForwardItem.
        :type: str
        """

        self._voice_tag = voice_tag

    @property
    def distinctive_ring(self):
        """
        Gets the distinctive_ring of this RuleSetForwardItem.
        Optional. Must equal one of: DEFAULT, STYLE_2, STYLE_3, STYLE_4, STYLE_5, STYLE_6, STYLE_7, STYLE_8, or STYLE_9. Identifies the style of ring tone you will hear when an incoming call is waiting.

        :return: The distinctive_ring of this RuleSetForwardItem.
        :rtype: str
        """
        return self._distinctive_ring

    @distinctive_ring.setter
    def distinctive_ring(self, distinctive_ring):
        """
        Sets the distinctive_ring of this RuleSetForwardItem.
        Optional. Must equal one of: DEFAULT, STYLE_2, STYLE_3, STYLE_4, STYLE_5, STYLE_6, STYLE_7, STYLE_8, or STYLE_9. Identifies the style of ring tone you will hear when an incoming call is waiting.

        :param distinctive_ring: The distinctive_ring of this RuleSetForwardItem.
        :type: str
        """
        if distinctive_ring is not None and not re.search('DEFAULT|STYLE_2|STYLE_3|STYLE_4|STYLE_5|STYLE_6|STYLE_7|STYLE_8|STYLE_9', distinctive_ring):
            raise ValueError("Invalid value for `distinctive_ring`, must be a follow pattern or equal to `/DEFAULT|STYLE_2|STYLE_3|STYLE_4|STYLE_5|STYLE_6|STYLE_7|STYLE_8|STYLE_9/`")

        self._distinctive_ring = distinctive_ring

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
        if not isinstance(other, RuleSetForwardItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
