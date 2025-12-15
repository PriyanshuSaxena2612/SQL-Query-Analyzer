# SQL Query Complexity Analyzer

A lightweight Python utility that performs **static, heuristic-based analysis**
of SQL queries to estimate complexity and highlight potential performance risks.

The goal is **not** to validate SQL syntax or execution plans, but to provide
**explainable signals** that help identify queries likely to be expensive or
hard to maintain in analytical workloads.

---

## 🚀 Features

- Extracts structural query features such as:
  - JOIN count
  - CTE depth
  - SELECT * usage
  - Missing filters
  - Window functions
- Computes a **heuristic complexity score** (0–100)
- Identifies **key cost drivers**
- Generates **actionable optimization recommendations**
- Supports **Snowflake-aware heuristics** (e.g., QUALIFY with window functions)
- Configurable scoring logic via external configuration

---

## 🧠 Design Philosophy

This project intentionally uses **lightweight string and pattern-based analysis**
instead of full SQL parsing or query execution.

The objective is to:
- Keep the logic **fast and explainable**
- Focus on **relative risk scoring**, not perfect correctness
- Reflect how internal tooling often flags SQL risks in analytics teams

---

## 🛠 Tech Stack

- Python
