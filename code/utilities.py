import requests
import requests_cache
import pandas as pd
requests_cache.install_cache("my_cache", backend="sqlite")

proxy = {"http": "192.168.86.235:36343", "https": "192.168.86.235:36343"}
cookies = {
    'site': 'US-DK',
    'VIDN': '24569054279',
    'SIDN': '40344408528',
    'SSIDN': '42499056457',
    'SN': '1223548523',
    'LID': '1',
    'EXC': '42499056457:73',
    'gatsby-siteExp': 'US-IL',
    'networkType': 'hosted',
    '_csrf': 'f62cf58d-3bd5-4b99-a3c5-f5e81b8e26c6',
    'STIDN': 'eyJDIjoxMjIzNTQ4NTIzLCJTIjo0MDM0NDQwODUyOCwiU1MiOjQyNDk5MDU2NDU3LCJWIjoyNDU2OTA1NDI3OSwiTCI6MSwiRSI6IjIwMjItMTEtMTJUMTk6MTc6NDYuNjAwODQyOVoiLCJTRSI6IlVTLURLIiwiVUEiOiI5dTVScEFFa1N4QlZWcU9mWW1zY1FuYU01ZE1RNlFBVVlZYm9DOWVnb1NJPSIsIkRLIjoiNjcyNGYyMGEtODcxNS00NmU1LTk1NzUtNzZmNGI1MDY3Nzk0IiwiREkiOiJjZmVlZWJkNC01YTI1LTQyNTYtYjI4Yi1jMzZiZmE3Mzk3ZTciLCJERCI6MjE1NTkwMjYyODB9',
    'STH': '99d8d1f639d842fefa4b6eee209a750b26aa1e65469e0774752f658649df1951',
    'bm_sz': 'EA76B61142B9A99C84C5AC193B91E688~YAAQiBwhFxK972SEAQAAX1UrbREW21YT0QqDyOB8briYvPJY+2ChIZwVk/ChWUTKVeXb6OnsQZKrXzud1/c/xNMlSgdzCfQioEmam9/wOgqW8BXRuyVdpKIbkvuxsl9hR+cnB83320yBz5JHoJ7H86D6riVEB7uVcmXjBWB4iDsgA+zooSvv07yXLI96YCIP3ak2jDlzAC7Hny5aOqULZr/KeM73c1i9kqALpjbujy0eAiDGtWlivA+x7VmMGwtwOSkhVg5RTb7unZ9k4H2u4pTH0CKrqN0pjTq4vjRZsDKkP9nuAo8N~3421749~4404037',
    'notice_behavior': 'implied,eu',
    '_abck': '823CF648B56B07E29F497B5B277751A9~0~YAAQiBwhF62972SEAQAAlFwrbQiTNNtj7hNbUvM8abXFeQ1HWuKr2vZYTXX1oeFmEPH3zehn2V9+y3ZDzpVBJYU/dW2h8622sWNun65nsqPoxq3qCiIm1tnhuc0PQNgodgBFgxsnexT/q5tj8CBdbBssu7rZhm9fk/O7YZJsSsi+fx03Qn9zkrsYKP3ek9dgZ9iKsaPdB9Ks6MFOuOAr+6pMJ7t7pdIrF6l6mbLbbvGgyL3hIN0Xgqf+OVmmewvSNQGg4XXkxMIqqEKGKBeGFGuk7/W7yjRqmK0BKYbnIBWbHoPhEV4SxrOaGKcSY/677EetVpybhav2vchM4boaqT4u9MVi3u/XL3+el0BARF4v3Ki7tR0NbBMVKWc2MCqolEzCu1eAj7P34gZec51gFqoatO5VR6O9bvsV~-1~-1~-1',
    'uk': '1',
    'PRV': '3P=1&V=24569054279&E=1668365374',
    'SINFN': 'PID=&AOID=&PUID=23261581&SSEG=&GLI=0&LID=1&site=US-DK',
    'mlc': 'true',
    'ak_bmsc': 'DD4425540E5664B9396FAF42ED3E7B49~000000000000000000000000000000~YAAQiBwhFwPm72SEAQAAekUtbRFD+O3rpTf+7ZknsjY7DOx1wwLOVEMAsINLhUvac18zXqixEF36KIRDB1aXteoxNqQtYS5pbBnTTNuhG8g6baAGme14NO/eIc+BfFj76RCGrNTjrLSNqK9CnirmzlSC0QkFDpbU2QwlQxlNsH5G1X4mUpHx3eqvr7516QIJgB8CRUcH4X9j0UJFwzWYEnbXPk+Z6wittUF0XexLkQwp/25sVDx9ZhDotz3SlinWAyzZZ2LM/6BgWYhVE/r3W3LuJQOboY4ifFtpxrEuGpMPJU067xOOitsYZdfXOursMsO+JTdIwomSLq8o9xdzUwcOXP3fRLjaZ8q+QFCCZpuOTI0Pr1pQFT6GfeI//dgIVGKlRCVORug/ajkWZ4jnxry7g5YAq63K4Y+cIMcg',
    'jwe': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImN0eSI6IkpXVCIsInZlcnNpb24iOiIxIn0.eyJ1bmlxdWVfbmFtZSI6InRveGljemlsbGEiLCJ1ayI6IjU5MmVjMjJjLWU5N2YtNGFkZC04Y2FmLTMxMmIxZmExNDJkOCIsInJvbGUiOiJOb3JtYWwiLCJlbWFpbCI6InRveGljemlsbGEyMDAwQG91dGxvb2suY29tIiwicmFmaWQiOiIiLCJ2aWQiOiIyNDU2OTA1NDI3OSIsImxpZCI6IjEiLCJqaWQiOiIxNjM5NDc3NjA1MCIsImprZXkiOiJjdXJyZW50IiwiZnRkYmUiOiJUcnVlIiwiZ2VvIjoiIiwiZnZzIjoiMyIsImNkYXRlIjoiMjAyMi0xMS0xMiAxODo0OTozNFoiLCJjdXIiOiJVU0QiLCJpdiI6IkFYbE9oazBHRnUxc1gzYkw2ODlPN1E9PSIsImV1aWQiOiJRWlkwaXFFc3B3NzVFM0w1cnhkVnFnPT0iLCJES1AtRGVueUFsbENvbnRlc3RzIjoidHJ1ZSIsIkRLUC1EZW55RGVwb3NpdCI6InRydWUiLCJES1AtRGVueVdpdGhkcmF3YWwiOiJ0cnVlIiwiREtQLURlbnlBbGNvaG9sUHJvbW9zIjoidHJ1ZSIsIkRLUC1WaWV3RGZzIjoidHJ1ZSIsIkRLUC1WaWV3TWFya2V0cGxhY2UiOiJ0cnVlIiwic3hwIjoiVVMtREsiLCJhdXRoIjoiMWNmNmVkZmYtODIyNC00YTIyLWJjMmEtZTA5ZWEyZGQ0MTRmIiwibHQiOiJkcmFmdGtpbmdzIiwic2J0IjoiNDg5NzE5ODQiLCJuYmYiOjE2NjgyNzkyODEsImV4cCI6MTY2ODI3OTU4MSwiaXNzIjoidXJuOmRrL2NlcmJlcnVzIiwiYXVkIjoidXJuOmRrIn0.5kGjzWock7tT4o_u6eleTUnEC-jyH0qxMLsVE3KHZVY',
    'iv': 'bERUROpkk97Gd9g6PpgG+QAqr58NFnFJp8D78wzsQ1Y=',
    'hgg': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ2aWQiOiIyNDU2OTA1NDI3OSIsImRrZS02MCI6IjI4NSIsImRraC0xMjYiOiI4MzNUZF9ZSiIsImRrZS0xMjYiOiIwIiwiZGtlLTE0NCI6IjQzMSIsImRrZS0xNDkiOiIzMzczIiwiZGtlLTE1MCI6IjU2NyIsImRrZS0xNTEiOiI0NTciLCJka2UtMTUyIjoiNDU4IiwiZGtlLTE1MyI6IjQ1OSIsImRrZS0xNTQiOiI0NjAiLCJka2UtMTU1IjoiNDYxIiwiZGtlLTE1NiI6IjQ2MiIsImRrZS0xNzkiOiI1NjkiLCJka2UtMjA0IjoiNzEwIiwiZGtlLTIxOSI6IjIyNDYiLCJka2gtMjI5IjoiSWxOaEMwNlMiLCJka2UtMjI5IjoiMCIsImRrZS0yMzAiOiI4NTciLCJka2UtMjg4IjoiMTEyOCIsImRrZS0zMDAiOiIxMTg4IiwiZGtlLTMxOCI6IjEyNjAiLCJka2UtMzQ1IjoiMTM1MyIsImRrZS0zNDYiOiIxMzU2IiwiZGtoLTM5NCI6IkNmWEFoemRPIiwiZGtlLTM5NCI6IjAiLCJka2UtNDA4IjoiMTYxMCIsImRrZS00MTYiOiIxNjQ5IiwiZGtlLTQxOCI6IjE2NTEiLCJka2UtNDE5IjoiMTY1MiIsImRrZS00MjAiOiIxNjUzIiwiZGtlLTQyMSI6IjE2NTQiLCJka2UtNDIyIjoiMTY1NSIsImRrZS00MjkiOiIxNzA1IiwiZGtlLTYzNiI6IjI2OTEiLCJka2UtNzAwIjoiMjk5MiIsImRrZS03MzkiOiIzMTQwIiwiZGtlLTc1NyI6IjMyMTIiLCJka2gtNzY4IjoiVVpHYzBySHgiLCJka2UtNzY4IjoiMCIsImRrZS03OTAiOiIzMzQ4IiwiZGtlLTc5NCI6IjMzNjQiLCJka2UtODA0IjoiMzQxMSIsImRrZS04MDYiOiIzNDI1IiwiZGtlLTgwNyI6IjM0MzciLCJka2UtODI0IjoiMzUxMSIsImRrZS04MjUiOiIzNTE0IiwiZGtlLTgzNCI6IjM1NTciLCJka2UtODM2IjoiMzU3MCIsImRrZS04NjUiOiIzNjk1IiwiZGtoLTg5NSI6IjJ6MERZU0MyIiwiZGtlLTg5NSI6IjAiLCJka2UtOTAzIjoiMzg0OCIsImRrZS05MTciOiIzOTEzIiwiZGtlLTkzOCI6IjQwMDQiLCJka2UtOTQ3IjoiNDA0MiIsImRrZS05NzYiOiI0MTcxIiwiZGtlLTEwODEiOiI0NTg3IiwiZGtlLTExMDQiOiI0Njc2IiwiZGtlLTExMjQiOiI0NzY0IiwiZGtlLTExMjYiOiI0NzY4IiwiZGtoLTExMjkiOiIyOG1oZWZvcCIsImRrZS0xMTI5IjoiMCIsImRrZS0xMTcyIjoiNDk2NCIsImRrZS0xMTczIjoiNDk2NyIsImRrZS0xMTc0IjoiNDk3MCIsImRrZS0xMTg3IjoiNTAxNSIsImRrZS0xMjEwIjoiNTEyNyIsImRrZS0xMjEyIjoiNTE0MSIsImRrZS0xMjEzIjoiNTE0MiIsImRrZS0xMjMxIjoiNTIxMyIsImRrZS0xMjMzIjoiNTIyMSIsImRrZS0xMjQ0IjoiNTI2NyIsImRrZS0xMjQ5IjoiNTI4OSIsImRrZS0xMjU1IjoiNTMyNiIsImRrZS0xMjU5IjoiNTMzOSIsImRrZS0xMjYxIjoiNTM0NyIsImRrZS0xMjcwIjoiNTM4MyIsImRrZS0xMjc3IjoiNTQxMSIsImRrZS0xMjgwIjoiNTQyNyIsImRrZS0xMjkwIjoiNTQ3NCIsImRrZS0xMjkxIjoiNTQ3OCIsImRrZS0xMjk1IjoiNTQ5NSIsImRrZS0xMjk5IjoiNTUwOSIsImRraC0xMzAzIjoiLUxrekFyZUsiLCJka2UtMTMwMyI6IjAiLCJka2gtMTMwNCI6IkFCSDhqM1hUIiwiZGtlLTEzMDQiOiIwIiwibmJmIjoxNjY4Mjc5MjgxLCJleHAiOjE2NjgyNzk1ODEsImlhdCI6MTY2ODI3OTI4MSwiaXNzIjoiZGsifQ.HCFnRnZWI9Rz8cN2k60rbomb8ShNPbgxmJQfCCqzGp0',
    'STE': '"2022-11-12T19:24:44.8287245Z"',
    'bm_sv': '2D5CBA54E4DCE03D8A9A27E64A33BCA6~YAAQmBwhF4ShZ2mEAQAAaLQxbRGgxvSx3jvedPpXcw80niyEQCGOtXuJytvNNbXHn2ELU3ST9ekdsDM1l83a4YPsRiO3PkifHHqOQBvg/75Okc2mssdATcl20Gwhx0+gcLfh2VBoof6htb/+4g2WTqXF7UH8jtXus2a0XgS+bj1p9M5Jd8ovwB5UPioOE7QEfNjn1sto5ihfqst0369xupOuqP/bVGOxhDeDeSunrdim4FsJ3Y2vMBAPJ/vTBcKW0pnlrp8=~1',
}

