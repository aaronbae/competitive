"""
Pizza.py
===========================================================
The the data structure to easily access the Pizza object.
"""

class Pizza:
    def __init__(self, file_name):
        """
        The constructor

        Parameters
        ----------
        file_name
            A string indicating the name of the file that has the input file.
        """
        input_file = open(file_name, "r")

        # Extracting condition information
        conditions = input_file.readline().split()
        self.row = int(conditions[0])
        self.col = int(conditions[1])
        self.min_ingredient = int(conditions[2])
        self.max_cell_per_slice = int(conditions[3])

        # printing the rest of the input file
        self.ingredient_map = [line[:-1] for line in input_file]

        # variable to keep track of slices
        self.loc_to_index = [[0 for i in range(self.col)] for j in range(self.row)]
        self.index_to_locs = {} # key: index - (int), value: (r1, r2, c1, c2) - (tuple)
        self.next_slice_index = 1

    def ingredient_map():
        """
        The access method to return a copy of the current ingredient_map
        """
        return self.ingredient_map[:][:]

    # returns either 'T' or 'M'
    def check_content(self, row, col):
        """
        The access method to return the content of the ingredient at that grid

        Parameters
        ----------
        row
            the integer representation of the row where the user wishes to query
        col
            the integer representation of the column where the user wishes to query
        """
        print(self.ingredient_map[row][col])

    # prints the string representation of the pizza status
    def print(self):
        """
        The client method to print out the current status of the ingredient map
        """
        print(str(self.row) +" x "+str(self.col) + "\t\tMin: "+str(self.min_ingredient)+"\t\tMax: "+str(self.max_cell_per_slice))
        for index, row in enumerate(self.ingredient_map):
            print(row+'\t\t'+', '.join(str(x) for x in self.loc_to_index[index]))

    # Cuts a slice
    def slice(self, r1, r2, c1, c2):
        """
        The mutator method to create a new slice of the Pizza

        Parameters
        ----------
        r1
            the row coordinate of the top-left corner of the pizza
        r2
            the row coordinate of the bottom-right corner of the pizza
        c1
            the column coordinate of the top-left corner of the pizza
        c2
            the column coordinate of the bottom-right corner of the pizza
        """
        try:
            m_count = 0
            t_count = 0

            # Condition #1: In bounds
            if r1 < 0 or r1 >= self.row or r2 < 0 or r2 >= self.row or c1 < 0 or c1 >= self.col or c2 < 0 or c2 >= self.col:
                raise Exception('Coordinates out of bounds. The input was: {}'.format((r1, r2, c1, c2)))

            # Condition #2: Max Cells per Slice
            if (max(r1, r2) - min(r1, r2) + 1) * (max(c1, c2) - min(c1, c2) + 1) > self.max_cell_per_slice:
                raise Exception('Too big of a slice. Must be at most '+ str(self.max_cell_per_slice) +'. The input was: {}'.format((r1, r2, c1, c2)))
            for i in range(min(r1, r2), max(r1, r2) + 1):
                for j in range(min(c1, c2), max(c1, c2) + 1):
                    # Condition #3: Cannot slice one cell into two different slices
                    if self.loc_to_index[i][j] != 0:
                        raise Exception('Already Occupied Slices. The conflicting location is: {}'.format((i,j)))
                    elif self.ingredient_map[i][j] == "M":
                        m_count += 1
                    else: # T
                        t_count += 1
            # Condition #4: Min Mushrooms required
            if m_count < self.min_ingredient:
                raise Exception('Not enough Mushrooms in this slice. The input was: {}'.format((r1, r2, c1, c2)))

            #Condition #5: Min Tomatoes required
            if t_count < self.min_ingredient:
                raise Exception('Not enough Tomatoes in this slice. The input was: {}'.format((r1, r2, c1, c2)))

            # record the slice into var 'index_to_locs'
            self.index_to_locs[str(self.next_slice_index)] = (r1, r2, c1, c2)

            # update the 'loc_to_index'
            for i in range(min(r1, r2), max(r1, r2) + 1):
                for j in range(min(c1, c2), max(c1, c2) + 1):
                    self.loc_to_index[i][j] = self.next_slice_index

            # Success!
            self.next_slice_index += 1
            return 1
        except Exception as error:
            print(repr(error))
            # Failure
            return 0

    # shows the indices of the current slices
    def curr_slices(self):
        """
        The accessor method to return the list of slices that the pizza currently has
        """
        return self.index_to_locs.keys()

    # removes the slices
    def unslice(self, slice_index):
        """
        The mutator method to return the slice back into the available pool of pizza squares

        Parameters
        ----------
        slice_index
            the unique index of the slice to be unsliced
        """
        # invalid slice_index
        if str(slice_index) not in self.index_to_locs:
            print("Slice Index does not exist! " + str(slice_index))
            return 0

        # remove this slice
        r1,r2,c1,c2 = self.index_to_locs.pop(str(slice_index), (-1, -1, -1, -1))

        # update the 'loc_to_index'
        for i in range(min(r1, r2), max(r1, r2) + 1):
            for j in range(min(c1, c2), max(c1, c2) + 1):
                self.loc_to_index[i][j] = 0
        return 1

    # saves the current set of slices to recommended file
    def save_to_file(self, file_name):
        """
        The method creates the output file that the Hash Code scoring function can understand

        Parameters
        -----------
        file_name
            the name of the file that the output should have
        """
        list_of_slice_indices = self.curr_slices()

        # create file
        output_file = open(file_name, 'w')

        # write how many total slice
        output_file.write(str(len(list_of_slice_indices))+"\n")

        # write about each slices
        for i in list_of_slice_indices:
            r1, r2, c1, c2 = self.index_to_locs[str(i)]
            output_file.write("{} {} {} {}\n".format(r1, c1, r2, c2))
        output_file.close()
