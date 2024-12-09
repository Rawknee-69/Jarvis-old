import asyncio
import sys
sys.path.append("")
from Listen import MicExecution
from braininuse import brainy
Data = MicExecution()
Data = str(Data)

if "jarvis tell me" in Data or "tell me" in Data or "question" in Data or "answer" in Data:   
            asyncio.run(brainy(Data))