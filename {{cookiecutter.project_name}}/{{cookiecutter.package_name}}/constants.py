import email

headers_str = """authority: www.linkedin.com
accept: application/vnd.linkedin.normalized+json+2.1
accept-language: en-US,en;q=0.9,ru;q=0.8
cookie: bcookie="v=2&0bed6c9a-2a6c-411c-832d-5a577fa62d45"; bscookie="v=1&20230211094626d738483a-58eb-4676-8d99-6da1ff44b3baAQEizD4r_IiOFiiJySQcgRswQrPWHxG-"; fid=AQGJMYQyzBK87wAAAYY_3shcsSkABCV2qFhCWVmrnv8CjcnSvDdD5Vz9paIz6vHVkb22U362uPw_hg; G_ENABLED_IDPS=google; fcookie=AQFUs5AwfU_a5wAAAYZhvSGNlAe1_8xVFxZ7juCe2tPsJheay01IXuL1i0UfmPYY0xwT7hSeA-XPhHWb_LyVytwUwnM13JOHoJ2dv4sBQsUQ94FixDkE2yeeA-ZKjgP3bUQTsR98T_PRtESC91E1lEgUrsT8jTXbjIGFLmE0lLetCbbSK5IyyiozmEj92Q5UWpUYot5BTyPm_YHUxitUhoBPrH0ia_KskQEJyMfvG-CqOaMH8lTXz4nrG9eeHKOCOTMoEUig98ogNLks4shrtiGEteETIeVXb88747IInXnDTOPi40P8U9wlyPgrYJ5LMXmEcjexGNDneh1HYSxEag==; timezone=Africa/Cairo; li_theme=light; li_theme_set=app; li_sugr=9fb67bf3-d234-42f9-a3bb-3998767bd412; _guid=681af6b1-3951-4c00-86eb-db2ff818b125; AnalyticsSyncHistory=AQIXNarlt7W36QAAAYZhvXJG4PDNEjlbwVhna_UByHw-1KFJ5kmc3Yfg08lBiOUG1FJihkFNyhV22hDnKvgNzA; lms_ads=AQF6HMZP_7bzVAAAAYZhvXNAFlzBR830nIo3hS93oQrbVThNqIFHQ6mx9uDBZwXWOL0HAetsTW9vSmCIn95-YZ6-K_PZf72Q; lms_analytics=AQF6HMZP_7bzVAAAAYZhvXNAFlzBR830nIo3hS93oQrbVThNqIFHQ6mx9uDBZwXWOL0HAetsTW9vSmCIn95-YZ6-K_PZf72Q; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; ln_or=eyI0MzQ2MTM3IjoiZCJ9; _gcl_au=1.1.243186935.1676678907; aam_uuid=65727078034765436080657173591038347615; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19407%7CMCMID%7C66275722156044932350707505884823632532%7CMCAAMLH-1677283865%7C6%7CMCAAMB-1677283865%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1676686265s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C-1681438853; li_rm=AQExm_xN1rSbwAAAAYZh8Hs1GSGsUGRyViWXNhoivrJQujkvGVlqtWJWMNOm8h7TNWUPHpxIwt3IIG7vgbMWTkgFbd4m0yjsi7RZfAj_YnNfQWTFv_hdjaN7vgPDRS5VrVEpO-KUCrR4rZ8DVIq9iHYlU3U207Pl0Gf582I0QXIOabAdVxE3D-uWU91quhDFvT1rp5ppbXjr0T6XQCsEN88kbzWwAmQr1QUoy7pxe_-KCYEoRS5LYovnv9RvpRP0JE_VGWXplRgMOsT_U-p2A2QDSXyHwh6UuOb_Z4krMjlPCdJzu5rLMF4ONtcKnAh3dVUAy2HJ20_rqs-aliQ; li_g_recent_logout=v=1&true; visit=v=1&M; lang=v=2&lang=en-us; g_state={"i_p":1676687698575,"i_l":1}; liap=true; li_at=AQEDAUFNmb0DKoZkAAABhmHyF6cAAAGGhf6bp04AeZ6ci0WhWLcEakOo2ZzcDSDy-sgB_ZHTx2BUZb1IgMbO_YKiBAK8866EYjSjgq9mebO8-rwRKf5kwsz5YuSVvsjb__qCKDxADjgNS2UFhyXWUPwF; JSESSIONID="ajax:8861361918523364449"; sdsc=36%3A1%2C1676680582817%7EJAPP%2C0%7EJBSK%2C-3396762KWkPwdVZTDbf2r66Z3zYHix0poI%3D; UserMatchHistory=AQID4Ppzhk_oEQAAAYZh82SxZUvwFaai4tFno29Xh0rNwZCI4WfBzSJg8I5i-ZogyvHzAOpMM8hYsS5oEJza4edjlZKTZCoGGfdymOSLReDbPO31GFj3lyXlJTkWEh641alWwAXhuXg5RPUQ9Q_xHCj_z4oy4ApJdyhOvu-y15KidAH9G_MpgBtFYWfQOCQnUDMiZEn8LqEKySXVczLcc6CjIBy5D1JcMDXOziQgA-DQe5xd1i0wD8vGvYJmDj_XeCebMmkyK6GYkGWZsg5-4U8lGK7tYzl0Q-KME0M; lidc="b=TB69:s=T:r=T:a=T:p=T:g=3286:u=3:x=1:i=1676680587:t=1676682361:v=2:sig=AQHxTywDxN2GHxUj6PisREVvob_NnSoa"
csrf-token: ajax:8861361918523364449
referer: https://www.linkedin.com/jobs/view/3472312310/
sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "macOS"
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
x-li-deco-include-micro-schema: true
x-li-lang: en_US
x-li-page-instance: urn:li:page:d_flagship3_job_details;a9TlAfrwQoCtJXNcJPjUkg==
x-li-pem-metadata: Voyager - Careers - Job Details=job-posting-prefetch
x-li-track: {"clientVersion":"1.11.9082","mpVersion":"1.11.9082","osName":"web","timezoneOffset":2,"timezone":"Africa/Cairo","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":2,"displayWidth":3584,"displayHeight":2240}
"""
HEADERS = dict(email.message_from_string(headers_str))
