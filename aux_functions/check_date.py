import datetime
import json
import os

class CheckDate:

    def check_valid_date(self, string_date):
        try:
            string_date = string_date.replace("-", "/")
            if len(string_date) == 5:
                converted_date = datetime.datetime.strptime(string_date, "%d/%m")
                converted_date = converted_date.date()
            else:
                converted_date = datetime.datetime.strptime(string_date, "%d/%m/%Y")
                converted_date = converted_date.date()
        except:
            converted_date = ""
        
        return converted_date


    def check_sign(self, birthday_date):
        base_path = os.path.abspath(os.path.dirname(__file__))
        with open (base_path + "/signs_names.json") as sign_file:
            sign_list = json.load(sign_file)

        if birthday_date.month == 12:
            sign = "sagitario" if (birthday_date.day < 22) else "capricornio"
        elif birthday_date.month == 1:
            sign = "capricornio" if (birthday_date.day < 20) else "aquario"
        elif birthday_date.month == 2:
            sign = "aquario" if (birthday_date.day < 19) else "peixes"
        elif birthday_date.month == 3:
            sign = "peixes" if (birthday_date.day < 21) else "aries"
        elif birthday_date.month == 4:
            sign = "aries" if (birthday_date.day < 20) else "touro"
        elif birthday_date.month == 5:
            sign = "touro" if (birthday_date.day < 21) else "gemeos"
        elif birthday_date.month == 6:
            sign = "gemeos" if (birthday_date.day < 21) else "cancer"
        elif birthday_date.month == 7:
            sign = "cancer" if (birthday_date.day < 23) else "leao"
        elif birthday_date.month == 8:
            sign = "leao" if (birthday_date.day < 23) else "virgem"
        elif birthday_date.month == 9:
            sign = "virgem" if (birthday_date.day < 23) else "libra"
        elif birthday_date.month == 10:
            sign = "libra" if (birthday_date.day < 23) else "escorpiao"
        elif birthday_date.month == 11:
            sign = "escorpiao" if (birthday_date.day < 22) else "sagitario"
        
        sign_message = sign_list.get(sign)

        return sign_message