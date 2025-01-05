"""
File:    the_internet.py
Author:  SETH LESLIE
Date:    11/25/24
Description:
  This program is meant to simulate creating and connecting to servers on the internet.
"""

"""
This function starts the program.
"""


def the_internet():

    the_internet = {}

    current_server = ""

    user_input = input("What would you like to do first? >> ")

    #The user's input is split and the functions are carried out based on the first index of
    #the input.
    while user_input != "quit":

        input_split = user_input.split()

        command_name = input_split[0]

        if command_name == "create-server":
            if len(input_split) != 3:
                print("Please enter the full command for creating a server.")
            elif input_split[2] in the_internet.values():
                print("There is already a server with this IP address.")
            else:
                the_internet = create_server(the_internet, input_split[1], input_split[2])

        elif command_name == "create-connection":
             if len(input_split) != 4:
                print("Please enter the full command for create-connection.")
             else:
                 the_internet = create_connection(the_internet, input_split[1], input_split[2], input_split[3])
        elif command_name == "set-server":
            if len(input_split) != 2:
                print("Please enter the full command for setting a server.")
            else:
                current_server = set_server(the_internet, input_split[1])

        elif command_name == "ping":

            if current_server == "":
                print("Please set a server before pinging.")

            elif len(input_split) != 2:
                print("Please enter the full command for pinging a server.")

            elif not connection_check(the_internet, current_server, input_split[1]):
                print("Unable to ping", input_split[1])

            else:
                ping_server(the_internet, current_server, input_split[1])

        elif command_name == "traceroute":
            if current_server == "":
                print("Please set a server before using traceroute.")

            elif len(input_split) != 2:
                print("Please enter the full command for using traceroute.")

            elif not connection_check(the_internet, current_server, input_split[1]):
                print("Unable to trace route to", input_split[1])

            else:
                print("Tracing route to", input_split[1])
                traceroute(the_internet, current_server, input_split[1])

        elif command_name == "ip-config":
            if current_server == "":
                print("Please set a server before using ip-config.")

            else:
                ip_config(the_internet, current_server)

        elif command_name == "display-servers":
            display_servers(the_internet)

        else:
            print("Please enter a valid command.")

        user_input = input("What would you like to do next? >> ")


"""
CREATE SERVER:
create-server[server_name] [ip_v4_address]

-Adds a server name and its IP address to a dictionary.
-An appropriate IP address must be implemented.
-If there is a duplicate, ignore it.

:param the_internet: The dictionary containing all keys and values related to the servers.
:param server_name: The name of the server being created.
:param ip_v4_address: The ipv4 address that will relate to the server being created.
:return new_internet: The modified version of the dictionary that gets passed.
"""


def create_server(the_internet, server_name, ip_v4_address):

    new_internet = the_internet
    server_title = str(server_name)
    ip_v4_address_split = list(ip_v4_address.split("."))

    #Each number in the IP address is checked, if one of the numbers is larger than 255,
    #then the IP address is invalid
    for number in ip_v4_address_split:
        if int(number) > 255:
            print("One of the numbers in your IP address is too high to be assigned.")
            return new_internet

    #If the server is already in the internet, only the ip address is changed for that server.
    if server_name in the_internet:
        new_internet[server_title + " IPv4 address"] = ip_v4_address
        print("The server with the name", server_name, "has been updated with the ip", ip_v4_address)
    else:
        #The server that the user chooses to create is set as a key in a dictionary with an
        #empty list as its value
        new_internet[server_name] = []

        #The IP address of the server is also given its own key.
        new_internet[server_title + " IPv4 address"] = ip_v4_address

        print("A server with the name", server_name, "was created at ip", ip_v4_address)


    return new_internet


"""
CREATE CONNECTION:
create-connection [server_1] [server_2] [connect_time]

-Connect two servers together
-The connection_time is in milliseconds
-The connection should be in both directions
-Make sure that the two servers are not already connected
-Ensure that both servers exist before connecting

:param the_internet: The dictionary of all servers and related information.
:param server_1: The name of the first server to be connected.
:param server_2: The name of the second server to be connected.
:param connect_time: The connection time associated with the respective server.
:return new_internet: The modified version of the internet with updated connections.
"""


def create_connection(the_internet, server_1, server_2, connect_time):
    new_internet = the_internet
    server_1_name = str(server_1)
    server_1_ipv4_address = the_internet[server_1_name + " IPv4 address"]
    server_2_name = str(server_2)
    server_2_ipv4_address = the_internet[server_2_name + " IPv4 address"]
    new_internet[server_1_name + " connection time"] = 0
    new_internet[server_2_name + " connection time"] = 0
    new_internet[server_1_ipv4_address + " connection time"] = 0
    new_internet[server_2_ipv4_address + " connection time"] = 0

    #If the servers have not been created or the connections have already been made,
    #a statement is printed telling the user so.
    if server_1 not in new_internet or server_2 not in new_internet:
        print("One or both of your servers do not exist.")


    elif server_2 in new_internet[server_1] and server_1 in new_internet[server_2]:

        print("There is already a connection between these two servers.")

    #If the previous if statements are false, the servers are added to each other's lists.
    else:
        new_internet[server_1].append(server_2)
        new_internet[server_1_name + " connection time"] += int(connect_time)
        new_internet[server_1_ipv4_address + " connection time"] += int(connect_time)
        new_internet[server_2].append(server_1)
        new_internet[server_2_name + " connection time"] += int(connect_time)
        new_internet[server_2_ipv4_address + " connection time"] += int(connect_time)
        print("A server with name", server_1, "is now connected to", server_2)


    return new_internet

