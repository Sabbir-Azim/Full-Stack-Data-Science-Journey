import time
class TimeTaken:
 def __enter__(s): s.t=time.time()
 def __exit__(s,*_): print(time.time()-s.t)
with TimeTaken(): time.sleep(0.2)