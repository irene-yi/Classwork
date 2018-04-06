class Cypher
	def cipher
		#letters to numbers
		{'a' => '001', 'b' => '002', 'c' => '003', 'd' => '004', 'e' => '005',
		 'f' => '010', 'g' => '020', 'h' => '030', 'i' => '040', 'j' => '050',
		 'k' => '100', 'l' => '200', 'm' => '300', 'n' => '400', 'o' => '500',
		 'p' => '006', 'q' => '007', 'r' => '008', 's' => '009', 't' => '700',
		 'u' => '060', 'v' => '070', 'w' => '080', 'x' => '090', 'y' => '900',
		 'z' => '600',}
	end

	def encrypt(letter)
		#lowercase every letter
		low_case = letter.downcase
		
		#go through the cipher
		cipher[low_case]
	end

	def encrypt_string(moo)
		
		#lowercase everything in the string
		low_case = moo.downcase
		
		
		cow = low_case.split("")
		results = []
		for x in cow do
			encrypted_letter = encrypt(x)
			results.push(encrypted_letter)
		end

		results.join
	end

end