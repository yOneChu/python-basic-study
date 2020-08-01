

## class 생성
class Quad():
    height = 0
    width = 0
    color = ''
    name = 'Qurd'

    def quad_name(self, arg1, arg2):
        print(arg1, arg2)
        return self.name


quad1 = Quad()
quad1.height = 30


print(quad1.name)
print(quad1.height)
print(quad1.quad_name('kk', 'bb'))