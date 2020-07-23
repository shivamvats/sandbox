from sacred import Experiment

ex = Experiment()

@ex.config
def ExperimentConfig():
    """Config values need to be accessed with a string."""
    name = "Shivam"
    age = 25

class Config():
    """Allows accessing config values as properties."""
    def __init__(self, cfg):
        for key, val in cfg.items():
            setattr(self, key, val)

@ex.automain
def main(_config):
    args = Config(_config)
    print("My name is %s and I am %d years old." %(_config['name'], _config['age']))
    print("My name is %s and I am %d years old." %(args.name, args.age))
