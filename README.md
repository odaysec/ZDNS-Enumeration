# 🔍 ZDNS Enumeration Automation Tool  
ZDNS Enumeration Automation Tool adalah alat otomatisasi berbasis Python untuk enumerasi subdomain menggunakan **ZDNS**. Alat ini membantu dalam pemetaan DNS dengan cepat, mendukung berbagai jenis query (A, CNAME, MX, NS, dll.), dan menyimpan hasil dalam format JSON atau CSV.

## 🚀 Fitur  
✅ **Otomatisasi ZDNS** – Menjalankan ZDNS secara otomatis dengan daftar subdomain.  
✅ **Dukungan Berbagai Query** – A, CNAME, MX, NS, TXT, dan lainnya.  
✅ **Parsing Output JSON** – Memformat hasil agar lebih mudah dianalisis.  
✅ **Error Handling** – Menangani kesalahan jika file tidak ditemukan atau eksekusi gagal.  

---

## 📥 Instalasi  
### 1️⃣ **Install ZDNS**  
Pastikan **ZDNS** telah diinstal:  
```sh
sudo apt update && sudo apt install -y golang
go install github.com/zmap/zdns/v3@latest
export PATH=$PATH:$(go env GOPATH)/bin
```
### 2️⃣ Clone Repository
```
git clone https://github.com/odaysec/ZDNS-Enumeration.git
cd ZDNS-Enumeration
pip install -r requirements.txt
```
## 🎯 Penggunaan
Jalankan alat ini dengan perintah berikut:
```
python zdns_enum.py -d example.com -w subdomains.txt -o result.json
```
**📌 Penjelasan Parameter:**
- `-d` `example.com` → Domain target
- `-w` `subdomains.txt` → File berisi daftar subdomain
- `-o` `result.json` → File output dalam format JSON
- `-t` `A` → (Opsional) Jenis query DNS (default: A, bisa diubah ke CNAME, MX, NS, dll.)

### 📌 Contoh Output:
```
[INFO] Menjalankan ZDNS pada example.com dengan 100 subdomain...
[SUCCESS] Hasil tersimpan di result.json
```
## 🛠 Cara Kerja
- 1️⃣ Membaca daftar subdomain dari file.
- 2️⃣ Menjalankan ZDNS untuk melakukan query DNS pada setiap subdomain.
- 3️⃣ Menyimpan hasil dalam format JSON untuk analisis lebih lanjut.
- 4️⃣ Menampilkan output yang relevan di terminal.



