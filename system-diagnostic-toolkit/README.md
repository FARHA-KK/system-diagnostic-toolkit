#  System Diagnostic Toolkit

A Python-based command-line application that displays detailed information about the current computer system. This project is built using Python modules and follows a modular structure for better readability and maintainability.

---

##  Features

###  System Information
- Computer Name
- Current User
- Operating System
- Architecture (32-bit/64-bit)
- Python Version
- Machine Type

###  CPU Information
- CPU Name
- Number of Physical Cores
- Number of Logical Cores
- CPU Usage (%)

###  Memory Information
- Total RAM
- Used RAM
- Available RAM
- RAM Usage (%)

###  Disk Information
- Total Storage
- Used Storage
- Free Storage
- Disk Usage (%)

### 🌐 Network Information
- Hostname
- Local IP Address

---

## 📂 Project Structure

```
System-Diagnostic-Toolkit/
│
├── main.py
├── system_info.py
├── cpu_info.py
├── memory_info.py
├── disk_info.py
├── network_info.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Technologies Used

- Python 3
- psutil
- platform
- socket
- getpass
- os
- datetime

---

## 📦 Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project folder:

```bash
cd System-Diagnostic-Toolkit
```

Install the required package:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📋 Menu

```
1. System Information
2. CPU Information
3. Memory Information
4. Disk Information
5. Network Information
6. View Complete Report
7. Exit
```

---

##  Future Improvements

- Export report to a text file
- Export report as PDF
- GUI version using CustomTkinter
- Live CPU and Memory Monitoring
- Battery Information
- GPU Information
- Network Speed Monitoring

---

## 👨‍💻 Author

**Fathima Farha**

B.Tech Computer Science and Engineering (CSE) Student with an interest in Python programming, Cybersecurity, and Software Development. Passionate about building practical projects and continuously learning new technologies.

