import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# Afficher un message simple
st.write('Hello World')

# Demander à l'utilisateur d'entrer un film préféré
x = st.text_input('Favorite zMovie?')
st.write(f"Your favorite movie is: {x}")

# Afficher un bouton et exécuter une action lorsque l'utilisateur clique dessus
if st.button("Click Me"):
    st.success("Button clicked!")

# Afficher un titre H2
st.write("## This is a H2 Title!")

# Utiliser markdown pour formater le texte
st.markdown("Streamlit is *really* **cool**.")
st.markdown('''
:red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]  
:gray[pretty] :rainbow[colors] and :blue-background[highlight] text.
''')
st.markdown("Here's a bouquet — :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# Texte multi-ligne
multi = '''If you end a line with two spaces,  
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

# Lecture du fichier CSV
try:
    data = pd.read_csv("movies.csv")
    st.write("### Movies Data")
    st.dataframe(data)
except FileNotFoundError:
    st.error("❌ 'movies.csv' not found in the current directory.")

# Données aléatoires pour graphiques
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.write("### Example Bar Chart")
st.bar_chart(chart_data)

st.write("### Example Line Chart")
st.line_chart(chart_data)

# ----------------------------
# CALCULATE MORTGAGE REPAYMENT
# ----------------------------

st.title("🏠 Mortgage Repayments Calculator")
st.write("### Input Data")
col1, col2 = st.columns(2)

home_value = col1.number_input("Home Value", min_value=0, value=500000)
deposit = col1.number_input("Deposit", min_value=0, value=100000)
interest_rate = col2.number_input("Interest Rate (%)", min_value=0.0, value=5.5)
loan_term = col2.number_input("Loan Term (years)", min_value=1, value=30)

loan_amount = home_value - deposit

# Calcul si le prêt est valide
if loan_amount > 0:
    monthly_interest_rate = (interest_rate / 100) / 12
    number_of_payments = loan_term * 12

    if monthly_interest_rate > 0:
        monthly_payment = (
            loan_amount
            * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
            / ((1 + monthly_interest_rate) ** number_of_payments - 1)
        )
    else:
        monthly_payment = loan_amount / number_of_payments

    total_payments = monthly_payment * number_of_payments
    total_interest = total_payments - loan_amount

    st.write("### Repayments")
    col1, col2, col3 = st.columns(3)
    col1.metric("Monthly Repayments", f"${monthly_payment:,.2f}")
    col2.metric("Total Repayments", f"${total_payments:,.0f}")
    col3.metric("Total Interest", f"${total_interest:,.0f}")

    # Tableau du plan de remboursement
    schedule = []
    remaining_balance = loan_amount

    for i in range(1, number_of_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment
        year = math.ceil(i / 12)
        schedule.append([
            i,
            monthly_payment,
            principal_payment,
            interest_payment,
            max(remaining_balance, 0),  # éviter valeur négative
            year
        ])

    df = pd.DataFrame(schedule, columns=[
        "Month", "Payment", "Principal", "Interest", "Remaining Balance", "Year"
    ])

    st.write("### Payment Schedule (Table)")
    st.dataframe(df.head(24))  # afficher les 2 premières années

    st.write("### Remaining Balance Over Time")
    payments_df = df.groupby("Year")["Remaining Balance"].min()
    st.line_chart(payments_df)
else:
    st.warning("Deposit must be less than Home Value to calculate the loan.")
