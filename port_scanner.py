"""
Basic Port Scanner

"""
import socket, common_ports

def get_open_ports(target, port_range, verbose=False):
    open_ports = []
    start = port_range[0]
    stop = port_range[1]

    try:
      for i in range(start, stop + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        error_code = s.connect_ex((target, i))
        if error_code == 0:
            open_ports.append(i)
        else:
          print(error_code)
        s.close()
      if verbose == False:
        return (open_ports)
      else:
        msg = "Open ports for " + target + "\n" + "PORT" + "     " + "SERVICE"
        for port in open_ports:
          if port < 100:
            spaces = "       "
          elif port >= 100 and port < 1000:
            spaces = "      "
          elif port >= 1000:
            spaces = "     "
          msg += "\n" + str(port) + spaces + common_ports.ports_and_services[port]
        return msg
    except:
      try:
        int(target[0])
        return "Error: Invalid IP address"
      except:
        return "Error: Invalid hostname"