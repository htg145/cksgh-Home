# class Animal:  # 부모 클래스
#     def __init__(self, name):
#         self.name = name  # 공통 속성
#
#     def eat(self):
#         print(f"{self.name}가 밥을 먹습니다.")
#
#
# class Cat(Animal):  # 자식 클래스
#     def bark(self):
#         print(f"{self.name}가 야옹.")
#
#
# cat = Cat("메루")
# cat.eat()  # 부모 클래스의 메서드 호출
# cat.bark()  # 자식 클래스의 메서드 호출

# class Car:
#     def drive(self):
#         print("자동차가 앞으로 전진합니다.")
#
#
# class ElectricCar(Car):
#     def drive(self):  # 메서드 오버라이딩
#         super().drive()  # 부모 클래스의 메서드 호출
#         print("전기로 작동 합니다.")
#
#
# electric_car = ElectricCar()
# electric_car.drive()

# class GrandParent:
#     def introduce(self):
#         print("우리는 할머니 할아버지")
#
# class Parent(GrandParent):
#     def introduce(self):
#         super().introduce()
#         print("우리는 엄마 아빠")
#
# class Child(Parent):
#     def introduce(self):
#         super().introduce()
#         print("우리는 자식")
#
#     def work(self):
#         print("우리는 일을 합니다.")
#
#     def study(self):
#         print("우리는 공부를 합니다.")
#
# child = Child()
# child.introduce()
# child.work()
# child.study()


# class A:
#     def introduce(self):
#         print("나는 A입니다.")
#
#
# class B:
#     def introduce(self):
#         print("나는 B입니다.")
#
#
# class C:
#     def introduce(self):
#         print("나는 C입니다.")
#
#
# class Child(A, B, C):
#     def introduce(self):
#         print(Child.mro())  # MRO 출력
#         super().introduce()  # MRO에 따른 메서드 호출
#
#
# child = Child()
# child.introduce()

# class A:
#     def introduce(self):
#         print("나는 A")
#
# class B:
#     def introduce(self):
#         print("나는 B")
#
# class C:
#     def introduce(self):
#         print("나는 C")
#
# class Child(A, B, C):
#     def introduce(self):
#         print(Child.mro())
#         super().introduce() # MRO 에 따라 첫 번째 순서 대로 정의
#         super(A, self).introduce()
#         C.introduce(self)
#
# child = Child()
# child.introduce()


class Rocket:
    def __init__(self, name, company, fuel):
        self.name = name
        self.company = company
        self.fuel = fuel

    def status(self):
        print(f"회사: {self.company} {self.name}  연료: {self.fuel}")

    def ignite(self):
        print(f"{self.name} 점화 !!")

rocket1 = Rocket("팰컨9", "SpaceX", 100)
rocket1.status()
rocket1.ignite()

class Booster:
    def boost(self):
        print("부스터 !!")

class Separator:
    def separate(self):
        print("단계 분리 !!")

class Launch:
    def launch_stage(self):
        print("발사!!")

class Rocket_load(Rocket, Booster, Separator, Launch):
    def __init__(self, name, company, fuel):
        super().__init__(name, company, fuel)

    def launch(self, load):
        self.separate()
        self.launch_stage()
        self.boost()
        print("발사 완료")

rocket2 = Rocket_load("팰컨9", "SpaceX", 100)
rocket2.launch("완료")
















