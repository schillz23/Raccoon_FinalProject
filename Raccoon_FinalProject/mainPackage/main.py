# Name: Kaileb Strasser, Max Schiller, & Connor Laughlin
# email: strassks@mail.uc.edu, schillms@mail.uc.edu, laughlcd@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4/23/2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Decrypt text and json files to uncover details about taking a group photo on campus with a movie quote
# Brief Description of what this module does:
# Citations:
# Anything else that's relevant:

#main.py



if __name__ == "__main__":
    def main():
        file_path = "../Files/UCEnglish.txt"
        line_numbers = [42061, 44404, 28799, 298, 8848, 27781, 105654, 21723, 47096, 8021, 28420, 19312, 22147, 42049, 23887, 599, 105655, 24232, 19312, 9443]
        TextFileExtractor(file_path, line_numbers)
        
        
        
        
        
        
        
        # 3  Aes Decryption
        key = 'LMV69IGGTp2Gyn4TI-DTuupf0VvugeC5API5dpeoiqM='
        decryptor = MessageDecryptor(key)
        json_reader = JsonDataReader('../Files/TeamsAndEncryptedMessagesForDistribution.json')
        movie_data = json_reader.get_raccoon_data()
        strMovieMessage = ''.join([str(item) for item in movie_data])
        # Replace 'your_encrypted_message_here' with the actual encrypted message
        encrypted_message = strMovieMessage
        # Decrypt the message
        decrypted_message = decryptor.decrypt(encrypted_message)
        # Display the result
        print(decrypted_message)


   
    
    
    

