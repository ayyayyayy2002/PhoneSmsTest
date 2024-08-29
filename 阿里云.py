import requests
import os
import sys

# 获取传入的参数
phone = sys.argv[1]
print(f"接收到的参数 phone: {phone}")

cookies = {
    'cna': 'l91WHzz+HFQCAdoEKBrrszsf',
    'yunpk': '1306222260163933',
    'sca': '0d94489b',
    'partitioned_cookie_flag': 'addPartitioned',
    'login_aliyunid_csrf': '_csrf_tk_1463124903320850',
    '_samesite_flag_': 'true',
    'atpsida': '42b7a7af384defd81f9343e8_1724903322_2',
    'XSRF-TOKEN': '008c9e79-5e62-4a56-9430-b4deb5a37453',
    'cookie2': '162cbe1d331ff677eba4a9edb643dddf',
    't': 'a910219e8b4a276e22037f029fd1f776',
    '_tb_token_': '73b7e3e7e33b3',
    'isg': 'BFpa9UUU6JpvjmQ2e9s3nXpoqwB8i95lZ8rmRWTTUu241_kRQBoOdWXhp6PLB1b9',
    'tfstk': 'f9ZjYVMqPIAbWUWRCCBrPBN-kdi_f5seMdMTKRK2BmnYBcwTIflq7fzSf7VX3EyaBfN_abVNnA705cN8arlx7tA1fReLuAox7hO_gRxauVy9CAFrDV4q_jlsfRVCU6SFY-2mjDCFTMylxw2xYAd9XC8R2HhpBFIFY-2v3xBUeMWgt-9ZTfntkVnJ2bDwkchtBTG-CvY9M5FTeTMZQAKtHqHJexDnXfFtXTw-MZdSQZMThTU8sTKD1G2SNhKBKvgYQMcyXKZ-h8GLHPx9XuMjllWHbrzouPen-oyhf3m4dzn-L-jXVDexdSlz9MKS28y8_24lsHo4Nbu3DD9OD8ijG2EjrKKu98wT84ZPpMmjDjUZmRJCg8Zbg-q7QdL-cmzSRoidxIhazJZsClfGVWw3q7M89G1A4t-EOv6k5LgHXYGFFTTMSbvVcS-1D_1-kYDAYT6WNF0xEYOcFTTZIqHoh-B5Feo1.',
}

