import httpretty

from paystackapi.tests.base_test_case import BaseTestCase
from paystackapi.page import Page


class TestPage(BaseTestCase):

    @httpretty.activate
    def test_page_create(self):
        """Method defined to test page creation."""
        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("/page"),
            content_type='text/json',
            body='{"status": true, "message": "Page created"}',
            status=201,
        )

        response = Page.create(
            name="New test product One"
        )
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_page_list(self):
        """Function defined to test page list method."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/page/perPage=3&page=1"),
            content_type='text/json',
            body='{"status": true, "message": "Pages retrieved"}',
            status=201,
        )

        response = Page.list(perPage=3, page=1)
        self.assertEqual(response['status'], True)
    
    @httpretty.activate
    def test_page_fetch(self):
        """Function defined to test page fetch method."""
        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("/page/5nApBwZkvY"),
            content_type='text/json',
            body='{"status": true, "message": "Page retrieved"}',
            status=201,
        )

        response = Page.fetch(id_or_slug="5nApBwZkvY")
        self.assertEqual(response['status'], True)

    @httpretty.activate
    def test_page_update(self):
        """Function defined to test page update method."""
        httpretty.register_uri(
            httpretty.PUT,
            self.endpoint_url("/page/5nApBwZkvY"),
            content_type='text/json',
            body='{"status": true, "message": "page updated"}',
            status=201,
        )

        response = Page.update(id_or_slug="5nApBwZkvY", name="new page name")
        self.assertEqual(response['status'], True)
