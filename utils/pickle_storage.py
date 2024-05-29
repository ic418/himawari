import pickle, os

class InstantFileStorage:
    def __init__(self, folder, name):
        self.name = name
        self.folder = folder
        self.filename=os.path.join(self.folder,self.name)
        if not self.load_array():
            self.save_array([])
    def save_array(self, array):
        with open(self.filename, 'wb') as file:
            pickle.dump(array, file)

    def load_array(self):
        try:
            with open(self.filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            print(f"File {self.filename} not found.")
            return None





if __name__ == "__main__":
    storage = InstantFileStorage(r'C:\ZY\Projects\himawari\utils','array_data.pkl')
    array_to_save=storage.load_array()
    print(len(array_to_save))