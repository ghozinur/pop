import requests
import time
from datetime import datetime
from gpm_contract import *
import sys

WALLET = '0x54643E14E6C30b5FBBC6d90eF1b42d7ad45b52bD'

def waktu():
    return datetime.now().strftime("%H:%M:%S")

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://app.gpm.lol',
    'referer': 'https://app.gpm.lol/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

def predict(target_price, question_id):
    
    target_price = float(target_price)
    
    json_data = {
        'token': '73282af8f3d247ca9dfd90bccbe673d3',
        'question_id': question_id,
        'duration': -1,
        'interval': 30,
    }

    response = requests.post('https://app.gpm.lol/api/getPriceHistory', headers=headers, json=json_data)
    a = response.json()['info']['response']['price_history']['token_prices']
    up = 0
    down = 0
    for i in range(5):
        i = i + 1
        # print(a[-i], target_price)
        if a[-i] > target_price:
            up += 1
        elif a[-i] < target_price:
            down += 1
    if up > down:
        return True
    else:
        return False
    
def market_probability(question_id):
    json_data = {
        'question_id': question_id,
        'token': '73282af8f3d247ca9dfd90bccbe673d3',
    }

    response = requests.post('https://app.gpm.lol/api/getMarketProbabilities', headers=headers, json=json_data)
    market_probabilities = response.json()['info']['response']['probabilities']
    if market_probabilities[0] > market_probabilities[1]:
        return True
    else:
        return False
    
def get_output_prediction(question_id, pilihan):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://app.gpm.lol',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }
    amount = 300 * 10**18

    for i in range(4):
        try:
            amount -= 50 * 10**18
            json_data = {
                'question_id': question_id,
                'collateral_amount': amount,
                'outcome_index': pilihan,
                'token': '73282af8f3d247ca9dfd90bccbe673d3',
            }
            # Mengirim permintaan POST ke endpoint API
            response = requests.post(
                'https://app.gpm.lol/api/getMarketBuyPrice', 
                headers=headers, 
                json=json_data
            )

            # Mengecek apakah respons berhasil
            response.raise_for_status()

            # Mendapatkan nilai dari respons JSON
            output_min = response.json()['info']['response']['buy_amount']
            print(f"Output minimum: {output_min / 10**18:.2f} POP", end='\r')
            if output_min > amount * 5:
                return False
            # Mengevaluasi kondisi
            if output_min - amount > 1 * 10**18:
                chance_winning = (output_min - amount) / 10**18
                print(f"Chance winning: {chance_winning:.6f} POP")
                # print(amount, output_min)
                if pilihan == 0:
                    status = yes_unlocked(question_id, output_min, amount)
                    print("Order Placed", status)
                    return status
                elif pilihan == 1:
                    status = no_unlocked(question_id, output_min, amount)
                    print("Order Placed", status)
                    return status

        except requests.exceptions.RequestException as e:
            print(f"Terjadi kesalahan saat mengakses API: {e}")
            break
        except KeyError as e:
            print(f"Terjadi kesalahan parsing respons JSON: {e}")
            break

def get_outout_min(question_id, pilihan):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://app.gpm.lol',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }
    amount = 2000 * 10**18

    for i in range(4):
        try:
            amount -= 500 * 10**18
            json_data = {
                'question_id': question_id,
                'collateral_amount': amount,
                'outcome_index': pilihan,
                'token': '73282af8f3d247ca9dfd90bccbe673d3',
            }
            # Mengirim permintaan POST ke endpoint API
            response = requests.post(
                'https://app.gpm.lol/api/getMarketBuyPrice', 
                headers=headers, 
                json=json_data
            )

            # Mengecek apakah respons berhasil
            response.raise_for_status()

            # Mendapatkan nilai dari respons JSON
            output_min = response.json()['info']['response']['buy_amount']
            print(f"Output minimum: {output_min / 10**18:.2f} POP", end='\r')

            # Mengevaluasi kondisi
            if output_min - amount > 1 * 10**18:
                chance_winning = (output_min - amount) / 10**18
                print(f"Chance winning: {chance_winning:.6f} POP")
                # print(amount, output_min)
                if pilihan == 0:
                    status = yes_unlocked(question_id, output_min, amount)
                    print("Order Placed", status)
                    return status
                elif pilihan == 1:
                    status = no_unlocked(question_id, output_min, amount)
                    print("Order Placed", status)
                    return status

        except requests.exceptions.RequestException as e:
            print(f"Terjadi kesalahan saat mengakses API: {e}")
            break
        except KeyError as e:
            print(f"Terjadi kesalahan parsing respons JSON: {e}")
            break

