import random
from BaseAI_3 import BaseAI
import numpy as np

import os

class PlayerAI(BaseAI):

	def heu_1(self,move):
		grid = move
		map = grid.map
		mask = [[10,8,6,4],
				[8,7,5,3],
				[6,5,4,2],
				[4,3,2,1]]
		mask = np.array(mask)
		masks = [np.rot90(mask,i) for i in range(4)]
		h_vals = []
		for mask in masks:
			accu = 0
			for i in range(len(map)):
				for j in range(len(map[0])):
					accu += map[i][j] * mask[i][j]
			h_vals.append(accu)


		return

	def evaluate(self,state):
		return self.heu_1(state)

	def maximize(self, state, a, b, depth):
		if depth == 0:
			return 0,self.evaluate(state)
		maxChild, maxUtility = None, np.inf*-1

		for child in state.getAvailableMoves():
			_,utility = self.minimize(child[1], a, b, depth -1)

			if utility > maxUtility:
				maxChild, maxUtility = child, utility
			if maxUtility >= b:
				break
			if maxUtility > a:
				a = maxUtility
		return maxChild, maxUtility


	def minimize(self, state, a, b, depth):
		if depth == 0:
			return 0, self.evaluate(state)
		minChild, minUtility = None, np.inf

		for child in state.getAvailableMoves():
			_ , utility = self.maximize(child[1], a, b, depth-1)
			if utility < minUtility:
				minChild, minUtility = child, utility
			if minUtility <= a:
				break
			if minUtility < b:
				b = minUtility
		return minChild, minUtility


	def decision(self, state):
		child, _ = self.maximize(state,-1*np.inf, np.inf, 3)


	def getCompMoves(self, grid):
		avail = grid.getAvailableCells()
		moveset = []
		for x,y in avail:
			grid2 = grid.clone()
			grid4 = grid.clone()
			grid2.map[x][y] = 2
			grid4.map[x][y] = 4
			moveset.append(grid2)
			moveset.append(grid4)
		return



	def getMove(self, grid):
		# Selects a random move and returns it

		result = self.decision(grid)
		return result[0]