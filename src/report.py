import plotly.express as px

def print_summary(df):
    print("\n--- IFRS 17 Portfolio Summary ---")
    print(df[["Contract", "Classification", "BEL",
              "Risk_Adjustment", "Total_Liability",
              "Annual_CSM_Release"]].to_string(index=False))
    
    print("\n--- Portfolio Totals ---")
    totals = df[["BEL", "Risk_Adjustment",
                 "Total_Liability", "Annual_CSM_Release"]].sum()
    print(totals.to_string())

def plot_charts(df):
    fig1 = px.bar(df, x="Contract", y="Total_Liability",
                  color="Classification",
                  title="Total Liability by Contract")
    
    fig1.show()

    fig2 = px.pie(df, values="Total_Liability",
                  names="Classification",
                  title="Total Liability by Measurement Model")
    
    fig2.show()

    fig3 = px.bar(df, x="Contract", y="Annual_CSM_Release",
                  color="Classification",
                  title="Annual CSM Release by Contract")
    
    fig3.show()

