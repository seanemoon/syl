import gpiod

BUTTON_PIN = 17
CHIP = "gpiochip4"


def main():
    chip = gpiod.Chip(CHIP)
    button_line = chip.get_line(BUTTON_PIN)
    button_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)

    try:
        while True:
            button_state = button_line.get_value()
            button_pressed = button_state == 0
            if button_pressed:
                print("PRESSED")
            else:
                print("NOT PRESSED")
    finally:
        button_line.release()



if __name__ == "__main__":
    main()
