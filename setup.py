from cx_Freeze import setup, Executable

executables = [Executable("CingChecker.py")]

setup(
    name="Cing Checker",
    version = "1.0.0",
    description = 'Program for checking robot Cing sensors',
    author = 'Stanislav Jochman',
    options={"build_exe": {"packages":["serial","webbrowser","time"],
                           "include_files":["16x2.png",
                                            "Battery.png",
                                            "bmp180.png",
                                            "Button.png",
                                            "enc.png",
                                            "Gyro.png",
                                            "lidar.png",
                                            "lightsensor.png",
                                            "oled.png",
                                            "pot.png",
                                            "servoboard.png",
                                            "shinearray.png",
                                            "speaker.png",
                                            "TemperatureSensor.png",
                                            "ultrasonic.png",
                                            "Cing_Checker.config"]}},
    executables = executables

    )
