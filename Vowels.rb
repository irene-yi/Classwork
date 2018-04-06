def cap (word)
	first_letter = word[0].upcase!
	letter_join = first_letter << word
	lower_letter = letter_join.chomp[1]
	letter_join.delete!(lower_letter)
	puts letter_join
end

word = gets.chomp
cap(word)