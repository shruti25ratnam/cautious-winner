import os

def read_token(filename="token.txt"):
    script_dir = r"<your token location>"
    print(script_dir)
    file_path = os.path.join(script_dir, filename)
    with open(file_path, "r") as f:
        token = f.read().strip()
        #print(f"Loaded token: {token}") 
        return token
    
def load_access_token():
        TOKEN = read_token()
        print(f"Loaded token: {TOKEN}")
        headers = {
            "Authorization": f"token {TOKEN}",
            "Accept": "application/vnd.github+json"
        }
        return headers

load_access_token()