cookies = {
    'hgg': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ2aWQiOiIyNTM5Mzg3MTEzMyIsImRrZS02MCI6IjI4NSIsImRrZS0xMjYiOiIzNzQiLCJka2UtMTQ0IjoiNDMxIiwiZGtlLTE0OSI6IjMzNzMiLCJka2UtMTUwIjoiNTY3IiwiZGtlLTE1MSI6IjQ1NyIsImRrZS0xNTIiOiI0NTgiLCJka2UtMTUzIjoiNDU5IiwiZGtlLTE1NCI6IjQ2MCIsImRrZS0xNTUiOiI0NjEiLCJka2UtMTU2IjoiNDYyIiwiZGtlLTE3OSI6IjU2OSIsImRrZS0yMDQiOiI3MTAiLCJka2UtMjE5IjoiMjI0NiIsImRraC0yMjkiOiJJbE5oQzA2UyIsImRrZS0yMjkiOiIwIiwiZGtlLTIzMCI6Ijg1NyIsImRrZS0yODgiOiIxMTI4IiwiZGtlLTMwMCI6IjExODgiLCJka2UtMzE4IjoiMTI2MCIsImRrZS0zNDUiOiIxMzUzIiwiZGtlLTM0NiI6IjEzNTYiLCJka2gtMzk0IjoiQ2ZYQWh6ZE8iLCJka2UtMzk0IjoiMCIsImRraC00MDgiOiJZZGFWUm1EWiIsImRrZS00MDgiOiIwIiwiZGtlLTQxNiI6IjE2NDkiLCJka2UtNDE4IjoiMTY1MSIsImRrZS00MTkiOiIxNjUyIiwiZGtlLTQyMCI6IjE2NTMiLCJka2UtNDIxIjoiMTY1NCIsImRrZS00MjIiOiIxNjU1IiwiZGtlLTQyOSI6IjE3MDUiLCJka2UtNzAwIjoiMjk5MiIsImRrZS03MzkiOiIzMTQwIiwiZGtlLTc1NyI6IjMyMTIiLCJka2gtNzY4IjoiVVpHYzBySHgiLCJka2UtNzY4IjoiMCIsImRrZS03OTAiOiIzMzQ4IiwiZGtlLTc5NCI6IjMzNjQiLCJka2UtODA0IjoiMzQxMSIsImRrZS04MDYiOiIzNDI1IiwiZGtlLTgwNyI6IjM0MzciLCJka2UtODI0IjoiMzUxMSIsImRrZS04MjUiOiIzNTE0IiwiZGtlLTgzNCI6IjM1NTciLCJka2UtODM2IjoiMzU3MCIsImRrZS04NjUiOiIzNjk1IiwiZGtoLTg5NSI6IjJ6MERZU0MyIiwiZGtlLTg5NSI6IjAiLCJka2UtOTAzIjoiMzg0OCIsImRrZS05MTciOiIzOTEzIiwiZGtlLTkzOCI6IjQwMDQiLCJka2UtOTQ3IjoiNDA0MiIsImRrZS05NzYiOiI0MTcxIiwiZGtlLTEwODEiOiI0NTg3IiwiZGtlLTExMDQiOiI0Njc2IiwiZGtlLTExMjQiOiI0NzY0IiwiZGtlLTExMjYiOiI0NzY4IiwiZGtoLTExMjkiOiIyOG1oZWZvcCIsImRrZS0xMTI5IjoiMCIsImRrZS0xMTcyIjoiNDk2NCIsImRrZS0xMTczIjoiNDk2NyIsImRrZS0xMTc0IjoiNDk3MCIsImRrZS0xMTg3IjoiNTAxNSIsImRrZS0xMjEwIjoiNTEyNyIsImRrZS0xMjEzIjoiNTE0MiIsImRrZS0xMjMxIjoiNTIxMyIsImRrZS0xMjQ0IjoiNTI2NyIsImRrZS0xMjU1IjoiNTMyNiIsImRrZS0xMjU5IjoiNTMzOSIsImRrZS0xMjYxIjoiNTM0OSIsImRrZS0xMjc3IjoiNTQxMSIsImRrZS0xMjgwIjoiNTQyNyIsImRrZS0xMjg3IjoiNTQ1OCIsImRrZS0xMjkwIjoiNTQ3NCIsImRrZS0xMjk1IjoiNTQ5NSIsImRrZS0xMjk5IjoiNTUwOSIsImRraC0xMzAzIjoiLUxrekFyZUsiLCJka2UtMTMwMyI6IjAiLCJka2gtMTMwNCI6IkFCSDhqM1hUIiwiZGtlLTEzMDQiOiIwIiwiZGtoLTEzMDciOiJ4UTBTSHNZOCIsImRrZS0xMzA3IjoiMCIsImRraC0xMzA4IjoiLTFHR2xmdGsiLCJka2UtMTMwOCI6IjAiLCJka2UtMTMxNCI6IjU1NzIiLCJka2UtMTMyMyI6IjU2MjYiLCJka2UtMTMyNSI6IjU2MzkiLCJka2UtMTMyNyI6IjU2NTEiLCJka2UtMTMyOCI6IjU2NTMiLCJuYmYiOjE2Njk5MjI1OTIsImV4cCI6MTY2OTkyMjg5MiwiaWF0IjoxNjY5OTIyNTkyLCJpc3MiOiJkayJ9._IGFBNeN2fZDI5cnB6LCmXOQjjLHVs6OlbsDgEhFofc',
    'STE': '"2022-12-01T19:56:01.4520254Z"',
    'STIDN': 'eyJDIjoxMjIzNTQ4NTIzLCJTIjo0MTQ3ODE3OTM3MCwiU1MiOjQzNjc3NzE0OTMwLCJWIjoyNTM5Mzg3MTEzMywiTCI6MSwiRSI6IjIwMjItMTItMDFUMTk6NDc6NTUuNDg5NzY4M1oiLCJTRSI6IlVTLURLIiwiVUEiOiJrVTdSWDFDekFkYnAxZ1VMS2ovdzlFME4rR0N1YkJscXJzUzZCTllwVVFRPSIsIkRLIjoiNzI2YzU3MzktYjBiNC00M2UyLWIyNDItMWFkMzg3YjU3OTRkIiwiREkiOiJiOWY2ODhmNC00MDIxLTRhZjAtOTY0ZS02MjdiN2U3MDM0NzAiLCJERCI6MjEyMDU0NzM1MDZ9',
    'STH': '9d1d2138207918c650e4710d14396dac8e686709f60b1e9973b22027d4c91c0f',
    '_abck': '34949E7733B9C6AF1B7A96059294AE88~-1~YAAQH+x7XBtnG4yEAQAA7S0nzwgpzPgBA72h54m/Z4gCgYTSxlxGHPeYQ45qJtkuASw0/n/e5zSIxI7t1eFkUd/p7kq6BlZu80VhepsjAk94WnzsAAOlEpiHGIa//4z5IEPIWldjrYyoTv+TndK+0vMj4rUFPmxD6hg6s8YvQ9/D6py5L+8Yl/bVYzraOzse3zg4KgV8dQ1N/gQbW6ZHT7mWkyDr8UYgDccrXkX9zJvvw0J2j/gFOsP0eVlUMalTBoMLgpxHAN6jZS8jfgfeNljuugyNZp8qA6xt8KBpDz6Bsg+kCm4EcBYjI1ZSDfxzqvEV/SiuOlj+Rrx1em7dK6yNl0V+BnqD+cNV8/EHU3fT7qLYCdc/175aAtU2bwrZhhnBAF398aDw1JSoJdvvRbbErY45+aIQIpV9mQ==~0~-1~-1',
    'VIDN': '25393871133',
    'SN': '1223548523',
    'LID': '1',
    'SINFN': 'PID=&AOID=&PUID=26711549&SSEG=&GLI=0&LID=1&site=US-DK',
    'PRV': '3P=0&V=25393871133&E=1670008659',
    'ss-pid': 'UBp3gSXHUTF4BbNvpZUg',
    'site': 'US-DK',
    'SIDN': '41478179370',
    'SSIDN': '43677714930',
    'EXC': '43677714930:73',
    'ak_bmsc': '51349FED81D259D8B9B8214BE6D35650~000000000000000000000000000000~YAAQlRwhF7Oi8K+EAQAA9lQTzxGgaGXy74Sr/hNZqU374PShokkrJbSElvoalCpmQgmwkXPaq4oejvTG2w4y3KDEot2hTSOztjdnRCLCkBJrHJkMVr6oEcgOwEY5sf3nE7RnDk3qmFLVP6REZS9/oCai14kXKLvtcwFSuojeXGdnPxKppjP7Dr7T00Yf2xZYFBkOfEtNCasbeR0ht8rsCLuLcnK+Vy7V8FK6prEPNKl9eIBbqghvEcglnNpascSNAktAvW+V/+T3h3lnzSRjPQ4U9oe6p1e3pyYRV7zxu7mCjxbHHvvOI1W/vQJAFa05Bk51vCvPrHjUg0XnvKQBDGQDnmtlwjQLA5yItv1/J1k9GtoLQ3Hf+cP9PxjTquivQadpOvd0iX8v6M1XPo8=',
    'bm_sz': 'B19167A5EFBA07087A6C1958F9AD2F55~YAAQlRwhF7Si8K+EAQAA9lQTzxGRDOLf/x7t6OF6WH/JD5E4mhOVtgpuCcqrlRtS+2BpiFe4dPb4GPF1zcLEJyLrKK3xhkd08x8cvVY6f6iEJZSholdVjEW/DS6+arTqag6nAaFoTtw76ZGK6EXHSzX6bkkM1WPAZDGguRIn4ntqrG5ro2T3vdSH6EyVYbSXaVmMPowCrAlLQez8vzx+WHwBmMTQaSilzZu1H8o9aiPFXpAJRIcMUBk834tg0saBe1dO/IulY1taiDud9M6k605WeX6j7uKjujQdzqmE5IFIlhVgSydw~4277815~4539705',
    'bm_sv': '86B697FAC6876D243EB6DABF7F51CB59~YAAQH+x7XBBnG4yEAQAAOCsnzxEA8oFVHG9QPEA2Sf+inR5mWPrTAsrn4Wu0/WGrrCuSLaCFUR6seGqeou0yBI4rQyCY9MSs6wbwYeKoNu3vQfbbmJeZ3Ik/iUmg0bo05Tf/iIPPwbJX91ABO6EhhR0DKaZaNGQ9Lx56JmhoO7cWWDDIDI3h440CqRN/UOr4E3NVXT8Xw16QtxjHJnsyPetDZSGlaHKAWCYw4SGXc6FIOg6+p1505jC6sZD79HlXK/WEIMIl~1',
    '_csrf': '7515b090-5748-4c1f-a906-bd180ad820c9',
    'ASP.NET_SessionId': 'ruo33sq0jixjcxtz2mnveknm',
    'jwe': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImN0eSI6IkpXVCIsInZlcnNpb24iOiIxIn0.eyJ1bmlxdWVfbmFtZSI6Im5hdHZlazMzMzMiLCJ1ayI6IjFlMTk1YzEyLTYxODgtNDZiOC05MjFmLTRhODNmYmEyY2FiZCIsInJvbGUiOiJOb3JtYWwiLCJlbWFpbCI6Im5hdHZlazIyMjJAb3V0bG9vay5jb20iLCJyYWZpZCI6IiIsInZpZCI6IjI1MzkzODcxMTMzIiwibGlkIjoiMSIsImppZCI6IjE2OTUxNDUwNTU2IiwiamtleSI6ImN1cnJlbnQiLCJmdGRiZSI6IlRydWUiLCJnZW8iOiIiLCJmdnMiOiIzIiwiY2RhdGUiOiIyMDIyLTEyLTAxIDE5OjE3OjM4WiIsImN1ciI6IlVTRCIsIml2IjoiaGgzaGJycEY5NmVIK1JlVHNQTm54Zz09IiwiZXVpZCI6Ilgrc1pvVzNiNStvNU5LRkt3MFltUlE9PSIsIkRLUC1EZW55QWxsQ29udGVzdHMiOiJ0cnVlIiwiREtQLURlbnlEZXBvc2l0IjoidHJ1ZSIsIkRLUC1EZW55V2l0aGRyYXdhbCI6InRydWUiLCJES1AtRGVueUFsY29ob2xQcm9tb3MiOiJ0cnVlIiwiREtQLVZpZXdEZnMiOiJ0cnVlIiwiREtQLVZpZXdNYXJrZXRwbGFjZSI6InRydWUiLCJhdXRoIjoiYjlhODhiNWEtZWY3Yi00YjQxLWE4NTctMjQ5ZDgzZGM2NDZlIiwibHQiOiJkcmFmdGtpbmdzIiwic2J0IjoiNTIzNjUzMjIiLCJuYmYiOjE2Njk5MjI1OTIsImV4cCI6MTY2OTkyMjg5MiwiaXNzIjoidXJuOmRrL2NlcmJlcnVzIiwiYXVkIjoidXJuOmRrIn0.2GJtc0bGzrDjp8N9-Ti5w70-_kYpLm8WaiC0BEMTKng',
    'iv': 'e2DDlYHyknKGsv4pyAge3kINk0ROswZx140vi4pQc4M=',
    'uk': '1',
    'mlc': 'true',
    'notice_behavior': 'implied,eu',
    'notice_preferences': '2:',
    'notice_gdpr_prefs': '0,1,2::implied,eu',
    'cmapi_gtm_bl': '',
    'cmapi_cookie_privacy': 'permit 1,2,3',
}

