# Data Engineering Standards

## Purpose

This directory contains approved reference implementations for accessing, querying, and analyzing enterprise data sources.

Kiro should consult these implementations when generating data-related solutions to ensure alignment with the organization's preferred data access patterns, libraries, and security practices.

---

# Approved Technologies

- Teradata (Enterprise Database)
- Hive (Big Data Platform)
- SQLAlchemy (SQL Access)
- JayDeBeAPI (JDBC Access)
- Pandas (Analytics)
- Plotly (Visualization)

---

# Contents

| File | Description |
|------|-------------|
| teradata-query.py | Approved pattern for Teradata database access |
| hive-connection.py | Approved pattern for Hive connectivity |
| pandas-analysis.py | Approved pattern for data analysis with Pandas |

---

# Engineering Principles

- Use approved connection libraries (SQLAlchemy, JayDeBeAPI).
- Authenticate using configuration files or secure secret stores.
- Never hardcode database credentials.
- Use parameterized queries to prevent injection.
- Handle connection failures gracefully.
- Close connections properly after use.
- Log data access operations for audit.
- Limit data retrieval to required scope.

---

# Usage

When generating data access implementations, Kiro should reference these files as the approved implementation standard and adapt them to the specific data engineering requirements.
