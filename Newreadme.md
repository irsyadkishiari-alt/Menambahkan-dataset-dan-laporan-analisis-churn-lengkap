# 📞 Telco Customer Churn Analysis & Customer Retention Strategy

## 📌 Project Overview

Customer retention merupakan salah satu faktor paling penting dalam industri telekomunikasi. Mempertahankan pelanggan yang sudah ada umumnya membutuhkan biaya yang jauh lebih rendah dibandingkan memperoleh pelanggan baru.

Proyek ini bertujuan untuk mengidentifikasi faktor-faktor utama yang menyebabkan pelanggan berhenti berlangganan (customer churn), memvalidasi temuan menggunakan analisis statistik, serta menyusun strategi retensi yang dapat memberikan dampak bisnis nyata.

**Objectives**

- Mengidentifikasi faktor utama penyebab churn.
- Membuktikan hubungan antar variabel menggunakan uji statistik inferensial.
- Mengukur potensi kerugian finansial akibat churn.
- Memberikan rekomendasi strategi retensi berbasis data.

**Business Impact**

Analisis menunjukkan bahwa implementasi strategi retensi yang tepat berpotensi menyelamatkan lebih dari **$500.000 pendapatan tahunan** melalui pengurangan churn pada segmen pelanggan berisiko tinggi.

---

## 🎯 Business Problem

Perusahaan telekomunikasi mengalami kehilangan pelanggan secara berkelanjutan, namun belum mengetahui:

- Segmen pelanggan yang paling rentan melakukan churn.
- Faktor utama yang memengaruhi keputusan pelanggan untuk berhenti berlangganan.
- Dampak finansial yang ditimbulkan oleh churn.
- Strategi retensi yang paling efektif untuk diterapkan.

---

## 📂 Dataset Information

**Dataset:** Telco Customer Churn

**Total Records:** 7.043 pelanggan

Dataset berisi informasi mengenai:

- Demografi pelanggan
- Jenis layanan yang digunakan
- Metode pembayaran
- Durasi kontrak
- Biaya bulanan
- Masa berlangganan (tenure)
- Status churn

---

## 🛠️ Tech Stack

| Category | Tools |
| :-- | :-- |
| Database  | MariaDB / MySQL |
Programming Language| Python 3
Environment| Linux CLI (Termux + PRoot Ubuntu)
Data Processing| Pandas, NumPy
Visualization| Matplotlib, Seaborn
Database Connector| mysql-connector-python

---

## 🧼 Data Cleaning & Preprocessing

Sebelum analisis dilakukan, ditemukan masalah kualitas data berupa karakter tersembunyi ***("\r")*** pada kolom target ***"Churn"***.

Masalah ini menyebabkan query filtering dan grouping menghasilkan output yang tidak konsisten.

**Data Cleaning Query**

``` UPDATE telco_churn
SET Churn = REPLACE(Churn, '\r', '');
```
**Validation Query**
```
SELECT Churn, COUNT(*)
FROM telco_churn
GROUP BY Churn;
```
**Validation Result**

|Churn Status| Total Customers|
| :-- | :-- |
No| 5174
Yes| 1869

Dataset kemudian dinyatakan siap untuk dianalisis.

---
## 📊 Exploratory Data Analysis (EDA)
### 1️⃣ Customer Churn by Contract Type
**SQL Query**
```
SELECT 
    Contract,
    COUNT(*) AS Total_Pelanggan,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Total_Churn,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Churn_Rate_Persen
FROM telco_churn
GROUP BY Contract
ORDER BY Churn_Rate_Persen DESC;
```
**Result**
|Contract|Total Pelanggan|Total Churn|Churn Rate (%)|
| :-- | :-- | :-- | :-- |
|Month-to-month|3875|1655|42.71|
|One year|1473|166|11.27|
|Two year|1695|48|2.83%

**Visualisasi Grafik:**
![Grafik Churn berdasarkan Jenis Kontrak](churn_by_contract.png)
**Key Insight**

Pelanggan dengan kontrak bulanan memiliki tingkat churn hampir 15 kali lebih tinggi dibandingkan pelanggan kontrak dua tahun.
Hal ini menunjukkan bahwa komitmen kontrak merupakan salah satu faktor terkuat yang memengaruhi retensi pelanggan.