headers = {
    'authority': 'www.draftkings.com',
    'pragma': 'no-cache',
    # 'cache-control': 'no-cache',
    'sec-ch-ua': '";Not A Brand";v="99", "Chromium";v="94"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'site=US-DK; VIDN=24569054279; SIDN=40344408528; SSIDN=42499056457; SN=1223548523; LID=1; EXC=42499056457:73; gatsby-siteExp=US-IL; networkType=hosted; _csrf=f62cf58d-3bd5-4b99-a3c5-f5e81b8e26c6; STIDN=eyJDIjoxMjIzNTQ4NTIzLCJTIjo0MDM0NDQwODUyOCwiU1MiOjQyNDk5MDU2NDU3LCJWIjoyNDU2OTA1NDI3OSwiTCI6MSwiRSI6IjIwMjItMTEtMTJUMTk6MTc6NDYuNjAwODQyOVoiLCJTRSI6IlVTLURLIiwiVUEiOiI5dTVScEFFa1N4QlZWcU9mWW1zY1FuYU01ZE1RNlFBVVlZYm9DOWVnb1NJPSIsIkRLIjoiNjcyNGYyMGEtODcxNS00NmU1LTk1NzUtNzZmNGI1MDY3Nzk0IiwiREkiOiJjZmVlZWJkNC01YTI1LTQyNTYtYjI4Yi1jMzZiZmE3Mzk3ZTciLCJERCI6MjE1NTkwMjYyODB9; STH=99d8d1f639d842fefa4b6eee209a750b26aa1e65469e0774752f658649df1951; bm_sz=EA76B61142B9A99C84C5AC193B91E688~YAAQiBwhFxK972SEAQAAX1UrbREW21YT0QqDyOB8briYvPJY+2ChIZwVk/ChWUTKVeXb6OnsQZKrXzud1/c/xNMlSgdzCfQioEmam9/wOgqW8BXRuyVdpKIbkvuxsl9hR+cnB83320yBz5JHoJ7H86D6riVEB7uVcmXjBWB4iDsgA+zooSvv07yXLI96YCIP3ak2jDlzAC7Hny5aOqULZr/KeM73c1i9kqALpjbujy0eAiDGtWlivA+x7VmMGwtwOSkhVg5RTb7unZ9k4H2u4pTH0CKrqN0pjTq4vjRZsDKkP9nuAo8N~3421749~4404037; notice_behavior=implied,eu; _abck=823CF648B56B07E29F497B5B277751A9~0~YAAQiBwhF62972SEAQAAlFwrbQiTNNtj7hNbUvM8abXFeQ1HWuKr2vZYTXX1oeFmEPH3zehn2V9+y3ZDzpVBJYU/dW2h8622sWNun65nsqPoxq3qCiIm1tnhuc0PQNgodgBFgxsnexT/q5tj8CBdbBssu7rZhm9fk/O7YZJsSsi+fx03Qn9zkrsYKP3ek9dgZ9iKsaPdB9Ks6MFOuOAr+6pMJ7t7pdIrF6l6mbLbbvGgyL3hIN0Xgqf+OVmmewvSNQGg4XXkxMIqqEKGKBeGFGuk7/W7yjRqmK0BKYbnIBWbHoPhEV4SxrOaGKcSY/677EetVpybhav2vchM4boaqT4u9MVi3u/XL3+el0BARF4v3Ki7tR0NbBMVKWc2MCqolEzCu1eAj7P34gZec51gFqoatO5VR6O9bvsV~-1~-1~-1; uk=1; PRV=3P=1&V=24569054279&E=1668365374; SINFN=PID=&AOID=&PUID=23261581&SSEG=&GLI=0&LID=1&site=US-DK; mlc=true; ak_bmsc=DD4425540E5664B9396FAF42ED3E7B49~000000000000000000000000000000~YAAQiBwhFwPm72SEAQAAekUtbRFD+O3rpTf+7ZknsjY7DOx1wwLOVEMAsINLhUvac18zXqixEF36KIRDB1aXteoxNqQtYS5pbBnTTNuhG8g6baAGme14NO/eIc+BfFj76RCGrNTjrLSNqK9CnirmzlSC0QkFDpbU2QwlQxlNsH5G1X4mUpHx3eqvr7516QIJgB8CRUcH4X9j0UJFwzWYEnbXPk+Z6wittUF0XexLkQwp/25sVDx9ZhDotz3SlinWAyzZZ2LM/6BgWYhVE/r3W3LuJQOboY4ifFtpxrEuGpMPJU067xOOitsYZdfXOursMsO+JTdIwomSLq8o9xdzUwcOXP3fRLjaZ8q+QFCCZpuOTI0Pr1pQFT6GfeI//dgIVGKlRCVORug/ajkWZ4jnxry7g5YAq63K4Y+cIMcg; jwe=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImN0eSI6IkpXVCIsInZlcnNpb24iOiIxIn0.eyJ1bmlxdWVfbmFtZSI6InRveGljemlsbGEiLCJ1ayI6IjU5MmVjMjJjLWU5N2YtNGFkZC04Y2FmLTMxMmIxZmExNDJkOCIsInJvbGUiOiJOb3JtYWwiLCJlbWFpbCI6InRveGljemlsbGEyMDAwQG91dGxvb2suY29tIiwicmFmaWQiOiIiLCJ2aWQiOiIyNDU2OTA1NDI3OSIsImxpZCI6IjEiLCJqaWQiOiIxNjM5NDc3NjA1MCIsImprZXkiOiJjdXJyZW50IiwiZnRkYmUiOiJUcnVlIiwiZ2VvIjoiIiwiZnZzIjoiMyIsImNkYXRlIjoiMjAyMi0xMS0xMiAxODo0OTozNFoiLCJjdXIiOiJVU0QiLCJpdiI6IkFYbE9oazBHRnUxc1gzYkw2ODlPN1E9PSIsImV1aWQiOiJRWlkwaXFFc3B3NzVFM0w1cnhkVnFnPT0iLCJES1AtRGVueUFsbENvbnRlc3RzIjoidHJ1ZSIsIkRLUC1EZW55RGVwb3NpdCI6InRydWUiLCJES1AtRGVueVdpdGhkcmF3YWwiOiJ0cnVlIiwiREtQLURlbnlBbGNvaG9sUHJvbW9zIjoidHJ1ZSIsIkRLUC1WaWV3RGZzIjoidHJ1ZSIsIkRLUC1WaWV3TWFya2V0cGxhY2UiOiJ0cnVlIiwic3hwIjoiVVMtREsiLCJhdXRoIjoiMWNmNmVkZmYtODIyNC00YTIyLWJjMmEtZTA5ZWEyZGQ0MTRmIiwibHQiOiJkcmFmdGtpbmdzIiwic2J0IjoiNDg5NzE5ODQiLCJuYmYiOjE2NjgyNzkyODEsImV4cCI6MTY2ODI3OTU4MSwiaXNzIjoidXJuOmRrL2NlcmJlcnVzIiwiYXVkIjoidXJuOmRrIn0.5kGjzWock7tT4o_u6eleTUnEC-jyH0qxMLsVE3KHZVY; iv=bERUROpkk97Gd9g6PpgG+QAqr58NFnFJp8D78wzsQ1Y=; hgg=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ2aWQiOiIyNDU2OTA1NDI3OSIsImRrZS02MCI6IjI4NSIsImRraC0xMjYiOiI4MzNUZF9ZSiIsImRrZS0xMjYiOiIwIiwiZGtlLTE0NCI6IjQzMSIsImRrZS0xNDkiOiIzMzczIiwiZGtlLTE1MCI6IjU2NyIsImRrZS0xNTEiOiI0NTciLCJka2UtMTUyIjoiNDU4IiwiZGtlLTE1MyI6IjQ1OSIsImRrZS0xNTQiOiI0NjAiLCJka2UtMTU1IjoiNDYxIiwiZGtlLTE1NiI6IjQ2MiIsImRrZS0xNzkiOiI1NjkiLCJka2UtMjA0IjoiNzEwIiwiZGtlLTIxOSI6IjIyNDYiLCJka2gtMjI5IjoiSWxOaEMwNlMiLCJka2UtMjI5IjoiMCIsImRrZS0yMzAiOiI4NTciLCJka2UtMjg4IjoiMTEyOCIsImRrZS0zMDAiOiIxMTg4IiwiZGtlLTMxOCI6IjEyNjAiLCJka2UtMzQ1IjoiMTM1MyIsImRrZS0zNDYiOiIxMzU2IiwiZGtoLTM5NCI6IkNmWEFoemRPIiwiZGtlLTM5NCI6IjAiLCJka2UtNDA4IjoiMTYxMCIsImRrZS00MTYiOiIxNjQ5IiwiZGtlLTQxOCI6IjE2NTEiLCJka2UtNDE5IjoiMTY1MiIsImRrZS00MjAiOiIxNjUzIiwiZGtlLTQyMSI6IjE2NTQiLCJka2UtNDIyIjoiMTY1NSIsImRrZS00MjkiOiIxNzA1IiwiZGtlLTYzNiI6IjI2OTEiLCJka2UtNzAwIjoiMjk5MiIsImRrZS03MzkiOiIzMTQwIiwiZGtlLTc1NyI6IjMyMTIiLCJka2gtNzY4IjoiVVpHYzBySHgiLCJka2UtNzY4IjoiMCIsImRrZS03OTAiOiIzMzQ4IiwiZGtlLTc5NCI6IjMzNjQiLCJka2UtODA0IjoiMzQxMSIsImRrZS04MDYiOiIzNDI1IiwiZGtlLTgwNyI6IjM0MzciLCJka2UtODI0IjoiMzUxMSIsImRrZS04MjUiOiIzNTE0IiwiZGtlLTgzNCI6IjM1NTciLCJka2UtODM2IjoiMzU3MCIsImRrZS04NjUiOiIzNjk1IiwiZGtoLTg5NSI6IjJ6MERZU0MyIiwiZGtlLTg5NSI6IjAiLCJka2UtOTAzIjoiMzg0OCIsImRrZS05MTciOiIzOTEzIiwiZGtlLTkzOCI6IjQwMDQiLCJka2UtOTQ3IjoiNDA0MiIsImRrZS05NzYiOiI0MTcxIiwiZGtlLTEwODEiOiI0NTg3IiwiZGtlLTExMDQiOiI0Njc2IiwiZGtlLTExMjQiOiI0NzY0IiwiZGtlLTExMjYiOiI0NzY4IiwiZGtoLTExMjkiOiIyOG1oZWZvcCIsImRrZS0xMTI5IjoiMCIsImRrZS0xMTcyIjoiNDk2NCIsImRrZS0xMTczIjoiNDk2NyIsImRrZS0xMTc0IjoiNDk3MCIsImRrZS0xMTg3IjoiNTAxNSIsImRrZS0xMjEwIjoiNTEyNyIsImRrZS0xMjEyIjoiNTE0MSIsImRrZS0xMjEzIjoiNTE0MiIsImRrZS0xMjMxIjoiNTIxMyIsImRrZS0xMjMzIjoiNTIyMSIsImRrZS0xMjQ0IjoiNTI2NyIsImRrZS0xMjQ5IjoiNTI4OSIsImRrZS0xMjU1IjoiNTMyNiIsImRrZS0xMjU5IjoiNTMzOSIsImRrZS0xMjYxIjoiNTM0NyIsImRrZS0xMjcwIjoiNTM4MyIsImRrZS0xMjc3IjoiNTQxMSIsImRrZS0xMjgwIjoiNTQyNyIsImRrZS0xMjkwIjoiNTQ3NCIsImRrZS0xMjkxIjoiNTQ3OCIsImRrZS0xMjk1IjoiNTQ5NSIsImRrZS0xMjk5IjoiNTUwOSIsImRraC0xMzAzIjoiLUxrekFyZUsiLCJka2UtMTMwMyI6IjAiLCJka2gtMTMwNCI6IkFCSDhqM1hUIiwiZGtlLTEzMDQiOiIwIiwibmJmIjoxNjY4Mjc5MjgxLCJleHAiOjE2NjgyNzk1ODEsImlhdCI6MTY2ODI3OTI4MSwiaXNzIjoiZGsifQ.HCFnRnZWI9Rz8cN2k60rbomb8ShNPbgxmJQfCCqzGp0; STE="2022-11-12T19:24:44.8287245Z"; bm_sv=2D5CBA54E4DCE03D8A9A27E64A33BCA6~YAAQmBwhF4ShZ2mEAQAAaLQxbRGgxvSx3jvedPpXcw80niyEQCGOtXuJytvNNbXHn2ELU3ST9ekdsDM1l83a4YPsRiO3PkifHHqOQBvg/75Okc2mssdATcl20Gwhx0+gcLfh2VBoof6htb/+4g2WTqXF7UH8jtXus2a0XgS+bj1p9M5Jd8ovwB5UPioOE7QEfNjn1sto5ihfqst0369xupOuqP/bVGOxhDeDeSunrdim4FsJ3Y2vMBAPJ/vTBcKW0pnlrp8=~1',
}


