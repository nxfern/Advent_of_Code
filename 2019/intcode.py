from collections import defaultdict
from typing import Callable

class Computer:
    OPS: dict[int, Callable[[int, int], int]] = {
        1: lambda a, b: a + b,
        2: lambda a, b: a * b, 
        7: lambda a, b: int(a < b),
        8: lambda a, b: int(a == b)
    }

    IP_OPS: dict[int, Callable[["Computer", int, int], int]] = {
        5: lambda self, a, b: self.param(2, b) if self.param(1, a) != 0 else self.ip+3,
        6: lambda self, a, b: self.param(2, b) if self.param(1, a) == 0 else self.ip+3
    }

    def __init__(self, data: list[int]) -> None:
        self.ip = 0
        self.base = 0
        self.halted = False
        self.mem: defaultdict[int, int] = defaultdict(int)
        for i, d in enumerate(data): self.mem[i] = d
        
    def param(self, offset: int, mode: int) -> int:
        v = self.mem[self.ip + offset]
        if mode == 0:   return self.mem[v]
        elif mode == 1: return v
        elif mode == 2: return self.mem[self.base + v]
        raise ValueError("Invalid mode: {mode}")
    
    def dest(self, offset: int, mode: int) -> int:
        v = self.mem[self.ip + offset]
        if mode == 0:   return v
        elif mode == 2: return self.base + v
        raise ValueError(f"Invalid destination mode: {mode}")
    
    def run(self, inputs: int|list[int], feedback: bool=False) -> int | None:
        inputs = [inputs] if isinstance(inputs, int) else inputs
        output = None
        while self.ip < len(self.mem):
            instruction = self.mem[self.ip]
            op = instruction % 100
            m1 = (instruction // 100) % 10
            m2 = (instruction // 1000) % 10
            m3 = (instruction // 10000) % 10
            if op == 99:
                self.halted = True
                return output
            elif op in self.OPS:
                self.mem[self.dest(3, m3)] = self.OPS[op](self.param(1, m1), self.param(2, m2))
                self.ip += 4
            elif op in self.IP_OPS:
                self.ip = self.IP_OPS[op](self, m1, m2)
            elif op == 3:
                if not inputs:
                    return output   # pause until value available
                self.mem[self.dest(1, m1)] = inputs.pop(0)
                self.ip += 2
            elif op == 4:
                output = self.param(1, m1)
                self.ip += 2
                if feedback:
                    return output
            elif op == 9:
                self.base += self.param(1, m1)
                self.ip += 2
            else:
                raise ValueError(f"Unknown opcode {op} at ip={self.ip}")
        self.halted = True
        return output  # unlikely to be correct if triggered