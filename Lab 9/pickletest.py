import pickle

def main():
    again = "y"
    output_file = open('info.dat', 'wb')

    while again.lower() == 'y':
        save_data(output_file)

        again = input("Enter more data?")

    output_file.close()

    
# save_data gets data, stores in dictionary, and pickles
def save_data(file):
    person = {}

    person['name'] = input("Name: ")
    person['age'] = int(input("Age: "))
    person['weight'] = float(input("Weight: "))

    pickle.dump(person, file)

main()
    
