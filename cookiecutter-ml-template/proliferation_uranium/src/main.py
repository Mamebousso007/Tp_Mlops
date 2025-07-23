 
import hydra
from omegaconf import DictConfig
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.datasets import load_iris
#from sklearn.model_selection import train_test_split
#from sklearn.metrics import accuracy_score

@hydra.main(config_path="../configs", config_name="config", version_base=None)
def main(cfg: DictConfig):
    print("Configuration utilisees")
    print(cfg)

if __name__ == "__main__":
    main()