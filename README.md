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
  
## Sample Output

Found 3 users with details in demoCorp-inc:
- Username: shruti25ratnam, ID: 7614310, Company: Microsoft, Email: None
- Username: sr-demo, ID: 209555675, Company: None, Email: None
- Username: ss-demo47, ID: 209556177, Company: None, Email: None

Found 2 users NOT belonging to demoCorp-inc:
- [!] Username: sr-demo, Company: None
- [!] Username: ss-demo47, Company: None

---

## Requirements

- Python 3.7+
- `requests` library

Install dependencies:
pip install requests
