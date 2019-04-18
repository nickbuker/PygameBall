class Ball:

    def __init__(self, x, y, speed_x, speed_y, color, width=40, height=40):
        """

        Parameters
        ----------
        x
        y
        speed_x
        speed_y
        color
        """
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color
        self.width = width
        self.height = height

    def update_speed_x(self, speed_x):
        """

        Parameters
        ----------
        speed_x

        Returns
        -------
        None
        """
        self.speed_x = speed_x
        return

    def update_speed_y(self, speed_y):
        """

        Parameters
        ----------
        speed_y

        Returns
        -------
        None
        """
        self.speed_y = speed_y
        return

    def update_position(self):
        """

        Returns
        -------
        None
        """
        self.x += self.speed_x
        self.y += self.speed_y
        return


