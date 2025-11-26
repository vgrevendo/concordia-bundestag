# Copyright 2025 DeepMind Technologies Limited.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple counter for tracking simulation steps."""


class StepsCounter:
  """A counter that tracks the number of simulation steps.

  This is a simple wrapper around an integer that supports arithmetic
  operations and comparisons, enabling proper tracking and checkpointing
  of simulation progress.
  """

  def __init__(self, value: int = 0):
    """Initialize the counter with a given value.

    Args:
      value: The initial step count (must be non-negative).
    """
    self.value = max(0, value)

  def __iadd__(self, other):
    """Support in-place addition (+=) operator.

    Args:
      other: An integer or StepsCounter to add.

    Returns:
      Self, for chaining operations.
    """
    if isinstance(other, StepsCounter):
      self.value += other.value
    else:
      self.value += other
    return self

  def __lt__(self, other) -> bool:
    """Support less-than (<) comparison."""
    if isinstance(other, StepsCounter):
      return self.value < other.value
    return self.value < other

  def __le__(self, other) -> bool:
    """Support less-than-or-equal (<=) comparison."""
    if isinstance(other, StepsCounter):
      return self.value <= other.value
    return self.value <= other

  def __gt__(self, other) -> bool:
    """Support greater-than (>) comparison."""
    if isinstance(other, StepsCounter):
      return self.value > other.value
    return self.value > other

  def __ge__(self, other) -> bool:
    """Support greater-than-or-equal (>=) comparison."""
    if isinstance(other, StepsCounter):
      return self.value >= other.value
    return self.value >= other

  def __eq__(self, other) -> bool:
    """Support equality (==) comparison."""
    if isinstance(other, StepsCounter):
      return self.value == other.value
    return self.value == other

  def __int__(self) -> int:
    """Convert to integer for checkpoint callbacks and serialization."""
    return self.value

  def __repr__(self) -> str:
    """Return a developer-friendly string representation."""
    return f'StepsCounter({self.value})'

  def __str__(self) -> str:
    """Return a string representation of the value."""
    return str(self.value)