def get_contest_details(id, headers, proxy):
    import requests
    import requests_cache
    requests_cache.install_cache("my_cache", backend="sqlite")
    url = f"https://api.draftkings.com/contests/v1/contests/{id}?format=json"
    resp = requests.get(url, headers=headers, proxies=proxy)
    return resp

def get_draft_group_id(contest_id, headers = {}, proxy = {}):
    resp = get_contest_details(contest_id, headers = headers, proxy = proxy)
    return resp.json()['contestDetail']['draftGroupId']

def get_lineups(contest_id,  headers = {}, proxy = {}):
    draft_id = get_draft_group_id(contest_id)
    url = f"https://api.draftkings.com/draftgroups/v1/draftgroups/{draft_id}/draftables?format=json"
    resp = requests.get(url, headers=headers, proxies=proxy)
    return resp

def get_lineups_by_draft_id(draft_id, headers = {}, proxy = {}):
    url = f"https://api.draftkings.com/draftgroups/v1/draftgroups/{draft_id}/draftables?format=json"
    resp = requests.get(url, headers=headers, proxies=proxy)
    return resp

def get_leaderboard_and_lineups(index, contest_id,  headers = {}, proxy = {}):
    url = f"https://api.draftkings.com/scores/v1/leaderboards/{contest_id}?format=json&embed=leaderboard"
    resp = requests.get(url, cookies=cookies, headers=headers, proxies=proxy)
    data = resp.json()
    try:
        data["lineups"] = get_lineups_by_draft_id(data["leader"]["draftGroupId"]).json()
        with open(f"data/draftkings_contest_data_new_5000/{index}_{contest_id}_leaderboard.json", "w") as f:
            import json
            f.write(json.dumps(data))
        return data
    except Exception:
        return

