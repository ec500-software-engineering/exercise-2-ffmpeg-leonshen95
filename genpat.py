import pytest  # pytest >= 3.9 for tmp_path
import subprocess

@pytest.fixture
def genpat(tmp_path):

	vidfn = tmp_path / 'realshort.mp4'

	subprocess.check_call(['ffmpeg', '-v', 'warning', '-f',
						   'lavfi', '-i', 'smptebars', '-t', 5., str(vidfn)])
	return vidfn
