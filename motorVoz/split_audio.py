import auditok

# split returns a generator of AudioRegion objects
audio_regions = auditok.split(
    "KIMY__1h.wav", ##inserte audio
    min_dur=4,
    max_dur=8,
    max_silence=1.2,
    energy_threshold=55
)
n = 0
for i, r in enumerate(audio_regions):
    n += 1
    print("Region {i}: {r.meta.start:.3f}s -- {r.meta.end:.3f}s".format(i=i, r=r))
    filename = r.save(f"{n}.wav")
    print("region saved as: {}".format(filename))
