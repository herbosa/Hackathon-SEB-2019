from keras.models import model_from_json
from VectorMaker import *

TASKS = [
    "Backend",
    "Frontend",
    "SystemProgramming",
    "GameDevelopment",
    "SystemAdministration",
    "Scripting",
    "DevOps",
    "Mobile"
]
class AI :
    def __init__(self) :
        json_file = open('../data/ai_tasks_type_json.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        self.model = model_from_json(loaded_model_json)
        self.model.load_weights("../data/ai_tasks_type.h5")

    def predict(self, content) :
        vect = VectorMaker()
        mat = vect.VectorFromChars(content, 600, 1)
        pred = self.model.predict(np.array([mat]))
        arg = np.argmax(pred[0])
        print(content, '=', TASKS[arg - 1])
        return (TASKS[arg - 1])


if __name__ == '__main__' :
    ai = AI()

    ai.predict("Can you accept the invitation on November the 12 at 7:55p.m for the project (my web server), are you agree with that ?")
    ai.predict("I want an appointment on October the 4 at 11:27p.m to talk about reactJS.")
    ai.predict("I organized a meeting on August the 4 at 10:46p.m for a meeting concerning vueJS.")
    ai.predict("I invited you on January the 17 at 7:40a.m about C++, are you open ?")
