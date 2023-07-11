import requests, time
from config import cookie,universeid,badgedescription,badgename
err = False
def loop(universe):
    while True:
            print(f"Creating badges for GameID {universe}")
            with requests.session() as session:
                quota = session.get(f"https://badges.roblox.com/v1/universes/{universe}/free-badges-quota").text
                print(quota)
                if int(quota) == 0:
                    print("No more free badges to create.")
                    return
                if int(quota) > 0:
                    session.cookies.set(".ROBLOSECURITY", cookie)
                    header = session.post("https://auth.roblox.com")
                    token = session.headers["X-CSRF-TOKEN"] = header.headers["X-CSRF-TOKEN"]
                    for i in range(int(quota)):
                        badgedata = {"name": badgename, "description": badgedescription, "paymentSourceType": 1, "expectedCost": 0}
                        postreq = session.post(f"https://badges.roblox.com/v1/universes/{universe}/badges", data=badgedata, headers={"x-csrf-token": token}, files={"upload_file":open("icon.png", "rb")})
                        try:
                            print(postreq.json()['id'])
                        except KeyError or IndexError:
                            if postreq.json()['errors'][0]['code'] == 12:
                                print("You cannot create badges for this universe. Please change your config.py (make sure it's universeId)")
                                return
                            print(f"{postreq.json()['errors'][0]['id']}, retrying")
                            loop(universe)
                            return
                        time.sleep(1)
                    print(session.get(f"https://badges.roblox.com/v1/universes/{universe}/free-badges-quota").text + " badges left, returned status code " + str(postreq.status_code) + ", if this is not 200 refer to README.md")
                else:
                    print("Something went wrong? (retrying in 10 min)") 
for item in universeid:
    loop(item)
time.sleep(1000)
