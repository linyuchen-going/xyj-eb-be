# -*- coding: UTF8 -*-

import json
import base64
import hashlib
import datetime
import requests

account_id = '019d299b204a486bcf92188afc9960ad'
token = 'ca05f902a3a6ae71939272fe66c0cf41'
app_id = 'f71bdb25113a45929b863dd8824d956d'
soft_version = '2014-06-30'


class UcpaasTool(object):

    def __get_header(self, now):
        authorization = base64.b64encode(bytes(account_id + ':' + now, encoding="utf8"))
        headers = {
            'Content-Type': 'application/json;charset=utf-8', 'Accept': 'application/json',
            'Authorization': authorization
        }

        return headers

    @staticmethod
    def md5_str(s):
        s = s.encode("utf8")
        m = hashlib.md5()
        m.update(s)
        return m.hexdigest()

    def send_sms(self, to_mobile, template_id, param=""):
        """

        :param template_id: str
        :param to_mobile: str
        :param param: str, 如果有多个参数，用逗号(,)隔开
        :return: (bool, res_code)
        """
        # 根据规则生成的校验值
        now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        sig_parameter = self.md5_str(account_id + token + now).upper()
        # 发送短信的url
        req_url = 'https://api.ucpaas.com/' + soft_version + '/Accounts/' + account_id + '/Messages/templateSMS?sig=' + sig_parameter
        # 根据规则生成的校验值
        # 发送的内容
        body = {
            'templateSMS': {
                'appId': app_id, 'templateId': template_id, 'to': to_mobile,
                'param': param
            }
        }
        r = requests.post(req_url, data=json.dumps(body), headers=self.__get_header(now), timeout=15)
        response = r.json()
        response_code = response['resp']['respCode']
        if response_code == '000000':
            return True, 0
        else:
            # print response
            # self.create_error_record(response)
            return False, response


if __name__ == "__main__":
    test = UcpaasTool()
    # print test.send_sms("13088108191", "29789")
