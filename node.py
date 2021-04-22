class Node:
    """
    This class creates a node.

    Attributes:
        data : data
    """
    def __init__(self, data):
        """
        The constructor for the Node class.

        Parameters:
            data : data
        """
        self._data = data

    @property
    def data(self):
        """
        This function returns the data of the node.

        Return:
            data : data
        """
        return self._data

    @data.setter
    def data(self, new_data):
        """
        This function sets the data of the node.

        Parameter:
            new_data : data
        """
        self._data = new_data