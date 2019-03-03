import subprocess
import json
from pathlib import Path

def ffprobe_sync(filein: Path) ->dict:
    """ get media metadata """
    meta = subprocess.check_output(['ffprobe', '-v', 'warning','-print_format',
                                    'json','-show_streams','-show_format',
                                    str(filein)],universal_newlines=True)

    return json.loads(meta)
