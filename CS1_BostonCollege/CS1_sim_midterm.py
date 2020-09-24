def pass_course(*args):

    average = sum(args)/3

    if average >= 6:
        return "Passed course"
    else:
        return "Failed course"

pass_course(1.0, 9.9, 5.0)
pass_course(7.0, 9.9, 5.0)
