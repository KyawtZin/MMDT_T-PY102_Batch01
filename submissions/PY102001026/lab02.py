"""
Lab 02 — Stack & Queue Practice (4 Questions)

Rules:
- Do NOT use input() or print() in your solutions.
- Implement the functions below exactly with the given names.
- Use stack/queue operations (append/pop for stack; collections.deque for queue is recommended).

Questions:
  Q1) is_balanced_parentheses(s)
  Q2) next_greater_to_right(nums)

  Q3) first_non_repeating(stream)
  Q4) hot_potato(names, k)
"""

from collections import deque


# -------------------------
# Stack Questions (2)
# -------------------------

def is_balanced_parentheses(s: str) -> bool:
    """
    Return True if the string s has balanced brackets: (), {}, [].
    Ignore non-bracket characters.
    """
    # TODO: implement using a stack
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0
    raise NotImplementedError


def next_greater_to_right(nums: list[int]) -> list[int]:
    """
    For each element, find the next greater element to its right.
    If none exists, output -1 for that position.
    """
    # TODO: implement using a stack (monotonic stack)
    result = [-1] * len(nums)
    stack = []

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result
    raise NotImplementedError


# -------------------------
# Queue Questions (2)
# -------------------------

def first_non_repeating(stream: str) -> str:
    """
    Given a stream of lowercase letters, build a result string where each character
    is the first non-repeating character seen so far. If none exists, use '#'.
    """
    # TODO: implement using a queue + counts
    q = deque()
    count = {}
    result = ""

    for ch in stream:
        count[ch] = count.get(ch, 0) + 1
        q.append(ch)

        while q and count[q[0]] > 1:
            q.popleft()

        if q:
            result += q[0]
        else:
            result += '#'

    return result
    raise NotImplementedError


def hot_potato(names: list[str], k: int) -> str:
    """
    Simulate the Hot Potato game.
    """
    # TODO: implement using a queue (deque)
    q = deque(names)

    while len(q) > 1:
        for _ in range(k):
            q.append(q.popleft())
        q.popleft()

    return q[0]
    raise NotImplementedError