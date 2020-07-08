bicycles = ['trek', 'cannondale', 'redline', 'INGA', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[1].title())

print(bicycles[-1].upper())
print(bicycles[-2].islower())

message: str = f"My first bicycle was a {bicycles[-3].title()}."
print(message)
