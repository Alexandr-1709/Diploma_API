import json
import logging
from pydantic import ValidationError
import allure
import curlify
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from requests import Session, Response


def validate_shema(shema, response_json):
    try:
        shema.parse_obj(response_json)
    except ValidationError as e:
        print(e.json())


class CustomSession(Session):
    def __init__(self, base_url):
        self.base_url = base_url
        super().__init__()

    def request(self, method, url, *args, **kwargs) -> Response:
        response = super(CustomSession, self).request(method=method,
                                                      url=self.base_url + url,
                                                      *args, **kwargs)
        curl = curlify.to_curl(response.request)
        status_code = response.status_code
        logging.info(f"Status Code: {status_code}\n{curl}")
        with step(f'{method} {url}'):
            allure.attach(body=f'status_code={status_code}\n{curl}',
                          name="Request curl",
                          attachment_type=AttachmentType.TEXT,
                          extension='txt')
            try:
                response_body = response.json()
            except json.JSONDecodeError:
                response_body = response.text

            allure.attach(body=json.dumps(response_body, indent=2),
                          name="Response body",
                          attachment_type=AttachmentType.JSON)

        return response


reqres_session = CustomSession('https://reqres.in')
