
# Parking Lot Management System (FCFS Scheduling)

This project simulates a parking lot system using the **First Come First Serve (FCFS)** scheduling algorithm in Python. It includes vehicle queuing, dynamic parking allocation, time-based billing, and performance statistics like waiting and turnaround times.

---

## Features

- Dynamic parking slot allocation
- Queue management using FCFS
- Billing based on parking duration
- Waiting time and turnaround time tracking
- Gantt chart visualization
- Summary statistics and reports

---

## How It Works

- Vehicles are parked based on arrival time.
- If all slots are occupied, vehicles wait in a queue.
- As a slot becomes free, the next vehicle in the queue is parked.
- Bills are calculated based on parking duration (default Rs 10/hour).
- Average waiting and turnaround time is calculated.
- Gantt chart visually shows waiting and parking time per vehicle.

---

## File Structure

```
parking-lot-fcfs/
│
├── parking_lot_fcfs.py       # Main source code
├── README.md                 # Project documentation
├── screenshots/              # Input/output screenshots
└── OS_Lab_Project_Documentation.docx  # Final documentation
```

---

## 📸 Sample Output

![Gantt Chart Screenshot](![image](https://github.com/user-attachments/assets/8da13676-c01d-4459-8f6f-7f1add268e1c)
)

---

## 📊 Sample Table Output

| Vehicle | Arrival | Departure | Waiting | Turnaround |
|---------|---------|-----------|---------|------------|
| KA01AA1 |    1    |     5     |    0    |     4      |
| MH02BB2 |    2    |     8     |    1    |     6      |

---

## Requirements

- Python 3.x
- `matplotlib`
- `tabulate`

Install required libraries using:

```bash
pip install matplotlib tabulate
```

---

## Run the Program

```bash
python parking_lot_fcfs.py
```

Follow the menu-driven interface to park/remove vehicles, display status, and view charts.

---

## Contact

Created by **Faiza Mushtaq Ahmad**  
For academic OS Lab submission  
[faizamushtaqahmad@gmail.com]

---
