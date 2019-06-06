class Ball:

    def __init__(self, x, y, speed_x, speed_y, width=40, height=40):
        """

        Parameters
        ----------
        x
        y
        speed_x
        speed_y
        """
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.width = width
        self.height = height
        self.color_state = 0
        self.colors = [
            (255, 0, 0),
            (255, 87, 51),
            (255, 255, 0),
            (50, 205, 50),
            (20, 144, 255),
            (138, 43, 226)
        ]

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

    def set_color_state(self):
        """

        Returns
        -------
        None
        """
        if self.color_state < len(self.colors) - 1:
            self.color_state += 1
        else:
            self.color_state = 0
        return


