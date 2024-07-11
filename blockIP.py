import random

def generate_random_ip():
 return f"192.168.1.{random.randint(0, 20)}"

def check_firewall_rules(ip, rules):
    for rule_ip,action in rules.items():
        if ip == rule_ip:
            return action
    return "ALLOW"
    
def main():
    firewall_rules={"192.168.1.1" : "BLOCK",
                    "192.168.1.4" : "BLOCK",
                    "192.168.1.6" : "BLOCK",
                    "192.168.1.8" : "BLOCK",
                    "192.168.1.17": "BLOCK",
                    "192.168.1.19": "BLOCK"
                    }
    
    for _ in range(20):
     ip_adress = generate_random_ip()
     action=check_firewall_rules(ip_adress, firewall_rules)
    #random_number=random.randint(0, 200)
     # print(f"IP: {ip_adress}, Action : {action},Random: {random_number}")
     
     print(f"IP: {ip_adress}, Action : {action} ")
        
        
        
if __name__ == "__main__":
    main()