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
from swagger_client.api.enrollment_api import EnrollmentApi  # noqa: E501
from swagger_client.rest import ApiException


class TestEnrollmentApi(unittest.TestCase):
    """EnrollmentApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.enrollment_api.EnrollmentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_enrollment_add_client_to_enrollment(self):
        """Test case for enrollment_add_client_to_enrollment

        Book a client into an enrollment.  # noqa: E501
        """
        pass

    def test_enrollment_get_enrollments(self):
        """Test case for enrollment_get_enrollments

        Get enrollments scheduled at a site.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
