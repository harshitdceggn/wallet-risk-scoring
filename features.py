import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\91997\Desktop\wallet-risk-scoring\data\datawallet_transactions.csv")
df["avg_eth_per_txn"] = df["total_eth_transacted"] / df["transaction_count"]
df["contract_interaction_density"] = df["unique_contracts_interacted"] / df["transaction_count"]
df["log_eth_transacted"] = np.log1p(df["total_eth_transacted"])
df.to_csv(r"C:\Users\91997\Desktop\wallet-risk-scoring\data\engineered_wallet_data.csv", index=False)
print(df.head())
