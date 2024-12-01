#!/usr/bin/env python3
import sys

class Module():
    def __init__(self, name, destinations: list[str]):
        self.name = name
        self.destinations = destinations
    
    def __str__(self):
        return f"%{self.name} -> dest = {[d for d in self.destinations]}"
    
    # def add_destinations(self):
    #     dests = []
    #     for dest in self.destinations:
    #         # add destination module as univariate graph
    #         for module in self.modules:
    #             if module.name == dest:
    #                 dests.append(module)
    #     self.destinations = dests
            

class FlipFlop(Module):
    def __init__(self, name, destinations: list[str]):
        super().__init__(name, destinations)
        self.state = 0 

    def flip(self):  
        self.state = 1 - self.state
        print(f"{self.name} flipped. New state: {self.state}")

    def send_pulse(self):
        pass

class Conjunction(Module):
    def __init__(self, name, destinations: list[str]):
        super().__init__(name, destinations)
        self.memory = [0] * 1
        self.connections = {}

    def __str__(self):
        connected_modules = ', '.join(self.connections.keys())
        return f"Connections: {connected_modules}"

    def add_connection(self, connected_module):
        if connected_module not in self.connections:
            self.connections[connected_module] = 0

    def update_memory(self):
        pass

    def send_pulse(self):
        pass


class Relay:
    def __init__(self):
        self.modules = []
    
    def __str__(self):
        module_strings = [str(module) if hasattr(module, '__str__') else repr(module) for module in self.modules]
        return f"The relay contains {len(self.modules)} modules e.g. {module_strings}"
    
    def add_module(self, row):
        dest = [item.replace(',','') for item in row.split()[2:]]
        if row[0] == 'b':
            self.modules.append(Module('Broadcaster', row[(row.find('>') + 1) :].split(',')))
        elif row[0] == '%':
            self.modules.append(FlipFlop(row[1:].split()[0], dest))
        elif row[0] == '&':
            self.modules.append(Conjunction(row[1:].split()[0], dest))
    
    def get_conjunction_connections(self):
        connections = {}
        for module in self.modules:
            if isinstance(module, Conjunction):
                connected_modules = []
                for m in self.modules:
                    if module.name in m.destinations:
                        connected_modules.append(m.name)
                        module.add_connection(m.name)  # Pass the name, not the module
                connections[module.name] = connected_modules

        return connections
    
    def get_module(self, name):
        for module in self.modules:
            if module.name == name:
                return module
    
    def add_destinations(self):   
        for module in self.modules:
            dest = []
            for d in module.destinations:
                dest.append(self.get_module(d))
            module.destinations = dest


    def add_destinations(self):   
        for module in self.modules:
            dest = []
            for d in module.destinations:
                if module.name == 'Broadcaster':
                    dest.append(self.get_module('a'))  # Handle the case for Broadcaster
                else:
                    dest.append(self.get_module(d))
            module.destinations = dest
    
    def send_pulse(self):
        return 0
    
class Decoder:
    def part1(self, rows):
        rows = [row.replace('\n', '') for row in rows]
        relay = Relay()
        for row in rows:
            relay.add_module(row)

        relay.get_conjunction_connections()
        relay.add_destinations()
        print(relay)
        result = relay.send_pulse()
        print(relay.get_module('a'))
    
        return result

    def part2(self, rows):
        return 0

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day20.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            decoder_instance = Decoder()
            Part1 = decoder_instance.part1(rows=rows)
            Part2 = decoder_instance.part2(rows=rows)
            print(f"Part 1: {Part1}")
            print(f"Part 2: {Part2}")

    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except PermissionError:
        print(f"Permission denied for '{sys.argv[1]}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return 0

if __name__ == "__main__":
    main()