from typing import TypedDict
import typing
import fastf1
import fastf1.plotting
import pandas as pd
import numpy as np

class Session(TypedDict):
    race: fastf1.core.Session
    fp2: fastf1.core.Session
    fp1: fastf1.core.Session
    fp3: Union[fastf1.core.Session | None]
    quali: Union[fastf1.core.Session | None]
    sprint_quali: Union[fastf1.core.Session | None]
    sprint: Union[fastf1.core.Session | None]

def fastify_set_up(year: int, gp: str, event: str) -> Dict[Session]:
    ff1.Cache.enable_cache('cache')

if __name__ == "__main__":
   pass 
