def student(name, age, tracks, score):
        change_name = str(name)
        change_age = int(age)
        add_track = str(tracks)
        get_score = float(score)
        return(['Bob.change_name = {}'.format(change_name), 'Bob.change_age = {}'.format(change_age), 
                'Bob.add_track = {}'.format(add_track), 'Bob.get_score = {}'.format(get_score)])
student ('peter', 34, 'UI/UX', 53.40)



