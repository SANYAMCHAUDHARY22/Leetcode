class Solution:
    def numTeams(self, rating: List[int]) -> int:
        r, size = rating, len( rating )
        
		# compute statistics of sliding range
        left_smaller = [ sum( r[i] < r[j] for i in range(0,j) ) for j in range(size) ]
        right_bigger = [ sum( r[j] < r[k] for k in range(j+1, size) ) for j in range(size)]
        
        num_of_teams = 0
		
		# j slides from 0 to ( n-1 ), and j stands for the index of middle element
        for j in range( 0, size):
		
            num_of_ascending_team = left_smaller[j] * right_bigger[j]
			
            num_of_descending_team = ( j - left_smaller[j] ) * ( size-1 - j - right_bigger[j] )
            
            num_of_teams += ( num_of_ascending_team + num_of_descending_team )
            
        return num_of_teams