"""
CONNECTION CHECK:
This function checks the connection between the two servers before doing ping or traceroute.

:param the_internet: The current dictionary with all servers and respective info.
:param starting_server: The current server that is set.
:param destination_server: The server that is being looked for.
:param visited_servers: A list of all previous servers that have been visited.
:return True: If the connection is succsessful.
:return False: If the connection is not successful.
"""


def connection_check(the_internet, starting_server, destination_server, visited_servers = []):

    #Similar to the ping and traceroute functions; checks if there is a successful connection
    #between servers
    for value in the_internet[starting_server]:

        if value not in visited_servers:
            connection_check(the_internet, value, destination_server, visited_servers + [value])
            if value == destination_server or the_internet[str(value) + " IPv4 address"] == destination_server:
                return True
            if connection_check(the_internet, value, destination_server, visited_servers + [value]):
                return True
        else:
            return False


"""
SET SERVER:
set-server [server_name or ip_v4_address]

-Sets our current place on the internet
-Ensure that the server exists before setting it

:param the_internet: The dictionary of all current server configurations.
:param server_name: The name of the server that will be set to the current server.
:return current_server: The server that the user chooses to set to.
:return None: If the server name is not found in the dictionary, None is returned.
"""


def set_server(the_internet, server_name):
    #If the server that the user wishes to set to exists within the internet dictionary,
    #the current server is set to the requested server.
    if server_name in the_internet:
        current_server = server_name
        print("Server", server_name, "selected.")
        return current_server
    else:
        print("The server you chose has not yet been created.")
        return None


"""
PING (This must use recursion):
ping [server_name or ip_v4_address]

-Pings either the server or the IP address.
-Prints out the amount of time it takes for a trip to that server.
-If there is no path, tell the user.
-If the current server isn't set, don't run the command.

:param the_internet: The current configuration for the internet dictionary.
:param starting_server: The current server where the path for ping will start.
:param destination_server: The server that is being sought after.
:param visited_servers: All previous servers that have been visited.
:param connect_time_total: The accumulated connection time.
:return value: The destination server.
"""


def ping_server(the_internet, starting_server, destination_server, visited_servers = [], connect_time_total = 0):

    #For each value within the starting server's list, the values of that value as a key are checked
    #for the destination server.


    if starting_server == destination_server or the_internet[str(starting_server) + " IPv4 address"] == destination_server:
        print("Reply from", destination_server, "time = ", connect_time_total, "ms")
        return destination_server

    else:
        for value in the_internet[starting_server]:


            if value not in visited_servers:

                ping_server(the_internet, value, destination_server, visited_servers + [value], connect_time_total = connect_time_total + the_internet[str(starting_server) + " connection time"])

"""
TRACEROUTE (This must use recursion):
traceroute [server_name or ip_v4_address]

-Finds a path from the start server to the destination.
-Shows the path taken to get to the destination and the time it takes to hop from server to server.
-If the current server is not set, do not run this command.

:param the_internet: The current configuration for the internet.
:param starting_server: The starting server where the traceroute will start.
:param destination_server: The destination server where the traceroute will end.
:param visited_servers: The servers that were visited previously.
:param current_connection_time: The connection time related to the current server being looked at.
:return value: The destination server
"""


def traceroute(the_internet, starting_server, destination_server, visited_servers = [], current_connection_time = 0):
    instance_number = 0

    #Similar to ping, except that each server and their respective connect time are shown individually

    if starting_server == destination_server or the_internet[str(starting_server) + " IPv4 address"] == destination_server:
         for server in visited_servers:
                    instance_number += 1
                    print(instance_number, the_internet[str(server) + " connection time"], the_internet[str(server) + " IPv4 address"], server)



    else:

        for value in the_internet[starting_server]:

            if value not in visited_servers:

                traceroute(the_internet, value, destination_server, visited_servers + [value], current_connection_time = the_internet[str(value) + " connection time"])



"""
IP CONFIG:
ip-config

-Returns our current IP address and server name.
-Tells us where we are in the network.

:param the_internet: The current dictionary with all servers and configurations.
:param current_server: The current server that is set.
"""


def ip_config(the_internet, current_server):
    #For only the keys in the dictionary that have the current server name and the string " IPv4 address,"
    #print the respective server and ipv4 address
    for server in the_internet:
        if server == str(current_server) + " IPv4 address":
            print(current_server, the_internet[str(current_server) + " IPv4 address"])


"""
DISPLAY SERVERS:
display-servers

-Looks at all of the different servers and their connections.

:param the_internet: The dictionary with the current servers and their configurations.
"""


def display_servers(the_internet):

    #Display each key and their respective values in the dictionary
    for item in the_internet:
        print(item, the_internet[item])











if __name__ == '__main__':
    the_internet()
