def classify_contract(contract_type, duration):
    if contract_type == "PAA" and duration <= 1:
        return "PAA"
    elif contract_type == "GMM" or duration > 1:
        return "GMM"
    else:
        return "Unclassified"
    
def classify_portfolio(df):
    df["Classification"] = df.apply(
        lambda row: classify_contract(row["Type"], row["Duration"]), axis=1

    )
    return df