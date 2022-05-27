from collections import namedtuple
from datetime import datetime
import multiprocessing as mp
import random
import time
import enum


class C(enum.Enum):
    Green = "\u001b[32m"
    Magenta = "\u001b[35m"
    Yellow = "\u001b[33m"
    Cyan = "\u001b[36m"
    Blue = "\u001b[34m"
    Red = "\u001b[31m"
    White = "\u001b[37m"
    Reset = "\u001b[0m"
    # Black = "\u001b[30m"

Chopstick = namedtuple("Chopstick", "semaforo name")  

class Philosopher:
    def __init__(self, name, color: C, chopstick_derecho: Chopstick, chopstick_izquierdo: Chopstick):
        self.name = name
        self.color = color
        self.chopstick_derecho = chopstick_derecho
        self.eating_time = random.randint(2, 5)
        self.thinking_time = random.randint(2, 5)
        self.chopstick_izquierdo = chopstick_izquierdo
    
    def think(self):
        self.log(f"Empieza a pensar {self.thinking_time} segs")
        time.sleep(self.thinking_time)
        self.log("Termino de pensar")

    def _acquire_chopsticks(self) -> bool:
        # TODO: Wait for right chopstick.
        a = self.chopstick_derecho.semaforo.acquire()
        self.log(f"Palillo derecho {self.chopstick_derecho.name} {a}")
        # TODO: Get the left chopstick or release the right one.
        b = self.chopstick_izquierdo.semaforo.acquire()
        self.log(f"Palillo izquierdo {self.chopstick_izquierdo.name} , {b}")
        
        if a and b: 
            return True

    def _release_chopsticks(self):
        self.log("Releasing chopsticks")
        # TODO: Release both chopsticks.
        self.chopstick_derecho.semaforo.release()
        self.log(f"liberando {self.chopstick_derecho.name}")
        self.chopstick_izquierdo.semaforo.release()
        self.log(f"liberando {self.chopstick_izquierdo.name}")
        self.log("Released chopsticks")

    def eat(self):
        while not self._acquire_chopsticks():
            self.waiting()
            time.sleep(1)

        self.log(f"START Eating for {self.eating_time} seconds")
        time.sleep(self.eating_time)
        self.log("END   Eating")

        self._release_chopsticks()

    def waiting(self):
        self.log("START Waiting")
        time.sleep(1)  # Everyone waits the same.
        self.log("END   Waiting")

    def run(self):
        while True:
            self.think()
            self.eat()

    def log(self, msg):
        print(
            f"{self.color.value}{datetime.utcnow().isoformat(sep=' ', timespec='microseconds')}|{self.name}|{msg}{C.Reset.value}"
        )


if __name__ == "__main__":
    print("START OF PROGRAM")

    a = int(input("ingresa el numero: "))

    Chopsticks = [Chopstick(mp.Semaphore(), f"chopstick {i}") for i in range(a)]

    filosofos = []

    for i in range(a):
        r = i
        if (
            i == len(Chopsticks) - 1
        ): 
            l = 0
        else:
            l = i + 1  
            print(f"left {l}, right {r}")
        phil = Philosopher(
            f"P{i+1}",
            list(C)[i],
            chopstick_derecho=Chopsticks[r],
            chopstick_izquierdo=Chopsticks[l],
        )
        x = mp.Process(target=phil.run)
        filosofos.append(x)
        x.start()

    for a in filosofos:
        a.join()

    print("END OF PROGRAM")
