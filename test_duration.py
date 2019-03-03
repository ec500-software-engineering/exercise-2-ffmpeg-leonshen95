import ffprobe as probe
import encode as convert
from pytest import approx

def test_duration():
    fnin = 'realshort.mp4'
    fnout = 'realshort480_test.mp4'

    orig_meta = probe.ffprobe_sync(fnin)
    orig_duration = float(orig_meta['streams'][0]['duration'])

    convert.main()

    meta_480 = probe.ffprobe_sync(fnout)
    duration_480 = float(meta_480['streams'][0]['duration'])

    assert orig_duration == approx(duration_480)
