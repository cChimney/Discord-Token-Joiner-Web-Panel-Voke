import requests
import random
import time
with open("info/proxies.txt", 'r+') as f:
    proxyarray = f.read().splitlines()
    proxyarray.sort()
with open("info/tokens.txt", 'r+') as f:
    tokens = f.read().splitlines()
    tokens.sort()
def join(link):
        url = "https://discordapp.com/api/v9/experiments"
        r=requests.get(url).json()
        fingerprint = r["fingerprint"]

        posturl = f"https://discord.com/api/v8/invites/{link}"
        proxy = random.choice(proxyarray)

        proxies = {
                'http': 'http://' + proxy,
                'https': 'http://' + proxy
        }

        headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'de',
                'authorization': random.choice(tokens),
                'content-length': '0',
                'cookie': '''__cfduid=d29b03c861c9946a94d03a0496cd094881618767505; __dcfduid=39c9736a6f12e98b7067efa27ab53c6a; locale=de; _ga=GA1.2.1440912255.1618809286; _gid=GA1.2.384772034.1618809286; __stripe_mid=392b57df-a061-4026-82e7-7d7d04e2097907427b; __stripe_sid=b7eb9154-6794-4726-9097-04dbc28cd69216e93c''',
                'origin': 'https://discord.com',
                'referer': 'https://discord.com/channels/@me',
                'sec-ch-ua': '''"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"''',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
                'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjMyNTAxNzA5ODU5MjA1OTM5MiIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI2Njc0NzQ2MjYzMzAyMzA3ODQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlLURFIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg5LjAuNDM4OS4xMjggU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijg5LjAuNDM4OS4xMjgiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODI1OTAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                'x-fingerprint': fingerprint,
        }
        r = requests.post(posturl, headers=headers, timeout=10, proxies=proxies)
        print(r.text)
def spam(invite, channel,message):
        url = "https://discordapp.com/api/v9/experiments"
        r=requests.get(url).json()
        fingerprint = r["fingerprint"]
        posturl = f"https://discord.com/api/v9/invites/{invite}"
        proxy = random.choice(proxyarray)
        token = random.choice(tokens)
        proxies = {
                'http': 'http://' + proxy,
                'https': 'http://' + proxy
        }

        headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'de',
                'authorization': token,
                'content-length': '0',
                'cookie': '''__cfduid=d29b03c861c9946a94d03a0496cd094881618767505; __dcfduid=39c9736a6f12e98b7067efa27ab53c6a; locale=de; _ga=GA1.2.1440912255.1618809286; _gid=GA1.2.384772034.1618809286; __stripe_mid=392b57df-a061-4026-82e7-7d7d04e2097907427b; __stripe_sid=b7eb9154-6794-4726-9097-04dbc28cd69216e93c''',
                'origin': 'https://discord.com',
                'referer': 'https://discord.com/channels/@me',
                'sec-ch-ua': '''"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"''',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
                'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjMyNTAxNzA5ODU5MjA1OTM5MiIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI2Njc0NzQ2MjYzMzAyMzA3ODQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlLURFIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg5LjAuNDM4OS4xMjggU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijg5LjAuNDM4OS4xMjgiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODI1OTAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                'x-fingerprint': fingerprint,
        }
        r = requests.post(posturl, headers=headers, timeout=10, proxies =proxies)

        headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'de',
                'authorization': token,
                'content-length': '0',
                'cookie': '''__cfduid=d29b03c861c9946a94d03a0496cd094881618767505; __dcfduid=39c9736a6f12e98b7067efa27ab53c6a; locale=de; _ga=GA1.2.1440912255.1618809286; _gid=GA1.2.384772034.1618809286; __stripe_mid=392b57df-a061-4026-82e7-7d7d04e2097907427b; __stripe_sid=b7eb9154-6794-4726-9097-04dbc28cd69216e93c''',
                'origin': 'https://discord.com',
                'referer': f'https://discord.com/channels/{channel}',
                'sec-ch-ua': '''"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"''',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
                'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjMyNTAxNzA5ODU5MjA1OTM5MiIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI2Njc0NzQ2MjYzMzAyMzA3ODQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlLURFIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg5LjAuNDM4OS4xMjggU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijg5LjAuNDM4OS4xMjgiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODI1OTAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                'x-fingerprint': fingerprint,
        }
        for i in range(5):
                time.sleep(0.2)
                requests.post(f"https://discord.com/api/v9/channels/{channel}/messages", headers = headers, json={"content": message},proxies = proxies)

def frq(id,id2):
        proxy = random.choice(proxyarray)
        proxies = {
                'http': 'http://' + proxy,
                'https': 'http://' + proxy
        }

        userDiscrim = id.split('#')[0]
        userName = id.split('#')[1]
        url = f"https://discord.com/api/v9/users/@me/relationships/{id2}"
        token = random.choice(tokens)
        headers = {
                "Content-Type": "application/json",
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-GB',
                'authorization': token,
                'cookie': '''__cfduid=d29b03c861c9946a94d03a0496cd094881618767505; __dcfduid=39c9736a6f12e98b7067efa27ab53c6a; locale=de; _ga=GA1.2.1440912255.1618809286; _gid=GA1.2.384772034.1618809286; __stripe_mid=392b57df-a061-4026-82e7-7d7d04e2097907427b; __stripe_sid=b7eb9154-6794-4726-9097-04dbc28cd69216e93c''',
                'origin': 'https://discord.com',
                'referer': f'https://discord.com/channels/@me/{id2}',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
                'x-context-properties': 'eyJsb2NhdGlvbiI6IkNvbnRleHRNZW51In0=',
                'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk0LjAuNDYwNi44MSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTQuMC40NjA2LjgxIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2Rpc2JvYXJkLm9yZy8iLCJyZWZlcnJpbmdfZG9tYWluIjoiZGlzYm9hcmQub3JnIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjEwMTQ1MSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='
        }
        json={"discriminator": userDiscrim, "username": userName}
        f=requests.put(url,headers=headers,json=json,proxies=proxies)
        print(f.text)