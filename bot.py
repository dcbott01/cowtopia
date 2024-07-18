import requests
import time
from colorama import Fore, Style
from datetime import datetime
import random

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Content-Type": "application/json",
    "Connection": "keep-alive",
    "Origin": "https://cowtopia-prod.tonfarmer.com",
    "Pragma": "no-cache",
    "Referer": "https://cowtopia-prod.tonfarmer.com/",
    "Sec-Ch-Ua": "\"Not;A Brand\";v=\"99\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Chain-Id": "43113",
    "X-Lang": "en",
    "X-Os": "miniapp",
}

def get_access_token(query_data):
    url = 'https://cowtopia-be.tonfarmer.com/auth'
    headers["X-Tg-Data"] = query_data 
    try:
        data = {}
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status() 
        return response.json()
    except requests.RequestException as e:
        print(f"Request Error: {e} - Status Code: {response.status_code} - Response Text: {response.text}")
        return None

def info(access_token):
    url = 'https://cowtopia-be.tonfarmer.com/user/game-info?'
    mission_headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": f"Bearer {access_token}",
        "Origin": "https://cowtopia-prod.tonfarmer.com",
        "Referer": "https://cowtopia-prod.tonfarmer.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }
    try:
        response = requests.get(url, headers=mission_headers)
        response.raise_for_status() 
        return response.json()
    except requests.RequestException as e:
        print(f"Request Error: {e} - Status Code: {response.status_code} - Response Text: {response.text}")
        return None

def list_mission(access_token):
    url = 'https://cowtopia-be.tonfarmer.com/mission'
    mission_headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": f"Bearer {access_token}",
        "Origin": "https://cowtopia-prod.tonfarmer.com",
        "Referer": "https://cowtopia-prod.tonfarmer.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }
    try:
        response = requests.get(url, headers=mission_headers)
        response.raise_for_status() 
        return response.json()
    except requests.RequestException as e:
        print(f"Request Error: {e} - Status Code: {response.status_code} - Response Text: {response.text}")
        return None

def check_mission(access_token, key):
    url = 'https://cowtopia-be.tonfarmer.com/mission/check'
    mission_headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": f"Bearer {access_token}",
        "Origin": "https://cowtopia-prod.tonfarmer.com",
        "Referer": "https://cowtopia-prod.tonfarmer.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }
    try:
        data_mission = {
            "mission_key": key
        }
        response = requests.post(url, headers=mission_headers, data=data_mission)
        response.raise_for_status() 
        return response.json()
    except requests.RequestException as e:
        print(f"Request Error: {e} - Status Code: {response.status_code} - Response Text: {response.text}")
        return None

def buy_animal(access_token, factory_id):
    url = 'https://cowtopia-be.tonfarmer.com/factory/buy-animal'
    mission_headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": f"Bearer {access_token}",
        "Origin": "https://cowtopia-prod.tonfarmer.com",
        "Referer": "https://cowtopia-prod.tonfarmer.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }
    try:
        data_buy = {
            "factory_id": factory_id
        }
        response = requests.post(url, headers=mission_headers, data=data_buy)
        response.raise_for_status() 
        return response.json()
    except requests.HTTPError as http_err:
        if http_err.response.status_code == 400:
            print(f"{Fore.RED + Style.BRIGHT}[ Factory is full. Skipping...")
        else:
            print(f"HTTP error occurred: {http_err}")
        return None
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None

def offline_profit(access_token):
    url = 'https://cowtopia-be.tonfarmer.com/user/offline-profit?'
    mission_headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": f"Bearer {access_token}",
        "Origin": "https://cowtopia-prod.tonfarmer.com",
        "Referer": "https://cowtopia-prod.tonfarmer.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }
    try:
        response = requests.get(url, headers=mission_headers)
        response.raise_for_status() 
        return response.json()
    except requests.RequestException as e:
        print(f"Request Error: {e} - Status Code: {response.status_code} - Response Text: {response.text}")
        return None

def claim_profit(access_token):
    url = 'https://cowtopia-be.tonfarmer.com/user/claim-offline-profit'
    mission_headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": f"Bearer {access_token}",
        "Origin": "https://cowtopia-prod.tonfarmer.com",
        "Referer": "https://cowtopia-prod.tonfarmer.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }
    try:
        data_claim = {
            "boost": "false"
        }
        response = requests.post(url, headers=mission_headers, data=data_claim)
        response.raise_for_status() 
        return response.json()
    except requests.RequestException as e:
        print(f"Request Error: {e} - Status Code: {response.status_code} - Response Text: {response.text}")
        return None

