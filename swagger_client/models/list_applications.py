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


class ListApplications(object):
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
        'filters': 'FilterIdNameArray',
        'sort': 'SortIdName',
        'total': 'int',
        'offset': 'int',
        'limit': 'int',
        'items': 'list[ApplicationFull]'
    }

    attribute_map = {
        'filters': 'filters',
        'sort': 'sort',
        'total': 'total',
        'offset': 'offset',
        'limit': 'limit',
        'items': 'items'
    }

    def __init__(self, filters=None, sort=None, total=None, offset=None, limit=None, items=None):
        """
        ListApplications - a model defined in Swagger
        """

        self._filters = None
        self._sort = None
        self._total = None
        self._offset = None
        self._limit = None
        self._items = None

        if filters is not None:
          self.filters = filters
        if sort is not None:
          self.sort = sort
        if total is not None:
          self.total = total
        if offset is not None:
          self.offset = offset
        if limit is not None:
          self.limit = limit
        if items is not None:
          self.items = items

    @property
    def filters(self):
        """
        Gets the filters of this ListApplications.

        :return: The filters of this ListApplications.
        :rtype: FilterIdNameArray
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """
        Sets the filters of this ListApplications.

        :param filters: The filters of this ListApplications.
        :type: FilterIdNameArray
        """

        self._filters = filters

    @property
    def sort(self):
        """
        Gets the sort of this ListApplications.

        :return: The sort of this ListApplications.
        :rtype: SortIdName
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """
        Sets the sort of this ListApplications.

        :param sort: The sort of this ListApplications.
        :type: SortIdName
        """

        self._sort = sort

    @property
    def total(self):
        """
        Gets the total of this ListApplications.

        :return: The total of this ListApplications.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this ListApplications.

        :param total: The total of this ListApplications.
        :type: int
        """

        self._total = total

    @property
    def offset(self):
        """
        Gets the offset of this ListApplications.

        :return: The offset of this ListApplications.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this ListApplications.

        :param offset: The offset of this ListApplications.
        :type: int
        """

        self._offset = offset

    @property
    def limit(self):
        """
        Gets the limit of this ListApplications.

        :return: The limit of this ListApplications.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this ListApplications.

        :param limit: The limit of this ListApplications.
        :type: int
        """

        self._limit = limit

    @property
    def items(self):
        """
        Gets the items of this ListApplications.

        :return: The items of this ListApplications.
        :rtype: list[ApplicationFull]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this ListApplications.

        :param items: The items of this ListApplications.
        :type: list[ApplicationFull]
        """

        self._items = items

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
        if not isinstance(other, ListApplications):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
