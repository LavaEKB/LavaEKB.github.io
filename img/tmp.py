class Elevator:
    def __init__(self, visota=5, etazh=3):
        self.visota = visota
        self.etazh = etazh

    def up(self):
        if self.etazh < self.visota:
            self.etazh += 1
            print(f'Лифт поднимается на {self.etazh} этаж')
        else:    
            print('Лифт не может подняться выше')

        

    def down(self):
        if self.etazh > 1:
            self.etazh -= 1
            print(f'Лифт опускается на {self.etazh} этаж')
        else:
            print('Лифт не может опуститься ниже')
 

elevator = Elevator(7, 6) 
elevator.up()       
elevator.up()
elevator.up()
elevator.down()
elevator.down()
elevator.down()
elevator.down()