def get_fantasy_cruncher_contest_data():
    import pandas as pd
    df_arr = []
    for year in range(2016, 2023):
        df = pd.read_csv(f"data/consolidated_data/fantasy_cruncher_{year}.csv")
        df_arr.append(df)
    data = pd.concat(df_arr)
    return data


def get_past_contest_lineups():
    data = get_fantasy_cruncher_contest_data()
    filtered_data = data[data["site"].isin(["draftkings"])]
    site_ids = filtered_data[["site", "site_id"]]
    for row in site_ids.iloc[-5000:].iterrows():
        site_id = row[1]["site_id"]
        get_leaderboard_and_lineups(row[0], site_id)
        import time
        time.sleep(10)


def get_contest_today():
    response = requests.get('https://www.draftkings.com/lobby/getcontests')
    if response.status_code >= 200:
        df = pd.DataFrame.from_records(response.json()["Contests"])
        return df
    return {}


def get_lineup_today(headers = {}, proxy = {}):
    today = get_contest_today()
    today = today[today["n"].str.contains("NBA")]
    contest_ids = today["id"]
    contest = {}
    for id in contest_ids:
        draft_id = get_draft_group_id(id)
        info = get_draft_info(draft_id)
        sport = info["draftGroup"]["contestType"]["sport"]
        if sport == "NBA":
            contest[id] = draft_id
    unique_draft_id = {}
    for k, v in contest.items():
        if v not in unique_draft_id.values():
            unique_draft_id[k] = v
    lineups = {}
    #print(unique_draft_id)
    for contest_id, draft_id in unique_draft_id.items():
        lineup = get_lineups_by_draft_id(draft_id, headers = headers , proxy = proxy)
        if lineup.status_code >= 200:
            lineups[contest_id] = lineup.json()["draftables"]
    return lineups

