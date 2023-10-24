"""
The probability that it will rain tomorrow is dependent on whether
or not it is raining today and whether or not it rained yesterday.

If it rained yesterday and today, there is a 20% chance it will rain tomorrow.
If it rained one of the days, there is a 60% chance it will rain tomorrow.
If it rained neither today nor yesterday, there is a 20% chance it will rain tomorrow.

Given that it is raining today and that it rained yesterday, write a function rain_days
to calculate the probability that it will rain on the nth day after today.
"""

from typing import Tuple

FORECAST_2_RAIN = 0.2
FORECAST_1_RAIN = 0.6
FORECAST_0_RAIN = 0.2

STATE_PROBABILITIES = dict({(True, True): 0,
                            (True, False): 0,
                            (False, True): 0,
                            (False, False): 0})
STATE_TRANSITION = dict({(True, True): [(True, True), (True, False)],
                        (True, False): [(False, True), (False, False)],
                        (False, True): [(True, True), (True, False)],
                        (False, False): [(False, True), (False, False)]})
TRANSITION_PROBABILITIES = dict({(True, True): [FORECAST_2_RAIN, 1 - FORECAST_2_RAIN],
                                 (True, False): [FORECAST_1_RAIN, 1 - FORECAST_1_RAIN],
                                 (False, True): [FORECAST_1_RAIN, 1 - FORECAST_1_RAIN],
                                 (False, False): [FORECAST_0_RAIN, 1 - FORECAST_0_RAIN]})


def rain_days_archaic(yesterday_today_rain: Tuple[bool, bool], n: int) -> float:
    """

    :param yesterday_today_rain:
    :param n:
    :return:
    """

    state = STATE_PROBABILITIES.copy()
    state.update({yesterday_today_rain: 1})  # deterministic initial state (we know what happened)

    for _ in range(n):

        # updating transition probabilities
        updated_trans = TRANSITION_PROBABILITIES.copy()
        for s, p in updated_trans.items():
            updated_trans.update({s: [state[s] * p[0], state[s] * p[1]]})

        # updating state probabilities
        updated_state = STATE_PROBABILITIES.copy()
        for s, p in state.items():
            for new_s, new_p in zip(STATE_TRANSITION[s], updated_trans[s]):
                updated_state.update({new_s: updated_state[new_s] + new_p})

        state = updated_state.copy()

    return state[(True, True)] + state[(False, True)]  # probability of rain in n days


def rain_days_markov(n: int) -> float:
    """
    Adapted from InterviewQuery solutions

    :param n: lead time
    :return: rain forecast probability, n days ahead
    """
    import numpy as np
    from numpy.linalg import matrix_power

    m = np.zeros((4, 4))
    m[0, 0] = 0.2
    m[0, 1] = 0.8
    m[1, 2] = 0.6
    m[1, 3] = 0.4
    m[2, 0] = 0.6
    m[2, 1] = 0.4
    m[3, 2] = 0.2
    m[3, 3] = 0.8
    m = matrix_power(m, n)
    rain_prob = m[0, 0] + m[0, 2]
    return rain_prob


print(rain_days_archaic((True, True), 14))
print(rain_days_markov(14))