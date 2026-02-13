class EmployeeSalary:
    hourly_payment = 400 
    
    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    
    @classmethod
    def get_hours(cls, name, hours=None, rest_days=None, email=None):
        if hours is None:
            if rest_days is not None:
                hours = (7 - rest_days) * 8
            else:
                hours = 0  
        
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours=None, rest_days=None, email=None):
        if email is None:
            email = f"{name}@email.com"
        
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment
    
    def salary(self):
        if self.hours is None:
            if self.rest_days is not None:
                self.hours = (7 - self.rest_days) * 8
            else:
                return 0 
        
        return self.hours * self.hourly_payment



if __name__ == "__main__":
    emp1 = EmployeeSalary("Иван", hours=40, rest_days=2, email="ivan@company.com")
    print(f"Зарплата {emp1.name}: {emp1.salary()}")  
    print(f"Email: {emp1.email}")
    
    emp2 = EmployeeSalary.get_hours("Мария", rest_days=1)
    print(f"\nЗарплата {emp2.name}: {emp2.salary()}")  
    print(f"Часы Марии: {emp2.hours}")
    
    emp3 = EmployeeSalary.get_email("Петр", hours=35, rest_days=0)
    print(f"\nEmail Петра: {emp3.email}")  
    print(f"Зарплата Петра: {emp3.salary()}")  
    
    print(f"\nСтарая ставка: {EmployeeSalary.hourly_payment}")
    EmployeeSalary.set_hourly_payment(450)
    print(f"Новая ставка: {EmployeeSalary.hourly_payment}")
    
    print(f"Зарплата Ивана по новой ставке: {emp1.salary()}")
    print(f"Зарплата Марии по новой ставке: {emp2.salary()}")  
    
    emp4 = EmployeeSalary("Анна")
    print(f"\nЗарплата Анны без данных о часах: {emp4.salary()}")  