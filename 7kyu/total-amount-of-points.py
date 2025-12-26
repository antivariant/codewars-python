def points(games):
    return sum([3 if us>vs else 0 if us<vs else 1 for us, vs in (map(int,score.split(":")) for score in games)])
