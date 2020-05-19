import os
import hydra
from experimenting.trainHelper import get_training_params
from omegaconf import DictConfig
import pytorch_lightning as pl
import experimenting
import logging

logging.basicConfig(level=logging.INFO)


@hydra.main(config_path='./confs/train/config.yaml')
def main(cfg: DictConfig) -> None:
    trainer_configuration = get_training_params(cfg)
    model = getattr(experimenting, cfg.training.module)(cfg)
    
    if cfg.load_path:
        print('Loading training')
        model = getattr(experimenting,
                        cfg.training.module).load_from_checkpoint(cfg.load_path)
        
    trainer = pl.Trainer(**trainer_configuration)
    trainer.fit(model)
    trainer.test(model)

    
if __name__ == '__main__':
    main()
    
