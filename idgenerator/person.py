class person:
    def __init__(self, name, surname, phone, personal_num,
                 adress, postal_code, city):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = self.get_email()
        self.personal_num = personal_num
        self.adress = adress
        self.postal_code = postal_code
        self.city = city

    def __str__(self):
        return f"{self.name} {self.surname}"

    def get_email(self):
        s = f"{self.name}.{self.surname}@mail.com".casefold()
        s = s.replace("å", "a")
        s = s.replace("ä", "a")
        s = s.replace("ö", "o")
        return s

    def print(self):
        s = (f"Namn: {self.name} {self.surname}\n"
             f"Personnummer: {self.personal_num}\n"
             f"Telefon: {self.phone}\n"
             f"Mejl: {self.email}\n"
             f"\nAdress: {self.adress}\n"
             f"{self.postal_code} {self.city}")
        return s
