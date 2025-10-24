print("COLLECTING FAVORITE ANIME PROGRAM")
q1 = input("Enter the students name ---->")
list = []
while True:
    q2 = input("Enter the title of an anime (or type 'exit' to finish):  ")
    if q2.lower() == 'exit':
            print("The program has been stop")
            break
    else :
        if q2:
            list.append(q2)
            print(f'{q2}, has been added to your anime list')
            continue
print("You have exited the anime entry program.")
print(f"Hi {q1}, your anime list include:")
for each_anime in list:
    print(f'-{each_anime}')

