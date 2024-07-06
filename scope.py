#global scope
my_global=15

def fn1():
    enclosed_v=10

    def fn2():
        local_v=5
        print('Accesss to global:', my_global)
        print('Acccess to enclosed:', enclosed_v)
    fn2()

fn1()