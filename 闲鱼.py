import os

import requests
import sys
# 获取传入的参数
phone = sys.argv[1]
print(f"接收到的参数 phone: {phone}")
cookies = {
    'cookie2': '1429fc5358d61a3f58deb9a409208899',
    't': 'c01f380fd57fced7f94b303c649d3177',
    '_tb_token_': '75b3eee703b45',
    'cna': 'jvlWH8nV+z4CAdoEKBogedre',
    'XSRF-TOKEN': '0721f4e7-e576-4ce5-91b2-783e00e2c354',
    '_samesite_flag_': 'true',
    'xlly_s': '1',
    'arms_uid': 'd46a342f-bd1d-480d-98ff-56254f3aee74',
    '_uab_collina': '172491047899615959752745',
    '_bl_uid': 'hUmga0hdebgv3s5mCv3ztn500gqp',
    'tfstk': 'fI7ipoYVlG-_5oUeYX8_Dk-F0hrp1fTXCt3vHEp4YpJBH599BsWci_-VBFLtmrfVQn79W1BhoOBd6R6vWx4cKpBxk1QcAqf5GNF6k5T11ET4e8U8e116l6b6aobMLHRcTIJquFbUsyL4e8ULLpqFoESvFO2kK6JBiIR2_tReYpOr3EJw0voeap823tJNTyRD_IoN3EP38pOqgqiweZSP8RzuSMKFlAbeshvmkLuczw3JxLzkd4uyICxGX1Jnuq7hAVvIwdrS9KT9C6dGhzg67nj5MIXgSVWcNw6HTTzmyd5CwgK17zif6FpM8NSogq5HSd-RuhHgKL71TaTevzPlTw6O1wfxgrRdep517E4zNFYwQeACkJgwnMSVWhTjQ8K1gMXHsUSyADoz070XTSQncmtwOBv8WwT7did3HzP3t0CXbBOWeWVnDwtwOBb4tWm7ihRB_P5..',
    'isg': 'BMvLHx70KUJCAHWWJnaMliCZWm-1YN_ibrEX2j3JIophXO--zDEtMrk6Nlyy_Dfa',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'bx-v': '2.5.11',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'cookie2=1429fc5358d61a3f58deb9a409208899; t=c01f380fd57fced7f94b303c649d3177; _tb_token_=75b3eee703b45; cna=jvlWH8nV+z4CAdoEKBogedre; XSRF-TOKEN=0721f4e7-e576-4ce5-91b2-783e00e2c354; _samesite_flag_=true; xlly_s=1; arms_uid=d46a342f-bd1d-480d-98ff-56254f3aee74; _uab_collina=172491047899615959752745; _bl_uid=hUmga0hdebgv3s5mCv3ztn500gqp; tfstk=fI7ipoYVlG-_5oUeYX8_Dk-F0hrp1fTXCt3vHEp4YpJBH599BsWci_-VBFLtmrfVQn79W1BhoOBd6R6vWx4cKpBxk1QcAqf5GNF6k5T11ET4e8U8e116l6b6aobMLHRcTIJquFbUsyL4e8ULLpqFoESvFO2kK6JBiIR2_tReYpOr3EJw0voeap823tJNTyRD_IoN3EP38pOqgqiweZSP8RzuSMKFlAbeshvmkLuczw3JxLzkd4uyICxGX1Jnuq7hAVvIwdrS9KT9C6dGhzg67nj5MIXgSVWcNw6HTTzmyd5CwgK17zif6FpM8NSogq5HSd-RuhHgKL71TaTevzPlTw6O1wfxgrRdep517E4zNFYwQeACkJgwnMSVWhTjQ8K1gMXHsUSyADoz070XTSQncmtwOBv8WwT7did3HzP3t0CXbBOWeWVnDwtwOBb4tWm7ihRB_P5..; isg=BMvLHx70KUJCAHWWJnaMliCZWm-1YN_ibrEX2j3JIophXO--zDEtMrk6Nlyy_Dfa',
    'eagleeye-pappname': 'gf3el0xc6g@256d85bbd150cf1',
    'eagleeye-sessionid': 'hvmvL0jbevLv7y5pFv0vihk4Cqw1',
    'eagleeye-traceid': 'e15f96e11724910500656100150cf1',
    'origin': 'https://passport.goofish.com',
    'priority': 'u=1, i',
    'referer': 'https://passport.goofish.com/mini_login.htm??lang=zh_cn&appName=xianyu&appEntrance=oauth&styleType=auto&bizParams=&notLoadSsoView=true&notKeepLogin=false&isMobile=false&returnUrl=http%3A%2F%2Fopen.api.goofish.com%2Fauthorize%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%3A%2F%2Faldsidle.agiso.com%2FIdle%2FLoginAuth%26state%3Dddb828d785774cd5b9e9f39907e2ca50%26sp%3Dxianyu%26client_id%3D32712170&rnd=0.5757863900645448',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

params = {
    'appName': 'xianyu',
    'fromSite': '77',
    '_bx-v': '2.5.11',
}

data = (f'phoneCode=86&loginId={phone}&countryCode=CN&codeLength=6&isIframe=true&documentReferer=https%3A%2F%2Fopen.api.goofish.com%2F&defaultView=sms&ua=140%23VAOrAc1ZzzZ33zo2LZHuAtSogZYCifzYN4abARbOzBbLw5sc4%2BQ54clXWmf6TlJwdPjtP24bcjUvNFzaN%2FPZ3tbmmQN4lp1zzXc2tr3xFzzxJm8za3Jjzzrb22U3lp1xz1juVczV2brrLPc3L6gqzzrSxj0ODIuxnIcziXZ7dmdvOSvZrI7ZbIE9rmSOKPxyxB2igmLBQb45wijojnm%2B%2Fkm8K7MjGHxsY9M7Tqf4e08vgpeu8ITgM5L3mSDt%2BSHFtVS0T0dxMntv0GCHzpwkKfjLl4Md7sj%2Fzwz5sqgwyahygZ%2BnWeFuYJ9Q0IPbbS%2FyNil1U%2F6wLG%2BETelOsQqlc1F6QHlEFdNN4t8MHg8t3I9j8Uyisdd47u06cq2yopNWyIy6c6nVpDLSX81TcQecQFcO1KnRaBUw2wpGffmgqut%2FgxuNzDFAhjSWJ4SA4FWx3q1D2BULMQsD%2BdGrYx0PQdo6jHOseYm2NLZbGEsO0WK4%2BIRJE4Z73uLK8mYhZfCvrIq1rjNg1x4vCdrVxZnZ4YiFXG0eoIbMDOTi04maemnrkT4DqOeNBHCcFiFaOIxXWYnrjBUF8nN8tcbH65Jg1WGpu5mXL8bzA2F1RWHvX0doRehczCGMi8A%2FdvxKgekgVsxnijPVVkym3Ibv6tJiyRzLqpGI9Ieg5V5v%2BcIupAHAgR7rdV1saRO7K2XSB4Feel%2BhHSLul50dpr3%2F%2FEziYlOkYjSIIYc%2Fn4y0ejODGan61YfA499XbDsEaVx6K3c6OCQyAOzGZw%2FjBHGdc6%2FZMW%2BZHRRM3P9GueWh6LZtsaYjxDo34XbSApJZtHInWdwMK3PX8LM8DOUBmbllxKgqQRWCHu4TzHoMoqRIzJlqXargRA%2F3lpNfiQNo90d1uQIhXg3QUiLY72I0pMuWsOCNzxfw7fsGOa%2FIddNqy3MRXOi3deWCSHBN1dtxzMTKP47HKuBjBeO7sTP60KXYzuJzx0Q36mJYGSp9wz8w56dDDtd7KK1d1Ibkm0pm7g1pxeiZirxLK0usUrvtggiL1JraQjM%2Fl0a1ana3Y9H4MCTY7mbWwndbGthBkmxxyMz0TnAXHYNkCxmbT3H0BBz0Z9nyP7F2VlGe4Cdl2vy6YZKQmhcVFhxSj3ae7S%2FRZGwzUUtL%2FVP8fUApUnQ7JpUsTkO176eQM1Ss%2FZv3XpQ61XQbZNQ4a2ZVoL4MwK76rZs4EOk5nyE%2F%2BYpna8cCmnDfqRnxrJWmdfu3PLanJCkM%2BPUK%2BsFLI%2BtoeDuTUX7wgM8ikLvs2iHBbaJ560FbMz6yu52NSCoVMFGcekldzBWSyUQGeV82nGr9qF50PjyBay59DqLy9DvTDVHUMkNOoLSmGnohOu0%2F7sepfsQiwqIUIUkOK%2B8cJjFC5ZPnfVtNvlPa3j%2FbO1FXlC0o%2B60jWylQSQo9sxnZZMf77VnbzTHNg0OU%2FLBjYDFKTLF14j8C9O232Bt1aRNjKagZfW%2BAOwM1x7VFMz%3D%3D&umidGetStatusVal=255&screenPixel=2560x1440&navlanguage=zh-CN&navUserAgent=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F128.0.0.0%20Safari%2F537.36&navPlatform=Win32&appName=xianyu&appEntrance=oauth&_csrf_token=dfFMIzQMeZxi94GFKDGLH4&umidToken=fb1bac1b7eac0049163799578c006e6fe862c3e3&hsiz=1429fc5358d61a3f58deb9a409208899&bizParams=taobaoBizLoginFrom%3Dgoofish%26renderRefer%3Dhttps%253A%252F%252Fopen.api.goofish.com%252F&mainPage=false&isMobile=false&lang=zh_CN&returnUrl=http%3A%2F%2Fopen.api.goofish.com%2Fauthorize%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%3A%2F%2Faldsidle.agiso.com%2FIdle%2FLoginAuth%26state%3Dddb828d785774cd5b9e9f39907e2ca50%26sp%3Dxianyu%26client_id%3D32712170&fromSite=77&umidTag=SERVER&weiBoMpBridge=&jsVersion=0.10.1&deviceId=&pageTraceId=213e394117249104782631556e0c85&bx-ua=228!tAmT0RYJRRowhmbU9b65gAGTQzA9C0mcDHN71MWQfWdhlGAbY6DLsOq4Boic3cR3g3IRwoRZe7HRKFRz+NyfAEpwDlsxL04HXFA+o87g9tjn87PLk0awV1sEzSiOHLWWo4cINr8RZdrwQLEeeNx7dWjGXIVYL2l4MmJnKSDZvW5loiOAQytYRl0mFp7yRKoAl/IcKl1/mAAR1DqPRVmgAURRF67yIC/ZlDYPsl1GmAoRzDqPRfJgLURRCA7yYvopRRIPKRGYmAoSTDqWRkGNrURRPr1IR+D4eUI1Ko6smAlRRS2cVzyBAlkRXV7IRC/eTmrqFomYjO5UTG7PRj5gAT6lF8BnpZxEg0HKvzXlXE9cF6W+1s6DukQMHr8dsOrVFL3nKazPXEQci53s6HveBM3+f5WVZ7KyHDinJFrwNWQ+F63n62v8EMqcK5WVwPuFiMQsJqSiBEQpF6j8UJJLw3HV8/RAn/nMIqXEuaeYhoH/Yozcor+VzJ2vhPSk+bDuunR7JN6U4mW7QVTit1FnfCKUQO03ckVNFcI8mAiCT03bqixReEz6dKeXVo95NhxqeVA+/8/6MNR18KIizCW+XnLJUiy9XBbVWE7keVoyygFyJhVQXHPd2PiLifwvqtxHHarTeblxTryHvr1SGirmjlVZ4HxbFGFjb2M+XCks48GD2rYwQ5kRIlztJhMJQeu1D3+Dz+VghLqBPzKxnFZoiVMEi4FQZO/t3STu+TNSKIlHIeIrOe0upEMxvR9z1PqyDYGgXgSH2zu0qEcBi5yueJkq3jtAhVqA9mLdKAeKSzAbb33quaIGUhBQeiteS36j5MIJDxgKnYJb/0J6aXoyk/9CtTunsETyNusSX0wGeebuLVP0FgnVLfa2jGGeixUyS6HJjzM5szjz0BCRsxiHeuVtoFFfd1NmYt+EJs2zu9DxjjCtk/cc4sXxbq9+Qi0SznvbLK0a/AFdfN64CBzEXfaXjzZP5ZVCPLeggcv0oqJqqsaqJRcepa4KqfR2337OaaQ/aeteBv2wRtsugyXAeGGd/xQVk3XD+vwYW/fA+iRHgje2Nn65/swg5V01V1RjvyRczMZ7KCtKBg1vMNghvKMdL+LQNpm9vC9/QBWVudaXzmOCLRqf+fr4UZEf2Ef/ddARfXY/axCmD2OovzdtJo/Fc3H9s5d674nXMTb3Nzl3Eb0JfpUlq2fOVMDpzEYX7ZyN6hTSe9sZEeiM1fVn+1rMSMyyqi0Bm2KOl0dbCHOKed4jMH8aXAgA7X7OqpM/ZL473lGwi7oa/FthiIegAEaw3eCqPruf1EyHIW4BS8pii+UM6lI45F/etdWUN1Um7estdHSvFw8wgeSfLXt0uuSDcXDYhaXgD9th9MvhTzDNPOCjAx0yK47WHg0VO8EhqrmXeeiPvWL6i7WHpIkGLky4ZT2/g1biijrDDgu3/ieotPHteVNQJO9WC8YFnM5KCqIwpAGE5rlqiMvMjKSCowpFrjO99XPW+9jQobAO7PFGAyOKX/OyTaOd+UTDfqEwnJygH5IaUI2r5xI1QxJywRotNPMEP5ybftV1aZCFONn9hH7V90zB/om9/I8osEe3q/OiAEalHXZ2QreL&bx-umidtoken=T2gAjpao-G3davGAFvYZ7wA9zTOixX3RuS6wIf5YD9mqieBF55iXkrfzNa7WvVYJG8w=')

response = requests.post(
    'https://passport.goofish.com/newlogin/sms/send.do',
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