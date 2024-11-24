from django.test import TestCase, Client
from django.shortcuts import reverse
from django.http import JsonResponse
from typing import cast

import json

class DebugSessionClientTest(TestCase):

    def test_debug_session_client(self):
        client = Client()

        test_key = 'foo'
        test_val = 'bar'

        resp = client.get(reverse("debug_session_dump"))

        self.assertIsInstance(resp, JsonResponse)

        resp = cast(JsonResponse, resp)

        data = json.loads(resp.content)

        self.assertNotIn(test_key, data)

        resp = self.client.get(
            reverse(
                "debug_session_put", 
                kwargs={
                    'key': test_key, 
                    'val': test_val
                }
            ),
            follow = True
        )

        self.assertIsInstance(resp, JsonResponse)

        resp = cast(JsonResponse, resp)

        data = json.loads(resp.content)

        self.assertIn(test_key, data)
        self.assertEqual(data[test_key], test_val)

        resp = self.client.get(
            reverse(
                "debug_session_del", 
                kwargs={'key': test_key }
            ),
            follow = True
        )

        self.assertIsInstance(resp, JsonResponse)

        resp = cast(JsonResponse, resp)

        data = json.loads(resp.content)

        self.assertNotIn(test_key, data)
