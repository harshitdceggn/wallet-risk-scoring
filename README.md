# ⚠️ Wallet Risk Scoring – Compound Protocol

This project assigns risk scores (0–1000) to Ethereum wallets based on their interactions with Compound V2/V3.

---

## 📥 Data Collection

- Wallets were listed in `wallets.xlsx`.
- Transactions were fetched via **GoldRush API**, focusing on Compound-related activity.
- Data was saved and cleaned into CSV format.

---

## 📊 Feature Selection

Engineered features:
- `transaction_count`
- `total_eth_transacted`
- `unique_contracts_interacted`
- `avg_tx_value_eth`
- `contract_interaction_density`
- `log_eth_transacted`

These capture wallet behavior in volume, diversity, and transaction value.

---

## 🧮 Scoring Method

1. **Normalization** using MinMaxScaler.
2. **Weighted sum** of features:
   - Weights: `[0.2, 0.25, 0.2, 0.15, 0.2]`
3. Final score: scaled to range **0–1000**.

---

## ✅ Risk Indicators

- High avg tx value → potential laundering
- High interaction density → abnormal behavior
- Low diversity → limited protocol use

---

## 📁 Output

- `engineered_wallet_data.csv`
- `scored_wallets.csv`


