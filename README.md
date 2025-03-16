# 🍽️ Python-Based Restaurant Management System

## 📌 Introduction
The **Restaurant Management System** is a Python-based application designed to streamline the process of ordering food through multiple modes: **Dine-in, Self-Pickup, and Home Delivery**. It includes user authentication, transaction history, and automated charge calculations.

---

## 🚀 Features
- **User Authentication**: Sign-up and login system with validation for **mobile number, password, and date of birth**.
- **Ordering Modes**:
  - **Dine-in**: Separate menu, table booking, and a **15% service charge**.
  - **Self-Pickup**: No additional charges.
  - **Home Delivery**: Charges calculated based on distance from the restaurant.
- **Transaction Summary**: View past orders categorized by mode and sorted by amount spent.

---

## 🛠️ Functionalities

### 🔐 User Authentication
- **Mobile number** must start with **0** and have **10 digits**.
- **Password Requirements**:
  - Must start with an **alphabet**.
  - Must contain at least **one special character**.
  - Must end with a **digit**.
- **Date of Birth (DOB) validation** ensures the user is at least **21 years old**.

---

### 🛒 Ordering System

#### **Dine-in Mode**
- Displays **6 food items** + **3 drinks**.
- Asks for **number of people, booking date & time**.
- Applies **15% service charge**.
- Options:
  - ✅ **Proceed with Payment**
  - ❌ **Cancel Order**

#### **Self-Pickup Mode**
- Displays a menu with **6 items**.
- No additional charges.
- Options:
  - ✅ **Proceed with Payment**
  - ❌ **Cancel Order**

#### **Home Delivery Mode**
- Displays a menu with **6 items**.
- Asks for **delivery address & distance**.
- **Delivery charge** calculated based on distance.
- Options:
  - ✅ **Proceed with Payment**
  - ❌ **Cancel Order**

---

## 📊 Transaction Summary
Users can view:
1. 📌 **Dine-in Orders History**
2. 📌 **Self-Pickup Orders History**
3. 📌 **Delivery Orders History**
4. 📌 **All Orders Sorted by Amount**
5. 📌 **Total Amount Spent**

---

## 🏗️ Technologies Used
- **Python** (Core Logic & Authentication)
- **Regex** (Validation)
- **File Handling/Database** (Transaction Storage)

---

## 📜 Conclusion
This system offers a seamless way to manage restaurant orders across different modes while ensuring user authentication and transaction tracking.
