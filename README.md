# Python Instructions

Note: For your .ROBLOSECURITY cookie if you use third-party hosting platforms I strongly recommend using an alt with team create!

1. Install the library `requests` (pip install requests or pip3 install requests, and make sure you have python installed!)
2. Open config.py. From here, in `cookie` input your .ROBLOSECURITY cookie (search a tutorial for your browser if you don't know how or use EditThisCookie), in `universeid` input the universeId for the place you will add badges to (get from the creator page URL for the universe page), and `badgename` and `badgedescription` to whatever you want. Oh, and replace `icon.png` with your desired image file. You probably won't like my terrible artwork.
3. Run `main.py`. Make sure you can run this script 24/7.

# Game Instructions

1. Put a BadgeAwarder (I strongly recommend using Manner's as that's what avoids ratelimits, https://www.roblox.com/library/11647317355/Badge-Awarder-Kit) and put it in ReplicatedStorage. You can merge Inkthirsty's [Better Badge Awarder](https://create.roblox.com/marketplace/asset/6647379227/Better-Badge-Giver)'s decal script, just put `repeat task.wait(.1) until script.Parent.Parent.Parent == game.Workspace` into the script called `Decal`.
2. Copy the code from `game.lua` into a script inside ServerScriptService.
3. In lines 40 and 41, replace `pos` and `pos2` with your desired BadgeAwarder spawn coordinates. (Playtest first).
4. You're done!

Note: If your badge awarders are disappearing make sure they aren't called "BadgeAwarder". Change their name.

# Error codes
If you don't get status code 200 everytime, refer to this.

401 - Your cookie is invalid. Make sure it has no spaces or line breaks and you are accessing the cookie from the IP the account was logged in from.

403 - You cannot manage the game you are trying to access.

400 - Usually occurs when you have an invalid badge name.

500 - Something's wrong with Roblox; this is not your fault.

429 - Too many requests. Make sure you aren't making lots of requests to Roblox.

404 - Really rare occasions when the code is probably obsolete. Open an issue if you get this; this is most likely my bad coding.
