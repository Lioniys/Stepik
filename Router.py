class Data:
    def __init__(self, data, ip):
        """
        data - передаваемые данные (строка);
        ip - IP-адрес назначения.
        """
        self.data = data
        self.ip = ip
        

class Server:
    counter_server = 1
    
    def __new__(cls):
        cls.counter_server += 1
        return super().__new__(cls)

    def __init__(self):
        """
        buffer - список принятых пакетов;
        ip - IP-адрес текущего сервера.
        """
        self.buffer = []
        self.ip = self.counter_server
        self.router = None
        
    def send_data(self, data):
        """
        Для отправки информационного пакета data 
        с указанным IP-адресом получателя 
        (пакет отправляется роутеру и
        сохраняется в его buffer)
        """
        if self.ip in self.router.servers_ip:
            self.router.buffer.append(data)
        
    def get_data(self):
        """
        Возвращает список принятых пакетов 
        и очищает входной буфер
        """
        lst = self.buffer[:]
        self.buffer.clear()
        return lst
        
    def get_ip(self):
        """
        Возвращает свой IP-адрес.
        """
        return self.ip        


class Router:
    def __init__(self):
        """
        Для описания работы роутеров в сети
        (в данной задаче полагается один роутер).
        buffer - список для хранения принятых от
        серверов пакетов (объектов класса Data).
        """
        self.buffer = []
        self.servers_ip = {}
        
    def link(self, server):
        """
        Для присоединения сервера 
        (объекта класса Server) 
        к роутеру
        """
        self.servers_ip[server.ip] = server
        server.router = self
        
    def unlink(self, server):
        """
        Для отсоединения сервера 
        (объекта класса Server) 
        от роутера
        """
        self.servers_ip.pop(server.ip)
        
    def send_data(self):
        """
        Для отправки всех пакетов 
        (объектов класса Data) 
        из буфера роутера
        соответствующим серверам 
        (после отправки буфер должен очищаться)
        """
        for x in self.buffer:
            if x.ip in self.servers_ip:
                self.servers_ip[x.ip].buffer.append(x)
        self.buffer.clear()