def get_active_questions():
    params = {
        'page': '1',
        'size': '30',
    }

    json_data = {
        'address': WALLET,
        'token': '73282af8f3d247ca9dfd90bccbe673d3',
        'duration': 604800,
    }

    response = requests.post('https://app.gpm.lol/api/getRecentActivity', params=params, headers=headers, json=json_data)
    a = response.json()['items']
    buy = set()  # Gunakan set untuk operasi lebih efisien
    # Iterasi dari belakang
    for i in reversed(a):
        activity_type = i['activity_type']
        question_id = i['questionId']

        if activity_type == 'redeem':
            buy.discard(question_id)  # Hapus questionId jika ditemukan redeem
        elif activity_type == 'buy':
            buy.add(question_id)  # Tambahkan questionId ke set buy
    # Konversi set kembali ke list (opsional)
    buy = list(buy)
    return buy

# Fungsi untuk membersihkan baris
def clear_line():
    sys.stdout.write("\r" + " " * 80 + "\r")
    sys.stdout.flush()

# Fungsi untuk mencetak status dengan padding
def print_status(line):
    clear_line()
    print(line.ljust(90), end="\r")
    sys.stdout.flush()

# Fungsi utama
def get_active_markets():
    list_questions = []
    last = get_active_questions()
    for quest in last:
        list_questions.append(quest)
    json_data = {'token': '73282af8f3d247ca9dfd90bccbe673d3'}
    last_check_time = 0  # Menyimpan waktu terakhir pengecekan hasil
    for _ in range(10000):
        try:
            response = requests.post('https://app.gpm.lol/api/getActiveMarkets', headers=headers, json=json_data)
            response.raise_for_status()
            items = response.json().get('items', [])
            
            for item in items[:2]:  # Batasi hanya ke dua item pertama
                question_id = item.get('question_id')
                question_text = item.get('question_text', 'Unknown Question')
                target_price = item.get('extra_info', {}).get('target_price', 0)
                trading_end_time = item.get('trading_end_time', 0)
                current_timestamp = int(time.time())
                sisa_detik = trading_end_time - current_timestamp

                # Update status
                if sisa_detik > 10:
                    print_status(f"{question_text} Waktu tersisa: {sisa_detik} detik")

                # Proses jika memenuhi kriteria
                if 10 < sisa_detik < 30 and len(list_questions) < 10 and question_id not in list_questions:
                    print(f"\nQuestion {question_id} is active")
                    predik = predict(target_price, question_id)
                    print(f"Prediction by price: {predik}")
                    market_prob = market_probability(question_id)
                    print(f"Prediction by probability: {market_prob}")

                    if predik and market_prob:
                        print("Decision: Yes")
                        status = get_outout_min(question_id, 0)
                        if status:
                            list_questions.append(question_id)
                    elif not predik and not market_prob:
                        print("Decision: No")
                        status = get_outout_min(question_id, 1)
                        if status:
                            list_questions.append(question_id)
                    else:
                        # print("Hmm tidak pasti.")
                        if predik:
                            print("Decision by predict: Yes")
                            status = get_output_prediction(question_id, 0)
                            if status:
                                list_questions.append(question_id)
                        elif not predik:
                            print("Decision by predict: No")
                            status = get_output_prediction(question_id, 1)
                            if status:
                                list_questions.append(question_id)
     
            current_time = time.time()
            if list_questions and (current_time - last_check_time > 60):  # Update setiap 60 detik
                last_check_time = current_time
                print_status(f"{waktu()} Checking {len(list_questions)} questions every 60 seconds...")
                for q in list_questions[:]:
                    if is_answered(q):
                        print(f"\n{waktu()} Question {q} is answered")
                        balance_before = get_balance()
                        if redeem(q):
                            balance_after = get_balance()
                            if balance_after > balance_before:
                                res = 'Win'
                            else:
                                res = 'Lose'
                            change = balance_after - balance_before
                            if res == 'Win':
                                print(f"{waktu()} Question {q} is redeemed {res} +{change} POP [{balance_after}]")
                            else:
                                print(f"{waktu()} Question {q} is redeemed {res}")
                            # print(f"Balance: {get_balance()} POP")
                            
                            list_questions.remove(q)

        except requests.RequestException as e:
            print(f"\nError during API call: {e}")
        except Exception as e:
            print(f"\nUnexpected error: {e}")

        # Tunggu sebelum iterasi berikutnya
        time.sleep(10)


get_active_markets()
