import pygame
import math
from queue import PriorityQueue
from memory_profiler import profile

WIDTH = 600
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A star Path Finding Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Spot:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = WHITE
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows

	def get_pos(self):
		return self.row, self.col

	def is_closed(self):
		return self.color == RED

	def is_open(self):
		return self.color == GREEN

	def is_barrier(self):
		return self.color == BLACK

	def is_start(self):
		return self.color == ORANGE

	def is_end(self):
		return self.color == TURQUOISE

	def reset(self):
		self.color = WHITE

	def make_start(self):
		self.color = ORANGE

	def make_closed(self):
		self.color = RED

	def make_open(self):
		self.color = GREEN

	def make_barrier(self):
		self.color = BLACK

	def make_end(self):
		self.color = TURQUOISE

	def make_path(self):
		self.color = PURPLE

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		return False


def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2) #Manhattan
	


def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()
	return False


def algorithm(draw, grid, start, end):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	came_from = {}
	g_score = {spot: float("inf") for row in grid for spot in row}
	g_score[start] = 0
	f_score = {spot: float("inf") for row in grid for spot in row}
	f_score[start] = h(start.get_pos(), end.get_pos())

	open_set_hash = {start}

	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = open_set.get()[2]
		open_set_hash.remove(current)

		if current == end:
			reconstruct_path(came_from, end, draw)
			end.make_end()
			return True

		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
				if neighbor not in open_set_hash:
					count += 1
					open_set.put((f_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					#neighbor.make_open()

		draw()

		#if current != start:
			#current.make_closed()




def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = Spot(i, j, gap, rows)
			grid[i].append(spot)

	return grid


def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
	win.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()


def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col

@profile
def main(win, width):
	ROWS = 25
	grid = make_grid(ROWS, width)

	start = None
	end = None

  

	obstacle=grid[7][5]
	obstacle.make_barrier()

	obstacle=grid[10][4]
	obstacle.make_barrier()

	obstacle=grid[10][14]
	obstacle.make_barrier()

	obstacle=grid[9][4]
	obstacle.make_barrier()

	obstacle=grid[11][1]
	obstacle.make_barrier()

	obstacle=grid[1][3]
	obstacle.make_barrier()

	obstacle=grid[1][7]
	obstacle.make_barrier()

	obstacle=grid[5][2]
	obstacle.make_barrier()
	obstacle=grid[3][1]
	obstacle.make_barrier()
	obstacle=grid[4][1]
	obstacle.make_barrier()

	obstacle=grid[3][2]
	obstacle.make_barrier()
	obstacle=grid[8][1]
	obstacle.make_barrier()
	obstacle=grid[7][2]
	obstacle.make_barrier()

	obstacle=grid[13][2]
	obstacle.make_barrier()
	obstacle=grid[2][1]
	obstacle.make_barrier()
	obstacle=grid[10][3]
	obstacle.make_barrier()

	obstacle=grid[3][2]
	obstacle.make_barrier()
	obstacle=grid[3][4]
	obstacle.make_barrier()
	obstacle=grid[5][6]
	obstacle.make_barrier()

	obstacle=grid[3][5]
	obstacle.make_barrier()
	obstacle=grid[6][6]
	obstacle.make_barrier()
	obstacle=grid[7][7]
	obstacle.make_barrier()

	
	for i in range(10,19):
		obstacle=grid[i][10]
		obstacle.make_barrier()

	for i in range(1,5):
		obstacle=grid[i][4]
		obstacle.make_barrier()
	

	for i in range(1,5):
		obstacle=grid[i][7]
		obstacle.make_barrier()

		
	for i in range(1,5):
		obstacle=grid[i][6]
		obstacle.make_barrier()

		
	for i in range(1,5):
		obstacle=grid[8][i]
		obstacle.make_barrier()

		
	for i in range(0,9):
		obstacle=grid[i][13]
		obstacle.make_barrier()

		
	for i in range(1,9):
		obstacle=grid[8][i]
		obstacle.make_barrier()

		
	for i in range(1,9):
		obstacle=grid[9][i]
		obstacle.make_barrier()

	run = True
	while run:
		draw(win, grid, ROWS, width)

		start=grid[10][10]
		start.make_start()

		start2=grid[2][6]
		start2.make_start()

		start3=grid[0][0]
		start3.make_start()


		end=grid [24][23]
		end.make_end()
		


	
		

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				run = False
		
			
		for R in grid:
			for spot in R:
				spot.update_neighbors(grid)

		algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
		start.make_start()
		algorithm(lambda: draw(win, grid, ROWS, width), grid, start2, end)
		start2.make_start()
		algorithm(lambda: draw(win, grid, ROWS, width), grid, start3, end)
		start3.make_start()
		
		run = False

			
		for i in range(1000):
			draw(win, grid, ROWS, width)
	
	pygame.quit() 

main(WIN, WIDTH)