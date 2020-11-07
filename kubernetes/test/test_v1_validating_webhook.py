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
from kubernetes.client.models.v1_validating_webhook import V1ValidatingWebhook  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1ValidatingWebhook(unittest.TestCase):
    """V1ValidatingWebhook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1ValidatingWebhook
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_validating_webhook.V1ValidatingWebhook()  # noqa: E501
        if include_optional :
            return V1ValidatingWebhook(
                admission_review_versions = [
                    '0'
                    ], 
                kubernetes.client_config = kubernetes.client.models.admissionregistration/v1/webhook_client_config.admissionregistration.v1.WebhookClientConfig(
                    ca_bundle = 'YQ==', 
                    service = kubernetes.client.models.admissionregistration/v1/service_reference.admissionregistration.v1.ServiceReference(
                        name = '0', 
                        namespace = '0', 
                        path = '0', 
                        port = 56, ), 
                    url = '0', ), 
                failure_policy = '0', 
                match_policy = '0', 
                name = '0', 
                namespace_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                    match_expressions = [
                        kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                            key = '0', 
                            operator = '0', 
                            values = [
                                '0'
                                ], )
                        ], 
                    match_labels = {
                        'key' : '0'
                        }, ), 
                object_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                    match_expressions = [
                        kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                            key = '0', 
                            operator = '0', 
                            values = [
                                '0'
                                ], )
                        ], 
                    match_labels = {
                        'key' : '0'
                        }, ), 
                rules = [
                    kubernetes.client.models.v1/rule_with_operations.v1.RuleWithOperations(
                        api_groups = [
                            '0'
                            ], 
                        api_versions = [
                            '0'
                            ], 
                        operations = [
                            '0'
                            ], 
                        resources = [
                            '0'
                            ], 
                        scope = '0', )
                    ], 
                side_effects = '0', 
                timeout_seconds = 56
            )
        else :
            return V1ValidatingWebhook(
                admission_review_versions = [
                    '0'
                    ],
                kubernetes.client_config = kubernetes.client.models.admissionregistration/v1/webhook_client_config.admissionregistration.v1.WebhookClientConfig(
                    ca_bundle = 'YQ==', 
                    service = kubernetes.client.models.admissionregistration/v1/service_reference.admissionregistration.v1.ServiceReference(
                        name = '0', 
                        namespace = '0', 
                        path = '0', 
                        port = 56, ), 
                    url = '0', ),
                name = '0',
                side_effects = '0',
        )

    def testV1ValidatingWebhook(self):
        """Test V1ValidatingWebhook"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
