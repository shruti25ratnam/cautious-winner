# cautious-winner
Audit and validate GitHub organization members by company affiliation.

**Cautious Winner** is a Python tool designed to audit and validate GitHub organization users by analyzing public profile details like company affiliation and email.

## Features

- Fetch all members of a GitHub organization.
- Retrieve public profile attributes:
  - Username
  - GitHub ID
  - Company
  - Public Email
- Flag users whose company does not match the expected organization (e.g., "Microsoft").
- Easily configurable for any organization and expected company name.

---

## Requirements

- Python 3.7+
- `requests` library

Install dependencies:
pip install requests
