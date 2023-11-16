import base64
import json

import pytest

from src import main


class TestIntegrationBook:
    @pytest.fixture
    def basic_auth(self):
        username = 'hamza'
        password = 'bouzid'
        token = base64.b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
        return f'Basic {token}'

    def test_it_should_make_a_request_to_api_gateway(self, basic_auth):
        event = self.generic_http_gateway()
        event['path'] = '/api/v1/book/get_all'
        event['httpMethod'] = 'GET'
        event['headers'] = {
            'Authorization': basic_auth
        }

        response = main.lambda_handler(event, '')

        body_ = json.loads(response['body'])

        print(body_)

        assert response['statusCode'] == 200
        assert body_['result'] is True
        assert len(body_['data']) > 0

    @staticmethod
    def generic_http_gateway():
        return {
            "resource": "/{proxy+}",
            "path": "/",
            "httpMethod": "POST",
            "body": "{}",
            "headers": {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "cache-control": "no-cache",
                "CloudFront-Forwarded-Proto": "https",
                "CloudFront-Is-Desktop-Viewer": "true",
                "CloudFront-Is-Mobile-Viewer": "false",
                "CloudFront-Is-SmartTV-Viewer": "false",
                "CloudFront-Is-Tablet-Viewer": "false",
                "CloudFront-Viewer-Country": "US",
                "Content-Type": "application/json",
                "headerName": "headerValue",
                "Host": "gy415nuibc.execute-api.us-east-1.amazonaws.com",
                "Postman-Token": "9f583ef0-ed83-4a38-aef3-eb9ce3f7a57f",
                "User-Agent": "PostmanRuntime/2.4.5",
                "Via": "1.1 d9842f7680bd.cloudfront.net (CloudFront)",
                "X-Amz-Cf-Id": "pn-PWItl0gdeJky8tqsg8iS_sgsKD1A==",
                "X-Forwarded-For": "54.240.196.186, 54.182.214.83",
                "X-Forwarded-Port": "443",
                "X-Forwarded-Proto": "https"
            },
            "multiValueHeaders": {
                "Accept": [
                    "*/*"
                ],
                "Accept-Encoding": [
                    "gzip, deflate"
                ],
                "cache-control": [
                    "no-cache"
                ],
                "CloudFront-Forwarded-Proto": [
                    "https"
                ],
                "CloudFront-Is-Desktop-Viewer": [
                    "true"
                ],
                "CloudFront-Is-Mobile-Viewer": [
                    "false"
                ],
                "CloudFront-Is-SmartTV-Viewer": [
                    "false"
                ],
                "CloudFront-Is-Tablet-Viewer": [
                    "false"
                ],
                "CloudFront-Viewer-Country": [
                    "US"
                ],
                "Content-Type": [
                    "application/json"
                ],
                "headerName": [
                    "headerValue"
                ],
                "Host": [
                    "gy415nuibc.execute-api.us-east-1.amazonaws.com"
                ],
                "Postman-Token": [
                    "9f583ef0-ed83-4a38-aef3-eb9ce3f7a57f"
                ],
                "User-Agent": [
                    "PostmanRuntime/2.4.5"
                ],
                "Via": [
                    "1.1 d9842f7680bd.cloudfront.net (CloudFront)"
                ],
                "X-Amz-Cf-Id": [
                    "pn-PWItl0gdeJky8tqsg8iS_sgsKD1A=="
                ],
                "X-Forwarded-For": [
                    "54.240.196.186, 54.182.214.83"
                ],
                "X-Forwarded-Port": [
                    "443"
                ],
                "X-Forwarded-Proto": [
                    "https"
                ]
            },
            "queryStringParameters": {
                "name": "me",
                "multivalueName": "me"
            },
            "multiValueQueryStringParameters": {
                "name": [
                    "me"
                ],
                "multivalueName": [
                    "you",
                    "me"
                ]
            },
            "pathParameters": {
                "proxy": "hello/world"
            },
            "stageVariables": {
                "app_name": "B23MicroLayer",
                "version": "1.0.0",
                "docs_url": "/docs",
                "redoc_url": "/redoc",
                "cors_allow_origins": "*",
                "cors_allow_methods": "*",
                "cors_allow_headers": "*"
            },
            "requestContext": {
                "accountId": "12345678912",
                "resourceId": "roq9wj",
                "stage": "default",
                "requestId": "deef4878-7910-11e6-8f14-25afc3e9ae33",
                "identity": {
                    "cognitoIdentityPoolId": None,
                    "accountId": None,
                    "cognitoIdentityId": None,
                    "caller": None,
                    "apiKey": None,
                    "sourceIp": "192.168.196.186",
                    "cognitoAuthenticationType": None,
                    "cognitoAuthenticationProvider": None,
                    "userArn": None,
                    "userAgent": "PostmanRuntime/2.4.5",
                    "user": None
                },
                "resourcePath": "/{proxy+}",
                "httpMethod": "POST",
                "apiId": "gy415nuibc"
            },
            "isBase64Encoded": False
        }
