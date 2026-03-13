# Hamkor Bank System

**Hamkor Bank System** – bu zamonaviy bank platformasi bo‘lib, foydalanuvchilarga o‘z hisoblarini boshqarish, kartalari bilan ishlash,
turli to‘lovlarni amalga oshirish va QR kod orqali tezkor to‘lov qilish imkonini beradi.

---

## 📌 Xususiyatlar

- **Foydalanuvchi autentifikatsiyasi**: Ro‘yxatdan o‘tish, Login, Logout, Parolni tiklash (Reset Password)  
- **Hisob va kartalarni boshqarish**  
- **Pul o‘tkazmalar (Transfers) va tranzaksiyalarni ko‘rish**  
- **QR kod orqali to‘lovlar (Payments)**  
- **Mobile communication, Internet va Communal to‘lovlar**  
- **REST API orqali barcha funksiyalarni boshqarish**

---

## 🛠 Texnologiyalar

- Backend: Django + Django REST Framework  
- Database: PostgreSQL  
- Autentifikatsiya: DRF Token  
- Deploy: Railway 
---

## ⚡ O‘rnatish va Ishga Tushirish

1. Loyihani klonlash:

   git clone https://github.com/yasminatolibova/teamwork.git
   cd hamkor-bank-system

Virtual muhit yaratish va aktivlashtirish:

python -m venv venv

Kerakli paketlarni o‘rnatish:

pip install -r requirements.txt

.env faylini yaratish va konfiguratsiya qilish:

DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://user:password@localhost:5432/teamwork

Migratsiyalarni qo‘llash:

python manage.py migrate

Serverni ishga tushirish:

python manage.py runserver

Brauzer orqali kirish:

http://127.0.0.1:8000/
🚀 API Endpointlar

/api/accounts/accounts/ – foydalanuvchilarni boshqarish (CRUD)

/api/accounts/login/ – login

/api/accounts/logout/ – logout

/api/accounts/reset_password/ – parolni tiklash

/api/cards/card/ – foydalanuvchi kartalari

/api/transfers/transactions – tranzaksiyalar

/api/transfers/transfer – pul o‘tkazmalar

/api/qrcode/qrcode_createlist – QR kod orqali to‘lovlar

/api/payments/mobilepayment/ – mobil to‘lovlar

/api/payments/internetpayment/ – internet to‘lovlar

/api/payments/communalpayment/ – communal to‘lovlar

API Documentation

<img width="1866" height="941" alt="Screenshot 2026-03-11 152000" src="https://github.com/user-attachments/assets/2fe384e9-6023-44e8-822b-ca7dbf4e8869" />


🧩 Loyiha Struktura
hamkor_bank_system/

├── accounts/       # Foydalanuvchi modeli va autentifikatsiya

├── cards/          # Kartalar bilan ishlash

├── transactions/   # Tranzaksiyalar va transfers

├── payments/       # Mobile, Internet, Communal paymentlar

├── qrcode         # QR Code bilan to'lov qilish uchun

├── manage.py

├── requirements.txt

└── README.md

👩‍💻 Author

Yasmina Tolibova
