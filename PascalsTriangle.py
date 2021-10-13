def generate(self, numRows: int) -> List[List[int]]:
        # The outer list
        arr_out = []
        for i in range(1, numRows+1):
            # The inner list, initialized with 0
            arr_in = [0] * i
            
            # putting 1 to the either ends of this inner list
            arr_in[0] = 1
            arr_in[-1] = 1
            
            # Extra calculation starts when the length of inner list > 2
            if i > 2:
                # we need the last inner list for this operation
                prev = arr_out[-1]
                
                # The operation will only run on the inner items of this list
                for j in range(1, len(arr_in)-1):
                    # If the element is 0, we have to act
                    if arr_in[j] == 0:
                        arr_in[j] = prev[j-1] + prev[j]
            # Finally, append the inner list to the outer list
            arr_out.append(arr_in)
        return arr_out
      
      # Runtime complexity: O(numRows^2), as it is iterating a list of size numRows in a nested 2 layer loop.
      # Space Complexity: Same as runtime, as the function is creating and returning a 2D list.
