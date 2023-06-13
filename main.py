import requests, time
from config import cookie,universeid,badgedescription,badgename
while True:
    for item in universeid:
        print(f"Creating badges for GameID {item}")
        with requests.session() as session:
            quota = session.get(f"https://badges.roblox.com/v1/universes/{item}/free-badges-quota").text
            if int(quota) == 0:
                print("No more free badges to create.")
            if int(quota) > 0:
                session.cookies.set(".ROBLOSECURITY", cookie)
                header = session.post("https://auth.roblox.com")
                token = session.headers["X-CSRF-TOKEN"] = header.headers["X-CSRF-TOKEN"]
                for i in range(int(quota)):
                    badgedata = {"name": badgename, "description": badgedescription, "paymentSourceType": 1, "expectedCost": 0}
                    postreq = session.post(f"https://badges.roblox.com/v1/universes/{item}/badges", data=badgedata, headers={"x-csrf-token": token}, files={"upload_file":open("icon.png", "rb")})
                    print(postreq.json()['id'])
                    time.sleep(2)
                print(session.get(f"https://badges.roblox.com/v1/universes/{item}/free-badges-quota").text + " badges left, returned status code " + str(postreq.status_code) + ", if this is not 200 refer to README.md")
            else:
                print("Something went wrong? (retrying in 10 min)") 
    time.sleep(1000)
    
