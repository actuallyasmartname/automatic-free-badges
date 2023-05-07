import requests, time
from config import cookie, badgename, badgedescription, universeid
def badges():
    with requests.session() as session:
        quota = session.get(f"https://badges.roblox.com/v1/universes/{universeid}/free-badges-quota").text
        if int(quota) == 0:
            return print("No more free badges to create.")
        if int(quota) > 0:
            session.cookies.set(".ROBLOSECURITY", cookie)
            header = session.post("https://auth.roblox.com")
            token = session.headers["X-CSRF-TOKEN"] = header.headers["X-CSRF-TOKEN"]
            for i in range(int(quota)):
                badgedata = {"name": badgename, "description": badgedescription, "paymentSourceType": 1, "expectedCost": 0}
                postreq = session.post(f"https://badges.roblox.com/v1/universes/{universeid}/badges", data=badgedata, headers={"x-csrf-token": token}, files={"upload_file":open("download.png", "rb")})
            return print(session.get(f"https://badges.roblox.com/v1/universes/{universeid}/free-badges-quota").text + " badges left, returned status code " + str(postreq.status_code) + ", if this is not 200 refer to README.md")
        else:
            return print("Something went wrong?") 
while True:
    badges()
    time.sleep(120)


    
