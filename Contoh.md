# 📞 Customer Churn Analysis: Menurunkan Angka Churn pada Sektor Telekomunikasi

## 📌 Project Overview
Proyek ini bertujuan untuk menganalisis perilaku pelanggan dan mengidentifikasi faktor risiko utama yang menyebabkan pelanggan berhenti berlangganan (*churn*) pada perusahaan telekomunikasi. Dengan menggunakan pendekatan Data-Driven, analisis ini memberikan rekomendasi strategis bagi tim manajemen, produk, dan CRM untuk meningkatkan retensi pelanggan (*customer retention*).

**Business Impact:** Mempertahankan pelanggan lama jauh lebih efisien secara biaya daripada mengakuisisi pelanggan baru. Analisis ini berfokus pada pencarian akar masalah mengapa 1.869 pelanggan memutuskan untuk *churn*.

---

## 🛠️ Tech Stack & Environment
* **Database Management System:** MariaDB / MySQL
* **Environment:** Linux CLI via Termux (PRoot Ubuntu Environment)
* **Dataset:** Telco Customer Churn (7,043 baris data riil)

---

## 🧠 Data Cleaning & Preprocessing
Sebelum analisis dilakukan, ditemukan isu *formatting* di mana terdapat karakter *carriage return* (`\r`) tersembunyi pada data mentah akibat perbedaan ekosistem OS (Windows ke Linux). Hal ini sempat menyebabkan kegagalan deteksi query logika `=` pada string target karena panjang karakter menjadi tidak sesuai.

Proses pembersihan dilakukan langsung di database menggunakan perintah berikut:

```sql
-- Menghilangkan karakter tersembunyi \r secara permanen dari kolom Churn
UPDATE telco_churn SET Churn = REPLACE(Churn, '\r', '');

-- Validasi hasil data cleaning
SELECT Churn, COUNT(*) FROM telco_churn GROUP BY Churn;
