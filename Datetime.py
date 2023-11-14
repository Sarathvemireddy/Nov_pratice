import datetime

def print_current_date(format="%a %b %d %H:%M:%S %Z %Y"):

  now = datetime.datetime.now()
  print(now.strftime(format))

if __name__ == "__main__":
  print_current_date()
