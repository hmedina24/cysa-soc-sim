#Main game loop and level logic 

import random 

class SOCEngine: 
    def __init__(self):
        # CySA+ Domain Weights (CS0-003)
        self.domains = {
                "Security Operations": 0.33,
                "Vulnerability Management": 0.30,
                "Incident Response": 0.20,
                "Reporting & Communication": 0.17
        }
        self.user_xp = 0
        self.current_level = 1

    def get_next_mission(self):
        # Choose a domain based on the exam's actual weight 
        selected_domain = random.choices(
                list(self.domains.keys()),
                weights=list(self.domains.values())
            )[0]

        return selected_domain 


