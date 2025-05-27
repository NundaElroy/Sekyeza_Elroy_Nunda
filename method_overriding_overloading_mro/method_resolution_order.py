#Example one LOGGING
class FileLogger:
    def log(self):
        print("Logging to file")

class DatabaseLogger:
    def log(self):
        print("Logging to database")

class AppLogger(FileLogger, DatabaseLogger):
    pass

logger = AppLogger()
logger.log()  #  Logs to file


#Example 2 
# UI button System
class Clickable:
    def action(self):
        print("Clicked!")

class Hoverable:
    def action(self):
        print("Hovered!")

class Button(Clickable, Hoverable):
    pass

btn = Button()
btn.action()  # 👉 "Clicked!"
