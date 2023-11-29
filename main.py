import requests, time
from config import cookie,universeid,badgedescription,badgename,valuable,limit
err = False
def loop(universe):
    while True:
            print(f"Creating badges for GameID {universe}")
            with requests.sessions.Session() as session:
                quota = session.get(f"https://badges.roblox.com/v1/universes/{universe}/free-badges-quota").text
                print(quota)
                if int(quota) == 0 and not valuable:
                    print("No more free badges to create.")
                    return
                elif int(quota) == 0 and valuable:
                    session.cookies.set(".ROBLOSECURITY", cookie)
                    header = session.post("https://auth.roblox.com")
                    token = session.headers["X-CSRF-TOKEN"] = header.headers["X-CSRF-TOKEN"]
                    for i in range(int(limit)):
                        badgedata = {"name": badgename, "description": badgedescription, "paymentSourceType": 1, "expectedCost": 100} # disclaimer: i am not liable for any lost robux. by using this program you agree not to bug me about it
                        postreq = session.post(f"https://badges.roblox.com/v1/universes/{universe}/badges", data=badgedata, headers={"x-csrf-token": token}, files={"upload_file":open("icon.png", "rb")})
                        try:
                            print(postreq.json())
                        except KeyError or IndexError:
                            if postreq.json()['errors'][0]['code'] == 12:
                                print("You cannot create badges for this universe. Please change your config.py (make sure it's universeId)")
                                return
                            print(f"{postreq.json()['errors'][0]['id']}, retrying")
                            loop(universe)
                            return
                        time.sleep(5)
                    print('Successfully added valuables')
                    break
                if int(quota) > 0:
                    session.cookies.set(".ROBLOSECURITY", cookie)
                    header = session.post("https://auth.roblox.com")
                    token = session.headers["X-CSRF-TOKEN"] = header.headers["X-CSRF-TOKEN"]
                    for i in range(int(quota)):
                        badgedata = {"name": badgename, "description": badgedescription, "paymentSourceType": 1, "expectedCost": 0}
                        postreq = session.post(f"https://badges.roblox.com/v1/universes/{universe}/badges", data=badgedata, headers={"x-csrf-token": token}, files={"upload_file":open("icon.png", "rb")})
                        try:
                            print(postreq.json())
                        except KeyError or IndexError:
                            if postreq.json()['errors'][0]['code'] == 12:
                                print("You cannot create badges for this universe. Please change your config.py (make sure it's universeId)")
                                return
                            print(f"{postreq.json()['errors'][0]['id']}, retrying")
                            loop(universe)
                            return
                        time.sleep(5)
                    print(session.get(f"https://badges.roblox.com/v1/universes/{universe}/free-badges-quota").text + " badges left, returned status code " + str(postreq.status_code) + ", if this is not 200 refer to README.md")
                else:
                    print("Something went wrong? (retrying in 10 min)") 
for item in universeid:
    loop(item)
time.sleep(1000)
