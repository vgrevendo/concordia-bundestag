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

"""Component for entities that can request user input during simulation."""

from concordia.typing import entity_component


DEFAULT_USER_INPUT_COMPONENT_KEY = '__user_input_request__'


class UserInputRequest(entity_component.ContextComponent):
  """Component that allows entities to request and receive user input.

  This component enables entities to pause the simulation and request input
  from the user. The simulation will exit its run loop when any entity
  requests user input, allowing the caller to provide input and resume.

  The component tracks three pieces of state:
  - Whether input has been requested
  - Whether the requested input has been received
  - The pending action to resolve after input is received
  """

  def __init__(self):
    """Initialize the user input request component."""
    super().__init__()
    self._requested_input = False
    self._input_received = False
    self._pending_action = None

  def requires_user_input(self) -> bool:
    """Check if this entity currently requires user input.

    Returns:
      True if input has been requested but not yet received.
    """
    return self._requested_input and not self._input_received

  def request_user_input(self, pending_action: str) -> None:
    """Request user input and store the action to resolve later.

    This should be called by the entity when it wants to pause the simulation
    and wait for user input. The pending_action will be used to resolve the
    action once input is provided and the simulation resumes.

    Args:
      pending_action: The action string to resolve after user input is received.
    """
    self._requested_input = True
    self._input_received = False
    self._pending_action = pending_action

  def mark_input_received(self) -> None:
    """Mark that user input has been received for this request."""
    self._input_received = True

  def clear_request(self) -> None:
    """Clear the user input request state.

    This should be called after the pending action has been resolved.
    """
    self._requested_input = False
    self._input_received = False
    self._pending_action = None

  def was_input_just_received(self) -> bool:
    """Check if user input was just received and is ready to resolve.

    Returns:
      True if input was requested and has now been received.
    """
    return self._requested_input and self._input_received

  def get_pending_action(self) -> str | None:
    """Get the pending action to resolve.

    Returns:
      The pending action string, or None if no action is pending.
    """
    return self._pending_action

  def get_state(self) -> entity_component.ComponentState:
    """Returns the state of the component.

    Returns:
      A dictionary containing the component's state.
    """
    return {
        'requested_input': self._requested_input,
        'input_received': self._input_received,
        'pending_action': self._pending_action,
    }

  def set_state(self, state: entity_component.ComponentState) -> None:
    """Sets the state of the component.

    Args:
      state: A dictionary containing the component's state.
    """
    self._requested_input = state.get('requested_input', False)
    self._input_received = state.get('input_received', False)
    self._pending_action = state.get('pending_action', None)