headers = {
    'accept': 'application/json, text/javascript',
    'accept-language': 'zh-CN,zh;q=0.9',
    'bx-v': '2.5.11',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'XSRF-TOKEN=6e634e4f-bc11-428c-a3c3-cdfeb74d4045; cna=l91WHzz+HFQCAdoEKBrrszsf; yunpk=1306222260163933; sca=0d94489b; partitioned_cookie_flag=addPartitioned; login_aliyunid_csrf=_csrf_tk_1463124903320850; _samesite_flag_=true; atpsida=42b7a7af384defd81f9343e8_1724903322_2; XSRF-TOKEN=008c9e79-5e62-4a56-9430-b4deb5a37453; cookie2=162cbe1d331ff677eba4a9edb643dddf; t=a910219e8b4a276e22037f029fd1f776; _tb_token_=73b7e3e7e33b3; isg=BFpa9UUU6JpvjmQ2e9s3nXpoqwB8i95lZ8rmRWTTUu241_kRQBoOdWXhp6PLB1b9; tfstk=f9ZjYVMqPIAbWUWRCCBrPBN-kdi_f5seMdMTKRK2BmnYBcwTIflq7fzSf7VX3EyaBfN_abVNnA705cN8arlx7tA1fReLuAox7hO_gRxauVy9CAFrDV4q_jlsfRVCU6SFY-2mjDCFTMylxw2xYAd9XC8R2HhpBFIFY-2v3xBUeMWgt-9ZTfntkVnJ2bDwkchtBTG-CvY9M5FTeTMZQAKtHqHJexDnXfFtXTw-MZdSQZMThTU8sTKD1G2SNhKBKvgYQMcyXKZ-h8GLHPx9XuMjllWHbrzouPen-oyhf3m4dzn-L-jXVDexdSlz9MKS28y8_24lsHo4Nbu3DD9OD8ijG2EjrKKu98wT84ZPpMmjDjUZmRJCg8Zbg-q7QdL-cmzSRoidxIhazJZsClfGVWw3q7M89G1A4t-EOv6k5LgHXYGFFTTMSbvVcS-1D_1-kYDAYT6WNF0xEYOcFTTZIqHoh-B5Feo1.',
    'origin': 'https://passport.aliyun.com',
    'priority': 'u=1, i',
    'referer': 'https://passport.aliyun.com/havanaone/register/register.htm?_lang=zh&_regfrom=ALIYUN&cssStyle=&_extra=_country=null&_extra=null&tg=https%3A%2F%2Faccount.aliyun.com%2Fregister%2Fregister_success_with_identify.htm%3Fft%3Dpc_sms%26isQr%3Dfalse%26fromSite%3D6%26params%3D%257B%2522site%2522%253A%25226%2522%252C%2522ru%2522%253A%2522https%253A%252F%252Fcn.aliyun.com%252F%2522%257D%26umidToken%3DY9e63e2dbc6bb81e8964bc63e51151a85%26regFlag%3D1%26accounttraceid%3D2b8f9b9c86fc4f93be1601084c2e1a0bdtfg%26log_channel%3Dindep%26log_platform%3Dpc%26log_entrance%3Dofficial%26bizEntrance%3Dmobile_reg%26register_method%3Dmobile_reg%26log_biz%3Daliyun&bizName=aliyun&bizEntrance=mobile_reg&bizPassParams=%7B%22tenantName%22%3A%22%22%7D&cssUrl=&pageversion=v2&rnd=0.525108007447026',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'contextToken': 'sm2_0gagaroqwhqtxnwhnmrjmz8baz9sng6k',
    '_bx-v': '2.5.11',
}

data = (f'country=CN&tg=https%3A%2F%2Faccount.aliyun.com%2Fregister%2Fregister_success_with_identify.htm%3Fft%3Dpc_sms%26isQr%3Dfalse%26fromSite%3D6%26params%3D%257B%2522site%2522%253A%25226%2522%252C%2522ru%2522%253A%2522https%253A%252F%252Fcn.aliyun.com%252F%2522%257D%26umidToken%3DY9e63e2dbc6bb81e8964bc63e51151a85%26regFlag%3D1%26accounttraceid%3D2b8f9b9c86fc4f93be1601084c2e1a0bdtfg%26log_channel%3Dindep%26log_platform%3Dpc%26log_entrance%3Dofficial%26bizEntrance%3Dmobile_reg%26register_method%3Dmobile_reg%26log_biz%3Daliyun&bizEntrance=mobile_reg&bizName=aliyun&isPc=true&lang=zh_CN&device=PC&bizPassParams=%7B%22tenantName%22%3A%22%22%7D&ncoSig=&ncoSessionid=&ncoToken=&mobile={phone}&mobileArea=&ua=&phoneCountry=&phoneArea=&phoneNumber=&mobileCode=&baxia%5Bvalue%5D=unshow&checkbox=false&bx-ua=228!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&bx-umidtoken=T2gA3SSRXOO04cnG7EVqvHcR87VIheS4Bmt3j-fmJ-Cql1gTYim8m5UCSVxilPx0uLw=')

response = requests.post(
    'https://passport.aliyun.com/havanaone/registerLegacy/sendSms.do',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
print(response.text)

script_name = os.path.basename(__file__)

# 生成要写入的内容
output = f"{script_name}: {response.text}\n"

# 将内容追加到 response.txt 文件中
with open('AAA.txt', 'a', encoding='utf-8') as file:
    file.write(output)

print("内容已写入 AAA.txt")