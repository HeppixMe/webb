print("\033c")
print("\033[?25l")
width = 120
height = 40
function restart()
    global screen = falses(width, height)
    global timeCount = 0
end
function show()
	print("\033[H")
    printstyled("Falling Sand Simulation"; color = :cyan)
    print("\n")
	print("|")
	for i in 1:width
		print("-")
	end
	print("|")
	print("\n")
	print("|")
	for i in 1:length(screen)
		if screen[i]
			printstyled("*"; color = :yellow)
		else
			print(" ")
		end
		if i % width == 0
			print("|")
			print("\n")
			print("|")
		end
	end
	for i in 1:width
		print("-")
	end
	print("|")
    

end

function update()
	nextscreen = falses(width, height)
	for i in 1:width
		nextscreen[end-i]=screen[end-i]
	end

	for i in 1:(length(screen)-width)
		if screen[i]
			if !screen[i+width]
				nextscreen[i+width] = true
			else
				if !screen[i+width-1] && !screen[i+width+1]
                    nextscreen[i+width+rand([-1,1])[1]] = true
                else
					if !screen[i+width-1]
						nextscreen[i+width-1]=true
					else
						if !screen[i+width+1]
							nextscreen[i+width+1]=true

						else
							nextscreen[i] = true
						end
					end
				end
			end
		end
	end
    global screen = nextscreen
	
end
restart()
while true
    
	update()
    show()
	global timeCount += 1
    if screen[40] && screen[60] && screen[80]
        restart()
    end
	if timeCount == 3
		screen[40] = true
        screen[80] = true
        screen[60] = true
		timeCount = 0
    end
end
