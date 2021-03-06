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


class RuleSet(object):
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
        'filter': 'RuleSetFilter',
        'actions': 'list[RuleSetAction]'
    }

    attribute_map = {
        'filter': 'filter',
        'actions': 'actions'
    }

    def __init__(self, filter=None, actions=None):
        """
        RuleSet - a model defined in Swagger
        """

        self._filter = None
        self._actions = None

        if filter is not None:
          self.filter = filter
        if actions is not None:
          self.actions = actions

    @property
    def filter(self):
        """
        Gets the filter of this RuleSet.

        :return: The filter of this RuleSet.
        :rtype: RuleSetFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """
        Sets the filter of this RuleSet.

        :param filter: The filter of this RuleSet.
        :type: RuleSetFilter
        """

        self._filter = filter

    @property
    def actions(self):
        """
        Gets the actions of this RuleSet.
        Array of Action Objects. Required. Routes have rule sets, and rule sets have one or more actions. The supported actions are described below:

        :return: The actions of this RuleSet.
        :rtype: list[RuleSetAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this RuleSet.
        Array of Action Objects. Required. Routes have rule sets, and rule sets have one or more actions. The supported actions are described below:

        :param actions: The actions of this RuleSet.
        :type: list[RuleSetAction]
        """

        self._actions = actions

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
        if not isinstance(other, RuleSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
