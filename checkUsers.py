import requests
from pathlib import Path
from access_token.token_reader import load_access_token

class ValidateUsers:

    def __init__(self):
        self.headers = load_access_token()

    def get_all_git_users_by_company(self, org_name):
        members = []
        page = 1
        while True:
            url = f"https://api.github.com/orgs/{org_name}/members?per_page=100&page={page}"
            response = requests.get(url, headers=self.headers)
            if response.status_code != 200:
                raise Exception(f"Failed to fetch members: {response.json()}")
            page_members = response.json()
            if not page_members:
                break
            members.extend(page_members)
            page += 1

        # Now fetch additional user details like email and company
        detailed_members = []
        for member in members:
            username = member["login"]
            user_details = self.get_user_details(username)
            detailed_members.append(user_details)
        
        return detailed_members

    def get_user_details(self, username):
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            print(f"Failed to fetch details for user {username}")
            return {"login": username, "id": None, "email": None, "company": None}
        user_info = response.json()
        return {
            "login": user_info["login"],
            "id": user_info["id"],
            "email": user_info.get("email"),
            "company": user_info.get("company")
        }

    def manual_validator(self, org_name):
        members = self.get_all_git_users_by_company(org_name)

        print(f"\nFound {len(members)} users with details in {org_name}:")
        for member in members:
            print(f"Username: {member['login']}, ID: {member['id']}, Company: {member['company']}, Email: {member['email']}")

    def flag_users_by_company_name(self, org_name, expected_company="Microsoft"):
        members = self.get_all_git_users_by_company(org_name)
        flagged_users = []

        for member in members:
            company = member.get('company') or ""
            normalized_company = company.lower().replace(" ", "")
            if expected_company.lower().replace(" ", "") not in normalized_company:
                flagged_users.append(member)

        if flagged_users:
            print(f"\n[!] Found {len(flagged_users)} users NOT belonging to {expected_company}:")
            for user in flagged_users:
                print(f"[!] Username: {user['login']}, Company: {user['company']}")
        else:
            print(f"\n All users belong to {expected_company}.")

if __name__ == "__main__":
    org_name = "demoCorp-inc"
    validator = ValidateUsers()
    validator.manual_validator(org_name)
    validator.flag_users_by_company_name(org_name)
