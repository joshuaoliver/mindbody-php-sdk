# coding: utf-8

"""
    MINDBODY Public API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.site_api import SiteApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSiteApi(unittest.TestCase):
    """SiteApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.site_api.SiteApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_site_get_activation_code(self):
        """Test case for site_get_activation_code

        Get an activation code for a site.  # noqa: E501
        """
        pass

    def test_site_get_locations(self):
        """Test case for site_get_locations

        Get locations for a site.  # noqa: E501
        """
        pass

    def test_site_get_programs(self):
        """Test case for site_get_programs

        Get service categories offered at a site.  # noqa: E501
        """
        pass

    def test_site_get_resources(self):
        """Test case for site_get_resources

        Get resources used at a site.  # noqa: E501
        """
        pass

    def test_site_get_session_types(self):
        """Test case for site_get_session_types

        Get the session types used at a site.  # noqa: E501
        """
        pass

    def test_site_get_sites(self):
        """Test case for site_get_sites

        Get all sites that can be accessed by an API Key.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
