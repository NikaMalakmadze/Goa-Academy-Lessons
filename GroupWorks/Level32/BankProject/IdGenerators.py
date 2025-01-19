
import random
import string

#ფუქცია, რომელიც ქმნის მომხმარებლის უნიკალურ ID_ს
def User_ID_generator():
    
    #ერთ ცვლადში ვათავსებთ ყველა ინგლისურ ასოს(დიდსაც და პატარასაც) და ყველა ციფრს
    USER_ID_CHARS = string.ascii_letters + string.digits * 2
    
    #random მოდულის საშუალებით ვქმნით 9 სიმბოლოიან ID_ს
    User_ID = ''.join(random.choice(USER_ID_CHARS) for _ in range(9))

    return User_ID              #ვაბრუნებთ User_ID_ს

#ფუქცია, რომელიც ქმნის ბარათის უნიკალურ ID_ს
def Card_ID_generator():
    
    #ერთ ცვლადში ვათავსებთ ყველა ციფრს
    CARD_ID_CHARS = string.digits

    #random მოდულის საშუალებით ვქმნით 9 სიმბოლოიან ID_ს
    Card_ID = ''.join(random.choice(CARD_ID_CHARS) for _ in range(9))

    return Card_ID              #ვაბრუნებთ Card_ID_ს
