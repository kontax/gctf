import sys


class VM:
    def __init__(self):
        self.stack = []
        self.r1 = 0
        self.r2 = 0

    def add(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(b + a)

    def sub(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(b - a)

    def multiply(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(b * a)

    def divide(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(b // a)

    def modulo(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(b % a)

    def xor(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(b ^ a)

    def clone(self):
        self.stack.append(self.stack[-1])

    def print_top(self):
        sys.stdout.write(chr(self.stack.pop()))
        sys.stdout.flush()

    def jump_top(self):
        ip = self.stack.pop()
        if ip == 389:
            self.JMP_389()
        elif ip == 568:
            self.JMP_568()
        elif ip == 1023:
            self.JMP_1023()
        else:
            print(f"JUMP_TOP {ip}")

    def START_1(self):

        # Swap the top 2 self.stack items
        self.r1 = self.stack.pop()
        self.stack.append(self.r2)
        self.stack.append(self.r1)

        self.r1 = 389
        self.stack.append(self.r1)
        self.stack.append(self.r2)
        self.GOTO_D()

    def JMP_389(self):
        self.xor()

        self.print_top()

        self.r1 = 1
        self.stack.append(self.r1)

        self.add()

        self.r2 = self.stack.pop()
        if self.stack[-1] != 0:
            self.START_1()

    def START_2(self):

        # Swap the top 2 self.stack items
        self.r1 = self.stack.pop()
        self.stack.append(self.r2)
        self.stack.append(self.r1)

        self.r1 = 568
        self.stack.append(self.r1)
        self.stack.append(self.r2)
        self.GOTO_D()

    def JMP_568(self):
        self.xor()

        self.print_top()

        self.r1 = 1
        self.stack.append(self.r1)

        self.add()

        self.r2 = self.stack.pop()
        if self.stack[-1] != 0:
            self.START_2()

    def START_3(self):

        # Swap the top 2 self.stack items
        self.r1 = self.stack.pop()
        self.stack.append(self.r2)
        self.stack.append(self.r1)

        self.r1 = 1023
        self.stack.append(self.r1)
        self.stack.append(self.r2)
        self.GOTO_D()

    def JMP_1023(self):
        self.xor()

        self.print_top()

        self.r1 = 1
        self.stack.append(self.r1)

        self.add()

        self.r2 = self.stack.pop()
        if self.stack[-1] != 0:
            self.START_3()
        raise SystemExit()

    def GOTO_D(self):
        self.r1 = 2
        self.stack.append(self.r1)
        self.GOTO_I()

    def GOTO_E(self):
        self.GOTO_I()

    def GOTO_F(self):
        if self.stack[-1] == 0:
            self.stack.pop()
            self.GOTO_H()
        else:
            self.stack.pop()
            self.GOTO_K()

    def GOTO_G(self):
        if self.stack[-1] == 0:
            self.stack.pop()
            self.GOTO_H()
            return

        self.stack.pop()
        self.r1 = self.stack.pop()
        self.r2 = 1
        self.stack.append(self.r2)

        self.sub()

        if self.stack[-1] == 0:
            self.stack.pop()
            self.r2 = self.stack.pop()
            self.stack.append(self.r1)
            self.stack.append(self.r2)
            self.jump_top()
        else:
            self.stack.append(self.r1)
            self.GOTO_H()

    def GOTO_H(self):
        self.r2 = 1
        self.stack.append(self.r2)

        self.add()

        self.GOTO_E()

    def GOTO_I(self):
        self.clone()
        self.r1 = 2
        self.stack.append(self.r1)
        self.GOTO_J()

    def GOTO_J(self):

        self.sub()

        if self.stack[-1] == 0:
            self.stack.pop()
            self.r1 = 1
            self.stack.append(self.r1)
            self.GOTO_F()
            return

        self.stack.pop()
        self.clone()
        self.stack.append(self.r1)

        self.modulo()

        if self.stack[-1] == 0:
            self.GOTO_F()
        else:
            self.stack.pop()
            self.clone()
            self.stack.append(self.r1)
            self.r1 = 1
            self.stack.append(self.r1)

            self.add()

            self.clone()
            self.r1 = self.stack.pop()
            self.GOTO_J()

    def GOTO_K(self):
        self.clone()
        self.clone()
        self.r2 = 0
        self.stack.append(self.r2)
        self.GOTO_L()

    def GOTO_L(self):
        self.r1 = 10
        self.stack.append(self.r1)

        self.multiply()

        self.r2 = self.stack.pop()
        self.stack.append(self.r1)

        self.modulo()
        self.stack.append(self.r2)
        self.add()
        self.r2 = self.stack.pop()
        self.r1 = self.stack.pop()
        self.clone()
        self.stack.append(self.r2)
        self.sub()
        if self.stack[-1] == 0:
            self.stack.pop()
            self.r2 = 1
            self.stack.append(self.r2)
            self.GOTO_G()
        else:
            self.stack.pop()
            self.stack.append(self.r1)
            self.r1 = 10
            self.stack.append(self.r1)
            self.divide()
            if self.stack[-1] == 0:
                self.GOTO_G()
            else:
                self.clone()
                self.stack.append(self.r2)
                self.GOTO_L()


if __name__ == '__main__':
    vm = VM()
    vm.stack.append(0)
    vm.stack.append(17488)
    vm.stack.append(16758)
    vm.stack.append(16599)
    vm.stack.append(16285)
    vm.stack.append(16094)
    vm.stack.append(15505)
    vm.stack.append(15417)
    vm.stack.append(14832)
    vm.stack.append(14450)
    vm.stack.append(13893)
    vm.stack.append(13926)
    vm.stack.append(13437)
    vm.stack.append(12833)
    vm.stack.append(12741)
    vm.stack.append(12533)
    vm.stack.append(11504)
    vm.stack.append(11342)
    vm.stack.append(10503)
    vm.stack.append(10550)
    vm.stack.append(10319)
    vm.stack.append(975)
    vm.stack.append(1007)
    vm.stack.append(892)
    vm.stack.append(893)
    vm.stack.append(660)
    vm.stack.append(743)
    vm.stack.append(267)
    vm.stack.append(344)
    vm.stack.append(264)
    vm.stack.append(339)
    vm.stack.append(208)
    vm.stack.append(216)
    vm.stack.append(242)
    vm.stack.append(172)
    vm.stack.append(74)
    vm.stack.append(49)
    vm.stack.append(119)
    vm.stack.append(113)
    vm.stack.append(119)
    vm.r1 = 106
    vm.stack.append(vm.r1)
    vm.r2 = 1

    vm.START_1()

    vm.stack.append(98426)
    vm.stack.append(97850)
    vm.stack.append(97604)
    vm.stack.append(97280)
    vm.stack.append(96815)
    vm.stack.append(96443)
    vm.stack.append(96354)
    vm.stack.append(95934)
    vm.stack.append(94865)
    vm.stack.append(94952)
    vm.stack.append(94669)
    vm.stack.append(94440)
    vm.stack.append(93969)
    vm.r1 = 93766
    vm.stack.append(vm.r1)
    vm.r2 = 99

    vm.START_2()

    vm.stack.append(101141058)
    vm.stack.append(101060206)
    vm.stack.append(101030055)
    vm.stack.append(100998966)
    vm.stack.append(100887990)
    vm.stack.append(100767085)
    vm.stack.append(100707036)
    vm.stack.append(100656111)
    vm.stack.append(100404094)
    vm.stack.append(100160922)
    vm.stack.append(100131019)
    vm.stack.append(100111100)
    vm.stack.append(100059926)
    vm.stack.append(100049982)
    vm.stack.append(100030045)
    vm.stack.append(9989997)
    vm.stack.append(9981858)
    vm.stack.append(9980815)
    vm.stack.append(9978842)
    vm.stack.append(9965794)
    vm.stack.append(9957564)
    vm.stack.append(9938304)
    vm.stack.append(9935427)
    vm.stack.append(9932289)
    vm.stack.append(9931494)
    vm.stack.append(9927388)
    vm.stack.append(9926376)
    vm.stack.append(9923213)
    vm.stack.append(9921394)
    vm.stack.append(9919154)
    vm.stack.append(9918082)
    vm.r1 = 9916239
    vm.stack.append(vm.r1)
    vm.r2 = 765

    vm.START_3()
