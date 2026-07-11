def calculate_risk_adjustment(df):
    df["Risk_Adjustment"] = df["BEL"] * df["Risk_Factor"]
    df["Total_Liability"] = df["BEL"] + df["Risk_Adjustment"]
    return df

def calculate_csm_release(df):
    df["Annual_CSM_Release"] = df.apply(
        lambda row: row["Opening_CSM"] / row["Duration"]
        if row["Classification"] == "GMM"
        else 0,
        axis = 1
    )
    return df
