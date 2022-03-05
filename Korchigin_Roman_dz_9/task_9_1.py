import time


# time.sleep(), позволяет отсрочить выполнение вызываемого потока на указанное количество секунд.


class TrafficLight:
    _colors = {'red': 4, 'yellow': 2, 'green': 3}

    def running(self):
        for color, switch_time in self._colors.items():
            self._colors = color

            print(f"{self._colors} "
                  f" {switch_time} сек")

            time.sleep(switch_time)


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
