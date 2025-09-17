import re
log_text = """
User1 logged in from 192.168.1.10 at 10:45AM
User2 failed login from 10.0.0.5 at 11:15AM
User3 connected from 172.16.0.22 at 01:00PM
"""
pattern = r'\b\d{1,3}(?:\.\d{1,3}){3}\b'
ips = re.findall(pattern, log_text)
print("Extracted IPs:", ips)