from heapq import nlargest

def latest(scores):
    ''' Return the most recent score. '''
    return scores[-1]


def personal_best(scores):
    ''' Return the highest score. '''
    return max(scores)


def personal_top_three(scores):
    ''' Return the top 3 high scores. '''
    return nlargest(3, scores)
