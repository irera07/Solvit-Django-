Name="TWIZEYEYESU"
for c in Name:
    print(c)
for i in range(0, 21):
    if i%2==0:
        print("even")
    else:
        print("odd")
    
colors=[{
    "color":"red", "msg": "Stop"}, 
    {
    "color":"green", "msg": "Go"},
    {
    "color":"yellow", "msg": "Slow down"}]
color=input("Enter a color: ").lower()
m=list()
for c in colors:
    m.append(c.get("color"))
    if c.get("color") == color:
       print(c.get("msg")) 
       break
    else:
        print("Invalid color")
        break
