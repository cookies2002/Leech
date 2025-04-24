from mega import Mega  # Import the correct Mega class

# Initialize Mega instance
mega = Mega()

# Login using your MEGA credentials
m = mega.login('markusmarwin2002@gmail.com', 'Marwin2002@')

# Now you can interact with the MEGA account, for example:
files = m.get_files()  # List the files in the MEGA account
print(files)
