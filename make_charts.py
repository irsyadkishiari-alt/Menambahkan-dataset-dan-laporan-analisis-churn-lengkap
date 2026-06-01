import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# 1. Hubungkan ke database MariaDB lokal Anda

conn = mysql.connector.connect(
    host="127.0.0.1",        # Mengganti localhost dengan IP loopback lokal
    port=3306,               # Memastikan port standar MySQL/MariaDB terbuka
    user="root",        
    password="",        
    database="telco_projects"
)

# 2. Query untuk mengambil data Churn berdasarkan Jenis Kontrak
query = """
SELECT 
    Contract,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Churn_Rate
FROM telco_churn
GROUP BY Contract
ORDER BY Churn_Rate DESC;
"""

# 3. Masukkan data hasil query ke dalam Pandas DataFrame
df = pd.read_sql(query, conn)
conn.close()

# 4. Mulai membuat grafik menggunakan Matplotlib
plt.figure(figsize=(8, 5))
colors = ['#ff4d4d', '#ffb3b3', '#c2c2d6'] # Warna merah mencolok untuk churn tertinggi

# Membuat grafik batang
bars = plt.bar(df['Contract'], df['Churn_Rate'], color=colors, edgecolor='black')

# Menambahkan judul dan label informasi
plt.title('Tingkat Churn Pelanggan Berdasarkan Jenis Kontrak (%)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Jenis Kontrak', fontsize=12)
plt.ylabel('Churn Rate (%)', fontsize=12)
plt.ylim(0, 50) # Mengatur batas atas grafik ke 50%

# Menambahkan label angka di atas setiap batang grafik
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval}%", ha='center', va='bottom', fontweight='bold')

# Menyimpan grafik sebagai file gambar PNG
plt.tight_layout()
plt.savefig('churn_by_contract.png', dpi=300)
print("✅ Grafik berhasil dibuat dan disimpan dengan nama 'churn_by_contract.png'!")
