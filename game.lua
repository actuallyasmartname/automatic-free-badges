local initial = true
while true do
	local http = game:GetService("HttpService")
	local num = 0
	local freebadge = {}
	local c = ""
	local stop = false
	while stop == false do
		local s, m = pcall(function()
			return http:JSONDecode(http:GetAsync("https://badges.roproxy.com/v1/universes/"..game.GameId.."/badges?limit=100&cursor=" .. c .. "&sortOrder=Desc"))
		end)
		if type(m) ~= "table" then
			if initial == true then
				warn("Something went wrong setting up automatic badges. Try rejoining or waiting another time.")
				do return end
			end
		elseif type(m) == "table" then
			for i=1,#m.data do
				table.insert(freebadge,m.data[i].id)
			end
			num += #m.data
			if m.nextPageCursor == nil then
				stop = true
				initial = false
				local pos = -47.75
				local pos2 = -47.75
				for i,v in pairs(game.Workspace:GetDescendants()) do
					if v.Name == "BadgeAwarder" then
						v:Destroy()
					end
				end
				local freefolder = Instance.new("Folder", game.Workspace)
				freefolder.Name = "AutomaticBadges"
				for f=1, #freebadge do
					local clone = game.ReplicatedStorage.BadgePlatform:Clone()
					clone.Parent = freefolder
					clone.BadgeID.Value = freebadge[f]
					clone.Position = Vector3.new(pos-8, -0.5, 5)
					pos = pos - 8
				end
			else
			c = m.nextPageCursor
		end
	end
end
	task.wait(120)
end