def achievement(access_token):
    url = 'https://cowtopia-be.tonfarmer.com/mission/achievement?'
    mission_headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": f"Bearer {access_token}",
        "Origin": "https://cowtopia-prod.tonfarmer.com",
        "Referer": "https://cowtopia-prod.tonfarmer.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }
    try:
        response = requests.get(url, headers=mission_headers)
        response.raise_for_status() 
        return response.json()
    except requests.RequestException as e:
        print(f"Request Error: {e} - Status Code: {response.status_code} - Response Text: {response.text}")
        return None

def daily_claim(access_token, log_id):
    url = 'https://cowtopia-be.tonfarmer.com/mission/achievement/claim'
    mission_headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": f"Bearer {access_token}",
        "Origin": "https://cowtopia-prod.tonfarmer.com",
        "Referer": "https://cowtopia-prod.tonfarmer.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }
    try:
        data_daily = {
            "log_id": log_id
        }
        response = requests.post(url, headers=mission_headers, data=data_daily)
        response.raise_for_status() 
        return response.json()
    except requests.RequestException as e:
        print(f"Request Error: {e} - Status Code: {response.status_code} - Response Text: {response.text}")
        return None

def buy_factory(access_token):
    url = 'https://cowtopia-be.tonfarmer.com/factory/buy'
    mission_headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": f"Bearer {access_token}",
        "Origin": "https://cowtopia-prod.tonfarmer.com",
        "Referer": "https://cowtopia-prod.tonfarmer.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }
    try:
        data_buy = {}
        response = requests.post(url, headers=mission_headers, data=data_buy)
        response.raise_for_status() 
        return response.json()
    except requests.RequestException as e:
        return None

def buy_factory_house(access_token):
    url = 'https://cowtopia-be.tonfarmer.com/factory/upgrade-house'
    mission_headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": f"Bearer {access_token}",
        "Origin": "https://cowtopia-prod.tonfarmer.com",
        "Referer": "https://cowtopia-prod.tonfarmer.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }
    try:
        data_buy_house = {}
        response = requests.post(url, headers=mission_headers, data=data_buy_house)
        response.raise_for_status() 
        return response.json()
    except requests.RequestException as e:
        return None

def print_welcome_message(start_time):
    print(r"""
 
  _  _   _    ____  _   ___    _   
 | \| | /_\  |_  / /_\ | _ \  /_\  
 | .` |/ _ \  / / / _ \|   / / _ \ 
 |_|\_/_/ \_\/___/_/ \_\_|_\/_/ \_\
                                   

    """)
    print(Fore.GREEN + Style.BRIGHT + "COWTOPIA BOT")
    print(Fore.CYAN + Style.BRIGHT + "Jajanin dong orang baik :)")
    print(Fore.YELLOW + Style.BRIGHT + "0x5bc0d1f74f371bee6dc18d52ff912b79703dbb54")
    print(Fore.CYAN + Style.BRIGHT + "Contact Me : t.me/dcbott02")
    print(Fore.RED + Style.BRIGHT + "Update Link: https://github.com/dcbott01/")
    print(Fore.BLUE + Style.BRIGHT + "Tukang Rename MATI AJA")

