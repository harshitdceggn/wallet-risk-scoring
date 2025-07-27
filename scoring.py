import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def calculate_scores(input_csv_path: str, output_csv_path: str) -> None:
    df = pd.read_csv(input_csv_path)

    features = [
        "transaction_count",
        "total_eth_transacted",
        "unique_contracts_interacted",
        "avg_tx_value_eth",
        "contract_interaction_density",
        "log_eth_transacted"
    ]
    
    df[features] = df[features].fillna(0)
    df[features] = df[features].replace([float('inf'), -float('inf')], 0)

    scaler = MinMaxScaler()
    normalized = scaler.fit_transform(df[features])

    weights = [0.2, 0.2, 0.15, 0.15, 0.15, 0.15]
    raw_scores = normalized.dot(weights)
 
    df["score"] = (raw_scores * 1000).astype(int)
    
    df[["wallet", "score"]].to_csv(output_csv_path, index=False)
    print(f"[✓] Scores saved to: {output_csv_path}")
