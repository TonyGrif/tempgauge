class Core:
    """Class containing data on a CPU core.

    Attributes:
        core_num (int): The CPU core number.
        readings (list): List of tuples of CPU readings.
    """

    def __init__(self, c_num: int) -> None:
        """Constructor for the Core class

        Parameters:
            c_num (int): The CPU core number.
            readings (list): List of tuples containing readings.
        """
        self.core_num = c_num
        self.readings = []

    @property
    def core_num(self) -> int:
        """
        Get the core number of this Core.

        Returns:
            num (int): The core number.
        """
        return self._core_num

    @core_num.setter
    def core_num(self, num: int) -> None:
        """
        Set the core number of this Core.

        Parameters:
            num (int): The core number.

        Raises:
            AttributeError: If negative number is passed.
        """
        if num < 0:
            raise AttributeError("Negative core number is not allowed")
        self._core_num = num

    def add_reading(self, point: tuple) -> None:
        """
        Add a new reading to the reading list.

        Parameters:
            point (tuple): Tuple containing (time, temperature) readings.
        """
        self.readings.append(point)
