import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Hubungkan ke database MariaDB lokal
conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="",
    database="telco_projects"
)

sns.set_theme(style="whitegrid")
colors_binary = ['#4da6ff', '#ff4d4d']

# =========================================================================
# GRAPH 1: CHURN RATE BY CONTRACT
# =========================================================================
query1 = """
SELECT Contract, ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Churn_Rate
FROM telco_churn GROUP BY Contract ORDER BY Churn_Rate DESC;
"""
df1 = pd.read_sql(query1, conn)
plt.figure(figsize=(7, 5))
bars = plt.bar(df1['Contract'], df1['Churn_Rate'], color=['#ff4d4d', '#ff9999', '#b3d9ff'], width=0.5, edgecolor='black')
plt.title('Tingkat Churn Pelanggan Berdasarkan Jenis Kontrak (%)', pad=15, fontweight='bold')
plt.ylim(0, 50)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval}%', va='bottom', ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('churn_by_contract.png', dpi=150)
plt.close()

# =========================================================================
# GRAPH 2: MONTHLY CHARGES BOXPLOT
# =========================================================================
query2 = "SELECT Churn, MonthlyCharges FROM telco_churn;"
df2 = pd.read_sql(query2, conn)
plt.figure(figsize=(7, 5))
sns.boxplot(data=df2, x='Churn', y='MonthlyCharges', palette=colors_binary, width=0.4, linewidth=2)
plt.title('Distribusi Biaya Bulanan berdasarkan Status Churn', pad=15, fontweight='bold')
plt.tight_layout()
plt.savefig('churn_by_monthly_charges.png', dpi=150)
plt.close()

# =========================================================================
# GRAPH 3: INTERNET SERVICE
# =========================================================================
query3 = """
SELECT InternetService, ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Churn_Rate
FROM telco_churn GROUP BY InternetService ORDER BY Churn_Rate DESC;
"""
df3 = pd.read_sql(query3, conn)
plt.figure(figsize=(8, 4.5))
bars = plt.barh(df3['InternetService'], df3['Churn_Rate'], color=['#ff4d4d', '#ff9999', '#a6a6a6'], height=0.5, edgecolor='black')
plt.title('Churn Rate (%) berdasarkan Jenis Layanan Internet', pad=15, fontweight='bold')
plt.xlim(0, 50)
plt.gca().invert_yaxis()
for bar in bars:
    width = bar.get_width()
    plt.text(width + 1, bar.get_y() + bar.get_height()/2, f'{width}%', va='center', ha='left', fontweight='bold')
plt.tight_layout()
plt.savefig('churn_by_internet_service.png', dpi=150)
plt.close()

# =========================================================================
# GRAPH 4: TECH SUPPORT (DONUT CHART)
# =========================================================================
query4 = """
SELECT TechSupport, ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Churn_Rate
FROM telco_churn GROUP BY TechSupport;
"""
df4 = pd.read_sql(query4, conn)
plt.figure(figsize=(6, 6))
plt.pie(df4['Churn_Rate'], labels=df4['TechSupport'], autopct='%1.1f%%', startangle=140, colors=['#ff4d4d', '#4da6ff', '#a6a6a6'], wedgeprops={'edgecolor': 'white', 'linewidth': 2})
centre_circle = plt.Circle((0,0), 0.60, fc='white')
plt.gcf().gca().add_artist(centre_circle)
plt.title('Proporsi Churn Rate\nberdasarkan Ketersediaan Tech Support', pad=15, fontweight='bold')
plt.tight_layout()
plt.savefig('churn_by_tech_support.png', dpi=150)
plt.close()

# =========================================================================
# GRAPH 5: SENIOR CITIZEN
# =========================================================================
query5 = """
SELECT SeniorCitizen, ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Churn_Rate
FROM telco_churn GROUP BY SeniorCitizen;
"""
df5 = pd.read_sql(query5, conn)
plt.figure(figsize=(6, 6))
plt.pie(df5['Churn_Rate'], labels=['Usia Produktif', 'Lansia'], autopct='%1.1f%%', startangle=90, colors=['#b3d9ff', '#ff4d4d'], wedgeprops={'edgecolor': 'black', 'linewidth': 1})
plt.title('Perbandingan Risiko Churn\nSenior Citizen vs Usia Produktif', pad=15, fontweight='bold')
plt.tight_layout()
plt.savefig('churn_by_senior_citizen.png', dpi=150)
plt.close()

# =========================================================================
# GRAPH 6: TENURE
# =========================================================================
query6 = "SELECT Churn, AVG(tenure) AS Avg_Tenure FROM telco_churn GROUP BY Churn;"
df6 = pd.read_sql(query6, conn)
plt.figure(figsize=(6, 5))
bars = plt.bar(df6['Churn'], df6['Avg_Tenure'], color=colors_binary, width=0.4, edgecolor='black')
plt.title('Rata-Rata Masa Berlangganan (Tenure)', pad=15, fontweight='bold')
plt.ylim(0, 45)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{round(yval, 1)} Bln', va='bottom', ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('churn_by_tenure.png', dpi=150)
plt.close()

conn.close()
print("🚀 Sukses! 6 file grafik .png baru telah dibuat.")
