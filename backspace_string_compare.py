
def backspace_string_compare(s: str, t: str) -> bool:
    """
    LeetCode Backspace String Compare problem (844)

    Given two strings s and t, return true if they are equal when both are typed into empty text
    editors. '#' means a backspace character.
    Note that after backspacing an empty text, the text will continue empty.

    Example 1:
    Input: s = "ab#c", t = "ad#c"
    Output: true
    Explanation: Both s and t become "ac".

    Example 2:
    Input: s = "ab##", t = "c#d#"
    Output: true
    Explanation: Both s and t become "".

    Example 3:
    Input: s = "a#c", t = "b"
    Output: false
    Explanation: s becomes "c" while t becomes "b".

    :param s: string 1
    :param t: string 2
    :return: true if s and t are equal, false otherwise
    """

    def move_backward(q: str, pos: int) -> int:
        # move pointer backward to the next valid character; account for single or consecutive '#'
        pos -= 1
        erase = 0
        while pos > 0 and q[pos] == '#':
            erase += 1
            pos -= 1
        return pos - erase

    # initialization
    equal = True  # to account for empty s and t
    pos_s = move_backward(s, len(s))
    pos_t = move_backward(t, len(t))

    # compare s and t, from last to first character; account for '#' and escape at first difference
    while min(pos_s, pos_t) > -1:
        equal = s[pos_s] == t[pos_t]
        if not equal:
            break
        pos_s = move_backward(s, pos_s)
        pos_t = move_backward(t, pos_t)

    return equal