### 2️⃣ Monthly Charges Analysis
**SQL Query**
```
SELECT 
    Churn,
    ROUND(AVG(MonthlyCharges), 2) AS Rata_Rata_Biaya_Bulanan
FROM telco_churn
GROUP BY Churn;
```
**Result**
|Churn Status|Average Rata-rata Biaya Bulanan|
| :-- | :-- |
|No|61.27|
|Yes|74.44|

**Visualisasi Grafik:**
![Grafik Churn berdasarkan Biaya Bulanan](churn_by_monthly_charges.png)
**Key Insight**

Pelanggan yang churn membayar rata-rata biaya bulanan yang lebih tinggi dibandingkan pelanggan yang bertahan.
Perbedaan ini menunjukkan adanya sensitivitas harga pada kelompok pelanggan tertentu.

### 3️⃣ Internet Service Analysis
**SQL Query**
```
SELECT 
    InternetService,
    COUNT(*) AS Total_Pelanggan,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Total_Churn,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Churn_Rate_Persen
FROM telco_churn
GROUP BY InternetService
ORDER BY Churn_Rate_Persen DESC;
```
**Result**
|Internet Service|Total Pelanggan|Total Churn|Churn Rate (%)|
| :-- | :-- | :-- | :-- |
|Fiber Optic|3096|1297|41.89%|
|DSL|2421|459|18.96%
|No |1526|113|7.40%

**Visualisasi Grafik:**
![Grafik Churn berdasarkan Layanan Internet](churn_by_internet_service.png)
**Key Insight**

Layanan Fiber Optic memiliki tingkat churn tertinggi meskipun merupakan layanan premium.
Temuan ini mengindikasikan kemungkinan adanya masalah pada:
Kualitas layanan
Harga produk
Ekspektasi pelanggan yang tidak terpenuhi

### 4️⃣ Technical Support Analysis
**SQL Query**
```
SELECT 
    TechSupport,
    COUNT(*) AS Total_Pelanggan,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Total_Churn,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Churn_Rate_Persen
FROM telco_churn
GROUP BY TechSupport
ORDER BY Churn_Rate_Persen DESC;
```
**Result**
|Tech Support|Total Pelanggan|Total Churn|Churn Rate
| :-- | :-- | :-- | :-- |
|No|3473|1446|41.64%
|Yes|2044|310|15.17%
|No Internet Service|1526|113|7.40%

**Visualisasi Grafik:**

**Key Insight**

Pelanggan tanpa Technical Support memiliki risiko churn hampir tiga kali lebih tinggi dibandingkan pelanggan yang mendapatkan dukungan teknis.

### 5️⃣ Senior Citizen Analysis
**SQL Query**
```
SELECT 
    CASE WHEN SeniorCitizen = 1 THEN 'Lansia (Senior)' ELSE 'Usia Produktif' END AS Kategori_Umur,
    COUNT(*) AS Total_Pelanggan,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Total_Churn,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Churn_Rate_Persen
FROM telco_churn
GROUP BY SeniorCitizen;
```
**Result**
|Kategori Usia|Total Pelanggan|Total Churn|Churn Rate(%)
| :-- | :-- | :-- | :--
|Usia Produktif|5901|1393|23.61%
|Lansia(Senior)|1142|476|41.68%

**Visualisasi Grafik:**
![Grafik Churn berdasarkan Kategori Usia](churn_by_senior_citizen.png)
**Key Insight**

Kelompok Senior Citizen memiliki tingkat churn yang jauh lebih tinggi dibandingkan pelanggan usia produktif.

### 6️⃣ Tenure Analysis
**SQL Query**
```
SELECT 
    Churn,
    ROUND(AVG(tenure), 1) AS Rata_Rata_Bulan_Berlangganan
FROM telco_churn
GROUP BY Churn;
```
**Result**
|Churn Status|Rata-rata Bulanan Berlanggana
| :-- | :--
|No|37.6 Bulan
|Yes|18 Bulan

**Visualisasi Grafik:**
![Grafik Churn berdasarkan Rata-rata Bulan Berlangganan](churn_by_tenure.png)
**Key Insight**

Mayoritas pelanggan yang churn meninggalkan layanan pada sekitar bulan ke-18.
Periode 0–18 bulan dapat dikategorikan sebagai Customer Danger Zone.



