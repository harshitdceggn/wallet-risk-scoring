import pandas as pd
import requests
import time

API_KEY = "cqt_rQB96JK8bJm6G9ckKfMWQVpyYxrc" 
CHAIN_ID = 1 
INPUT_FILE = r"C:\Users\91997\Desktop\wallet-risk-scoring\data\wallet_id.xlsx"
OUTPUT_FILE = r"C:\Users\91997\Desktop\wallet-risk-scoring\datawallet_transactions.csv"

def load_wallets(file_path):
    df = pd.read_excel(file_path)
    return df.iloc[:, 0].dropna().unique().tolist()

def fetch_transactions(wallet_address):
    url = f"https://api.covalenthq.com/v1/{CHAIN_ID}/address/{wallet_address}/transactions_v2/"
    params = {"key": API_KEY}
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json().get("data", {}).get("items", [])
        else:
            print(f"Error {response.status_code} for wallet {wallet_address}")
    except Exception as e:
        print(f"Exception for wallet {wallet_address}: {e}")
    return []

def summarize_transactions(wallet, transactions):
    total_tx = len(transactions)
    total_eth = sum(float(tx.get("value", 0)) / 1e18 for tx in transactions if tx.get("value"))
    contract_addresses = {tx.get("to_address") for tx in transactions if tx.get("to_address")}
    return {
        "wallet": wallet,
        "transaction_count": total_tx,
        "total_eth_transacted": total_eth,
        "unique_contracts_interacted": len(contract_addresses)
    }

def main():
    wallets = load_wallets(INPUT_FILE)
    print(f"Found {len(wallets)} wallet(s). Fetching data...")

    all_data = []
    for i, wallet in enumerate(wallets):
        print(f"[{i+1}/{len(wallets)}] Fetching {wallet}...")
        txs = fetch_transactions(wallet)
        summary = summarize_transactions(wallet, txs)
        all_data.append(summary)
        time.sleep(1) 

    df = pd.DataFrame(all_data)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n Data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
