random_numbers = [0.5, -7, 10, 3]

def counter(col)
max = 0
min = 0

for x in col do
	for y in col do
		if y > x
			max = y
		elsif y < x
			min = y
		end
	end
end

puts "Max Number: #{max}"
puts "Min Number: #{min}"

range = max - min
puts "Range: #{range}"


end



#To call the method

counter(random_numbers)