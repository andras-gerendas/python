# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.17
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1beta1_self_subject_access_review_spec import V1beta1SelfSubjectAccessReviewSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1beta1SelfSubjectAccessReviewSpec(unittest.TestCase):
    """V1beta1SelfSubjectAccessReviewSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1SelfSubjectAccessReviewSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1beta1_self_subject_access_review_spec.V1beta1SelfSubjectAccessReviewSpec()  # noqa: E501
        if include_optional :
            return V1beta1SelfSubjectAccessReviewSpec(
                non_resource_attributes = kubernetes.client.models.v1beta1/non_resource_attributes.v1beta1.NonResourceAttributes(
                    path = '0', 
                    verb = '0', ), 
                resource_attributes = kubernetes.client.models.v1beta1/resource_attributes.v1beta1.ResourceAttributes(
                    group = '0', 
                    name = '0', 
                    namespace = '0', 
                    resource = '0', 
                    subresource = '0', 
                    verb = '0', 
                    version = '0', )
            )
        else :
            return V1beta1SelfSubjectAccessReviewSpec(
        )

    def testV1beta1SelfSubjectAccessReviewSpec(self):
        """Test V1beta1SelfSubjectAccessReviewSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
