text = open('test.txt','r')
readLines = text.readlines()

class EngineDecoder:

    def decode(self, lines: list[str]) -> int:
        
        grid = self.to_grid(lines)
        total_count = 0
        for row in range(len(grid)):
            for cell in range(len(grid[row])):
                if grid[row][cell].isnumeric():
                    number_region = self.get_entire_number_region(grid=grid, row=row,cell=cell)
                    is_part = self.check_is_part(grid, number_region, row)

                    if is_part:
                        list_to_add = grid[row][number_region[0]:number_region[1]]
                        number_to_add = int(''.join(list_to_add))
                        total_count+= number_to_add
                    for x in range(number_region[0],number_region[1]):
                        grid[row][x] = '.'


        return total_count

    def to_grid(self, lines: list[str]) -> list[list[str]]:
        grid = []
        for line in lines:
            row = list(line.rstrip())
            grid.append(row)
        return grid

    def get_entire_number_region(self, grid: list[list[str]], cell: int, row: int) -> list[int]:
        right_bound = len(grid[0])
        start = cell
        end = cell
        while start >= 0 and grid[row][start].isdigit():
            start-=1

        while end < right_bound and grid[row][end].isdigit():
            end += 1

        return [start+1, end]

    def check_is_part(self, grid: list[list[str]], range_check: list[int], y: int) -> bool:
        start, end = range_check[0], range_check[1]-1
        lower_bound, right_bound = len(grid), len(grid[0])
        is_part = False
        #Check this doesn't go out of bounds
        for x in range(start, min(len(grid[0]),end+1)):
            eight_directions = {
                "up": [x,y+1],
                "down": [x,y-1],
                "right": [x+1,y],
                "left": [x-1,y],
                "left_up": [x-1,y+1],
                "left_down": [x-1,y-1],
                "right_up": [x+1,y+1],
                "right_down": [x+1,y-1]
                }
            for direction in eight_directions:
                x_new, y_new = eight_directions[direction][0], eight_directions[direction][1]
                #Check not out of bounds
                if x_new > 0 and x_new < right_bound and y_new > 0 and y_new < lower_bound:
                    if not grid[y_new][x_new].isalnum() and not grid[y_new][x_new] == '.':
                        is_part = True
        return is_part

print(EngineDecoder().decode(readLines))