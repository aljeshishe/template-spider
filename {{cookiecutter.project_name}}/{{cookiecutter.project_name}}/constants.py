import email

headers_str = """Host: www.onlinetours.ru
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: application/json, text/plain, */*
Accept-Language: en-GB,en;q=0.5
X-Requested-With: XMLHttpRequest
X-CSRF-Token: 2bqNgNkbks7Hw/Upc6n+UBk8SplBTScrIbMBueg2Blj6P1IK8qgXb4iXtj4+E8RVkaiaWSWVktgp0Mkr/W+SFw==
Connection: keep-alive
Referer: https://www.onlinetours.ru/
Cookie: _onlinetours_session_v3=3787fbd711e1e6118a3f5ed97104f5b4; __ddg1_=AB4tEM9GwbH1xPsHKQgZ; userId=1091686; _ga=GA1.2.1892125833.1662408073; _ym_uid=1662408074959721969; _ym_d=1662408074; advert=141-oteli; sub_id=6e750220026e4851988619144c-20017; current_phone_params=%7B%22advert%22%3A%22141-oteli%22%7D; olt_ft_session=N1JwVitPSFpFeE8zS3czeE52TmFST29oQlh0Vi9rcXZKVDg3SmZ0T0o4UVo5cUdBVDd5VE4xZ3EydHhyTnVmQlFZTTRBWHB1RGNaUFp2cHpEamVNOFdHYm1ZQ1hzRU54U3FYczg5Vng2Y0U9LS1LU2NHSEVCVkVROUoySGtWaEtWcUpnPT0%3D--a8c3211bbe6d0fae100f4ac1c8efde8b60c4555c; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; mindboxDeviceUUID=d5ae28c3-5971-4fe5-9d94-54704c7182e0; directCrm-session=%7B%22deviceGuid%22%3A%22d5ae28c3-5971-4fe5-9d94-54704c7182e0%22%7D; referer_md5=8aa7ce86175c5c6ce6b788e80da935da
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Pragma: no-cache
Cache-Control: no-cache
TE: trailers
"""
HEADERS = dict(email.message_from_string(headers_str))
