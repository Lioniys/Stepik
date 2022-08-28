class Data:
    def __init__(self,data,ip) -> None:
        self.data = data
        self.ip = ip
        pass


class Server:
    counter_server = 1
    
    def __new__(cls):
        cls.counter_server += 1
        return super().__new__(cls)

    def __init__(self) -> None:
        self.buffer = []
        self.ip = self.counter_server
        self.router = None
        pass

    def send_data(self,data):
        if self.ip in self.router.servers_ip:
            self.router.buffer.append(data)
        pass

    def get_data(self):
        a = self.buffer[:]
        self.buffer.clear()
        return a
        

    def get_ip(self):
        return self.ip        


class Router:
    def __init__(self) -> None:
        self.buffer = []
        self.servers_ip = {}
        pass
    
    def link(self,server):
        self.servers_ip[server.ip] = server
        server.router = self
        pass
    
    def unlink(self,server):
        self.servers_ip.pop(server.ip)
        pass
    
    def send_data(self):
        for x in self.buffer:
            if x.ip in self.servers_ip:
                self.servers_ip[x.ip].buffer.append(x)
        self.buffer.clear()
        pass