def get_draft_info(draft_id):
    resp = requests.get(f"https://api.draftkings.com/draftgroups/v1/{draft_id}?format=json")
    return resp.json()


def draftkings_pipeline():
    lineups = get_lineup_today()
    # get game logs for each player in lineup
    # predict fantasy points for each player
    # run through optimizer

def see_lineup_info(lineups):
    unique_name = []
    data = {}
    array = list(lineups.items())
    total = len(array)
    count = 1
    for contest_id, draft_tables in list(lineups.items()):
        df = pd.DataFrame.from_records(draft_tables)
        # print(f"contest_id: {contest_id}")
        draft_id = get_draft_group_id(contest_id)
        # print(f"draft_id: {draft_id}")
        lineup_gamelogs = {}
        try:
            df = df[["displayName", "salary", "status", "position"]] 
            for name in df["displayName"]:
                # get game logs for this player
                if name not in unique_name:
                    unique_name.append(name)
            for name in unique_name:
                # print(name)
                pass
            total_name = len(unique_name)
            name_count = 1
            for name in unique_name:
                #print(f"draft group count: {count}/{total}")
                #print(f"player count: {name_count}/{total_name}")
                name_count += 1
                gamelogs = get_player_info(name)
                lineup_gamelogs[name] = gamelogs
            #print(df.head())
        except Exception as e:
            print(e)
            # print(df)
            # print(contest_id)
        data[draft_id] = lineup_gamelogs
        count += 1
    #print(len(unique_name))
    return data

def get_player_info(name):
    import difflib
    from code.get_basketball_reference import get_all_players, get_available_years, get_game_logs_all
    players = get_all_players()
    name = difflib.get_close_matches(name, players["player"])[0]
    df = players[players["player"] == name]
    player_path = df.iloc[0]["player_url"]
    gamelogs_path = get_available_years(player_path)
    df_advanced = get_game_logs_all(name, gamelogs_path, advanced=True)#, no_remote=True)
    df = get_game_logs_all(name, gamelogs_path, advanced=False, new_only=True)#, no_remote=True)
    return pd.concat([df, df_advanced], axis="columns")