def main():
    start_time = datetime.now()  
    print_welcome_message(start_time)  
    
    skip_list_mission = False
    user_input = input("Kerjakan Task? (y/n): ").strip().lower()
    if user_input == 'n':
        skip_list_mission = True

    while True:
        try:
            with open('query.txt', 'r') as file:
                queries = file.readlines()
            for query_data in queries:
                query_data = query_data.strip()
                print(f"{Fore.YELLOW+Style.BRIGHT}Getting access token ", end="\r", flush=True)
                auth_response = get_access_token(query_data)
                if auth_response:
                    token = auth_response['data'].get('access_token')
                    user_data = auth_response['data'].get('user', {})
                    firstname = user_data.get('first_name', '')
                    lastname = user_data.get('last_name', '')
                    print(Fore.CYAN + Style.BRIGHT + f"===== [ {firstname} {lastname} ] =====", flush=True)
                    print(f"{Fore.YELLOW+Style.BRIGHT}Getting balance..", end="\r", flush=True)
                    info_response = info(token)
                    buy_factory_response = buy_factory(token)
                    buy_house_response = buy_factory_house(token)
                    profit_response = claim_profit(token)
                    achievement_response = achievement(token)

                    log_id = None
                    if achievement_response and 'data' in achievement_response and 'check_in' in achievement_response['data']:
                        check_in_data = achievement_response['data']['check_in']['data']
                        last_completed = next((day for day in reversed(check_in_data) if day['state'] == 'completed'), None)
                        if last_completed and 'log_id' in last_completed:
                            log_id = last_completed['log_id']

                    if log_id:
                        daily_claim_response = daily_claim(token, log_id)
                        if daily_claim_response:
                            print(f"{Fore.GREEN+Style.BRIGHT}Daily Claim Success {Style.RESET_ALL}           ", flush=True)
                    else:
                        print(f"{Fore.RED+Style.BRIGHT}Daily sudah di claim. Skipping...{Style.RESET_ALL}", flush=True)
                    
                    if profit_response:
                        profit = profit_response.get('data',{}).get('profit',0)
                        print(f"{Fore.GREEN+Style.BRIGHT}[ Profit ]: {profit} {Style.RESET_ALL}           ", flush=True)
                    
                    if not skip_list_mission:
                        mission_response = list_mission(token)
                    
                    if info_response:
                        factories = info_response.get('data', {}).get('factories', [])
                        info_user = info_response.get('data', {}).get('user', [])
                        cow_token = info_user.get('token', 0)
                        money = info_user.get('money', 0)
                        print(f"{Fore.GREEN+Style.BRIGHT}[ Money ]: {money} {Style.RESET_ALL}           ", flush=True)
                        print(f"{Fore.GREEN+Style.BRIGHT}[ $COW ]: {cow_token} {Style.RESET_ALL}           ", flush=True)
                        time.sleep(2)
                        for factory in factories:
                            if not factory.get('lock', False) and factory.get('animal_count', 0) < 5:
                                factory_id = factory.get('factory_id')
                                factory_type = factory.get('type')
                                if factory_id:
                                    print(f"{Fore.YELLOW + Style.BRIGHT}[ Factory ID {factory_id}]: Mencoba membeli Animal...", flush=True)
                                    buy_response = buy_animal(token, factory_id)
                                    if buy_response:
                                        print(f"{Fore.GREEN + Style.BRIGHT}Animal berhasil dibeli !")
                                    else:
                                        print(f"{Fore.RED + Style.BRIGHT}Gagal membeli Animal.")
                                    break  

                    if buy_factory_response:
                        buy_success = buy_factory_response.get('success','')
                        print(f"{Fore.YELLOW + Style.BRIGHT} Mencoba membeli Factory... {buy_success}", flush=True)

                    if not skip_list_mission and mission_response and 'data' in mission_response and 'missions' in mission_response['data']:
                        for mission in mission_response['data']['missions']:
                            mission_name = mission.get('name', 'Unknown')
                            key = mission.get('key', 'Unknown')
                            completed = mission.get('completed', False)
                            time.sleep(1)
                            print(f"{Fore.BLUE+Style.BRIGHT}[ Mission ]: {mission_name} - Status : {completed}{Style.RESET_ALL}")
                            if not completed:
                                check_response = check_mission(token, key)
                                if check_response:
                                    updated_completed = check_response.get('completed', False)
                                    print(f"{Fore.YELLOW+Style.BRIGHT}[ Mencoba Menyelesaikan Mission ]", flush=True)
                    print(Fore.BLUE + Style.BRIGHT + f"\n==========Memproses Akun Berikutnya==========\n", flush=True)
                    time.sleep(2)

            print(Fore.BLUE + Style.BRIGHT + f"\n==========ALL ACCOUNTS PROCESSED==========\n", flush=True)
            for _ in range(3600):
                minutes, seconds = divmod(3600 - _, 60)
                print(f"{random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE])+Style.BRIGHT}==== [ All accounts processed, Next loop in {minutes} minutes {seconds} seconds ] ===={Style.RESET_ALL}", end="\r", flush=True)
                time.sleep(1)
        except FileNotFoundError:
            print("query.txt file not found. Please create 'query.txt' and populate it with query data.")
            time.sleep(10)  
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            time.sleep(10)  

if __name__ == "__main__":
    main()