---

🔬 Statistical Validation

Untuk memastikan pola yang ditemukan bukan sekadar kebetulan, dilakukan pengujian statistik inferensial.

Chi-Square Test

Variables Tested

- Contract vs Churn
- Internet Service vs Churn

Results

Variable| Statistical Result
Contract| p-value < 0.001
Internet Service| p-value < 0.05

Interpretation

Hasil menunjukkan bahwa jenis kontrak dan jenis layanan internet memiliki hubungan yang signifikan terhadap churn.

---

Independent Samples T-Test

Variable Tested

Monthly Charges vs Churn

Results

Group| Average Monthly Charges
Churn Customers| 74.44
Retained Customers| 61.27

Difference:

74.44 - 61.27 = 13.17

Statistical Result:

p-value < 0.05

Interpretation

Perbedaan biaya bulanan antara pelanggan yang churn dan pelanggan yang bertahan terbukti signifikan secara statistik.

---

🚨 High-Risk Customer Profile

Berdasarkan seluruh hasil analisis, pelanggan dengan risiko churn tertinggi memiliki karakteristik berikut:

- Senior Citizen
- Fiber Optic User
- High Monthly Charges
- Month-to-Month Contract
- No Technical Support
- Tenure Below 18 Months

---

💎 Customer Lifetime Value (CLV)

Untuk membantu prioritas retensi pelanggan digunakan pendekatan sederhana:

CLV = Monthly Charges × Tenure

Retention Priority

Priority 1 — Premium Customers at Risk

- Fiber Optic
- Monthly Charges > $80
- Month-to-Month Contract
- Tenure 10–24 Months

Priority 2 — New Customers

- Tenure < 6 Months
- High Monthly Charges
- Month-to-Month Contract

Priority 3 — Stable Customers

- One-Year or Two-Year Contract
- Low Churn Risk

---

📈 Financial Impact Analysis

Current Revenue Loss

Total Churn Customers:

1,869 Customers

Average Monthly Charges:

$74.44

Estimated Monthly Revenue Loss:

1,869 × $74.44 = $139,128.36

---

Retention Strategy Scenario

Assumption:

30% of High-Risk Customers Successfully Retained

Customers Saved:

30% × 1,869 = 560 Customers

Recovered Revenue per Month:

560 × $74.44 = $41,686.40

Recovered Revenue per Year:

$41,686.40 × 12 = $500,236.80

---

🚀 Business Recommendations

1. Contract Migration Program

Memberikan insentif kepada pelanggan kontrak bulanan agar berpindah ke kontrak 1 atau 2 tahun.

---

2. Fiber Optic Service Audit

Melakukan evaluasi menyeluruh terhadap kualitas layanan Fiber Optic untuk mengidentifikasi akar penyebab churn.

---

3. Free Technical Support Initiative

Memberikan akses Technical Support gratis selama periode kritis pelanggan baru.

---

4. Senior-Friendly Customer Experience

Menyediakan layanan bantuan khusus dan materi edukasi yang lebih mudah dipahami bagi pelanggan lansia.

---

5. Early Warning Retention Dashboard

Membangun sistem monitoring yang menandai pelanggan dengan kombinasi:

- Month-to-Month Contract
- Fiber Optic Service
- High Monthly Charges
- Tenure < 18 Months

agar tim CRM dapat melakukan intervensi lebih awal.

---

✅ Conclusion

Analisis menunjukkan bahwa churn pelanggan terutama dipengaruhi oleh kombinasi:

- Kontrak bulanan (Month-to-Month)
- Biaya bulanan tinggi
- Penggunaan layanan Fiber Optic
- Tidak adanya Technical Support
- Masa berlangganan yang masih relatif pendek

Melalui kombinasi SQL, Python, visualisasi data, dan validasi statistik inferensial, proyek ini berhasil mengidentifikasi faktor-faktor utama penyebab churn serta menerjemahkannya menjadi rekomendasi bisnis yang dapat ditindaklanjuti.

Implementasi strategi retensi yang tepat berpotensi menyelamatkan lebih dari $500.000 pendapatan tahunan dan meningkatkan loyalitas pelanggan secara berkelanjutan.
