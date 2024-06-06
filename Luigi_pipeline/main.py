import luigi
import os
from tasks.track_info_fetch import fetch_track_info

if __name__ =="__main__":
    # luigi.run(['fetch_track_info', '--local-scheduler'])
    try:
        os.remove('.cache')
    except OSError:
        pass
    luigi.run(['fetch_track_info'])
