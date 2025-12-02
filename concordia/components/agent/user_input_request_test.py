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

"""Tests for the UserInputRequest component."""

from absl.testing import absltest
from concordia.components.agent import user_input_request


class UserInputRequestTest(absltest.TestCase):
  """Tests for UserInputRequest component."""

  def test_initial_state(self):
    """Test that component initializes with no input requested."""
    component = user_input_request.UserInputRequest()
    self.assertFalse(component.requires_user_input())
    self.assertFalse(component.was_input_just_received())
    self.assertIsNone(component.get_pending_action())

  def test_request_user_input(self):
    """Test requesting user input."""
    component = user_input_request.UserInputRequest()
    component.request_user_input("test action")

    self.assertTrue(component.requires_user_input())
    self.assertFalse(component.was_input_just_received())
    self.assertEqual(component.get_pending_action(), "test action")

  def test_mark_input_received(self):
    """Test marking input as received."""
    component = user_input_request.UserInputRequest()
    component.request_user_input("test action")
    component.mark_input_received()

    self.assertFalse(component.requires_user_input())
    self.assertTrue(component.was_input_just_received())
    self.assertEqual(component.get_pending_action(), "test action")

  def test_clear_request(self):
    """Test clearing the request state."""
    component = user_input_request.UserInputRequest()
    component.request_user_input("test action")
    component.mark_input_received()
    component.clear_request()

    self.assertFalse(component.requires_user_input())
    self.assertFalse(component.was_input_just_received())
    self.assertIsNone(component.get_pending_action())

  def test_get_state(self):
    """Test getting component state."""
    component = user_input_request.UserInputRequest()
    component.request_user_input("test action")

    state = component.get_state()
    self.assertEqual(state['requested_input'], True)
    self.assertEqual(state['input_received'], False)
    self.assertEqual(state['pending_action'], "test action")

  def test_set_state(self):
    """Test setting component state."""
    component = user_input_request.UserInputRequest()

    state = {
        'requested_input': True,
        'input_received': True,
        'pending_action': "restored action",
    }
    component.set_state(state)

    self.assertFalse(component.requires_user_input())
    self.assertTrue(component.was_input_just_received())
    self.assertEqual(component.get_pending_action(), "restored action")

  def test_get_and_set_state_roundtrip(self):
    """Test that get_state and set_state are inverses."""
    component_a = user_input_request.UserInputRequest()
    component_a.request_user_input("action 1")
    component_a.mark_input_received()

    state_a = component_a.get_state()

    component_b = user_input_request.UserInputRequest()
    component_b.set_state(state_a)
    state_b = component_b.get_state()

    self.assertEqual(state_a, state_b)
    self.assertEqual(
        component_a.requires_user_input(),
        component_b.requires_user_input()
    )
    self.assertEqual(
        component_a.was_input_just_received(),
        component_b.was_input_just_received()
    )
    self.assertEqual(
        component_a.get_pending_action(),
        component_b.get_pending_action()
    )

  def test_multiple_requests(self):
    """Test that new requests override previous ones."""
    component = user_input_request.UserInputRequest()

    component.request_user_input("action 1")
    self.assertEqual(component.get_pending_action(), "action 1")

    component.request_user_input("action 2")
    self.assertEqual(component.get_pending_action(), "action 2")
    self.assertTrue(component.requires_user_input())

  def test_set_state_with_missing_keys(self):
    """Test that set_state handles missing keys gracefully."""
    component = user_input_request.UserInputRequest()

    # Set state with empty dict
    component.set_state({})

    self.assertFalse(component.requires_user_input())
    self.assertFalse(component.was_input_just_received())
    self.assertIsNone(component.get_pending_action())


if __name__ == "__main__":
  absltest.main()
