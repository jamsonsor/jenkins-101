import fire

def hello(name="World"):
  return "Hello %s!" % name

def bye(name="User"):
  return "Bye %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
  fire.Fire(bye)