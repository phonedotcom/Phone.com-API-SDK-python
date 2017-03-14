# coding: utf-8

"""
    Phone.com API

    This is a Phone.com api Swagger definition

    OpenAPI spec version: 1.0.0
    Contact: apisupport@phone.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class MediaApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_account_media(self, account_id, **kwargs):
        """
        Add a media object to your account that can be used as a greeting or hold music. Users may create a media by using the built-in Text-to-speech (TTS) facility or upload a file of their choice. (Note: The maximum size for media files or JSON objects included with a POST or PUT request is 10 MB)
        See Account Media for more info on the properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_account_media(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param CreateMediaParams data: Media data
        :return: MediaFull
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_account_media_with_http_info(account_id, **kwargs)
        else:
            (data) = self.create_account_media_with_http_info(account_id, **kwargs)
            return data

    def create_account_media_with_http_info(self, account_id, **kwargs):
        """
        Add a media object to your account that can be used as a greeting or hold music. Users may create a media by using the built-in Text-to-speech (TTS) facility or upload a file of their choice. (Note: The maximum size for media files or JSON objects included with a POST or PUT request is 10 MB)
        See Account Media for more info on the properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_account_media_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param CreateMediaParams data: Media data
        :return: MediaFull
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'data']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_account_media" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `create_account_media`")


        collection_formats = {}

        resource_path = '/accounts/{account_id}/media'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apiKey']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='MediaFull',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_account_media(self, account_id, recording_id, **kwargs):
        """
        Show details of an individual media recording (Greeting or Hold Music)
        Get individual media recording
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account_media(account_id, recording_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param int recording_id: Recording ID (required)
        :return: MediaFull
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_account_media_with_http_info(account_id, recording_id, **kwargs)
        else:
            (data) = self.get_account_media_with_http_info(account_id, recording_id, **kwargs)
            return data

    def get_account_media_with_http_info(self, account_id, recording_id, **kwargs):
        """
        Show details of an individual media recording (Greeting or Hold Music)
        Get individual media recording
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account_media_with_http_info(account_id, recording_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param int recording_id: Recording ID (required)
        :return: MediaFull
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'recording_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account_media" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_account_media`")
        # verify the required parameter 'recording_id' is set
        if ('recording_id' not in params) or (params['recording_id'] is None):
            raise ValueError("Missing the required parameter `recording_id` when calling `get_account_media`")


        collection_formats = {}

        resource_path = '/accounts/{account_id}/media/{recording_id}'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']
        if 'recording_id' in params:
            path_params['recording_id'] = params['recording_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apiKey']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='MediaFull',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_account_media(self, account_id, **kwargs):
        """
        Get a list of media recordings for an account
        See Account Menus for more info on the properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_account_media(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param list[str] filters_id: ID filter
        :param list[str] filters_name: Name filter
        :param str sort_id: ID sorting
        :param str sort_name: Name sorting
        :param int limit: Max results
        :param int offset: Results to skip
        :param str fields: Field set
        :return: ListMedia
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_account_media_with_http_info(account_id, **kwargs)
        else:
            (data) = self.list_account_media_with_http_info(account_id, **kwargs)
            return data

    def list_account_media_with_http_info(self, account_id, **kwargs):
        """
        Get a list of media recordings for an account
        See Account Menus for more info on the properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_account_media_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param list[str] filters_id: ID filter
        :param list[str] filters_name: Name filter
        :param str sort_id: ID sorting
        :param str sort_name: Name sorting
        :param int limit: Max results
        :param int offset: Results to skip
        :param str fields: Field set
        :return: ListMedia
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'filters_id', 'filters_name', 'sort_id', 'sort_name', 'limit', 'offset', 'fields']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_account_media" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `list_account_media`")

        if 'sort_id' in params and not re.search('asc|desc', params['sort_id']):
            raise ValueError("Invalid value for parameter `sort_id` when calling `list_account_media`, must conform to the pattern `/asc|desc/`")
        if 'sort_name' in params and not re.search('asc|desc', params['sort_name']):
            raise ValueError("Invalid value for parameter `sort_name` when calling `list_account_media`, must conform to the pattern `/asc|desc/`")

        collection_formats = {}

        resource_path = '/accounts/{account_id}/media'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']

        query_params = {}
        if 'filters_id' in params:
            query_params['filters[id]'] = params['filters_id']
            collection_formats['filters[id]'] = 'multi'
        if 'filters_name' in params:
            query_params['filters[name]'] = params['filters_name']
            collection_formats['filters[name]'] = 'multi'
        if 'sort_id' in params:
            query_params['sort[id]'] = params['sort_id']
        if 'sort_name' in params:
            query_params['sort[name]'] = params['sort_name']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apiKey']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ListMedia',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)