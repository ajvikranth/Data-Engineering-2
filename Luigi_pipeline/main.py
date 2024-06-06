import luigi
import os
from tasks.track_info_fetch import fetch_track_info

if __name__ =="__main__":
    
    try:
        os.remove('.cache')
    except OSError:
        pass
    # luigi.run(['fetch_track_info'])
    luigi.run(['fetch_track_info', '--local-scheduler'])
