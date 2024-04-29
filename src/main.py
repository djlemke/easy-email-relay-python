from gui import GUI
from server import Server

if __name__ == "__main__":
    view = GUI()
    server = Server()

    view.rebind_button("start", server.start)
    view.rebind_button("stop", server.stop)
    view.start()
