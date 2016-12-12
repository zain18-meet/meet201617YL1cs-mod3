from student import Student

Nisreen=Student('Nisreen','Jerusalem','15','165','vanilla')
Rajai=Student('Rajai','Jerusalem','15','178','chocolate')
Ofek=Student('Ofek','Adam','16','175','strawberry')

Nisreen.print_summary()
Rajai.print_summary()
Ofek.print_summary()

Nisreen.get_giraffe_gap()
Rajai.get_giraffe_gap ()
Ofek.get_giraffe_gap ()

N=Nisreen.get_giraffe_gap()
R=Rajai.get_giraffe_gap ()
O=Ofek.get_giraffe_gap ()

print(N,R,O)
