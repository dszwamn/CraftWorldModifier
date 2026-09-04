"""Offline regression checks for helpers that must not touch game memory."""

import importlib.util
from pathlib import Path
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = PROJECT_ROOT / "craft_web_v1.0.py"
SPEC = importlib.util.spec_from_file_location("craft_web_v1_0_test", SOURCE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PureHelperTests(unittest.TestCase):
    def test_merge_config_keeps_defaults_and_merges_nested_values(self):
        defaults = {"nested": {"one": 1, "two": 2}, "stable": True}
        user = {"nested": {"two": 20}, "custom": "saved"}

        merged = MODULE._merge_config(defaults, user)

        self.assertEqual({"one": 1, "two": 20}, merged["nested"])
        self.assertTrue(merged["stable"])
        self.assertEqual("saved", merged["custom"])
        self.assertEqual({"one": 1, "two": 2}, defaults["nested"])

    def test_update_version_tuple_is_stable_for_short_and_prefixed_versions(self):
        self.assertEqual((1, 0, 0, 0), MODULE.Api._update_version_tuple("v1"))
        self.assertEqual((1, 11, 9, 0), MODULE.Api._update_version_tuple("1.11.009"))
        self.assertIsNone(MODULE.Api._update_version_tuple("release"))

    def test_32bit_pointer_guard_accepts_upper_user_space_addresses(self):
        # The game is a 32-bit process.  Heap pointers above 2 GB are valid
        # under WOW64 and must not be discarded as signed negative values.
        self.assertTrue(MODULE._is_plausible_32bit_pointer(0x80001000))
        self.assertTrue(MODULE._is_plausible_32bit_pointer(0xE0001000))
        self.assertFalse(MODULE._is_plausible_32bit_pointer(0))
        self.assertFalse(MODULE._is_plausible_32bit_pointer(0xFFF00000))

    def test_32bit_pointer_guard_normalizes_signed_input(self):
        self.assertTrue(MODULE._is_plausible_32bit_pointer(-2147479552))
        self.assertFalse(MODULE._is_plausible_32bit_pointer(None))

    def test_update_path_rejects_traversal_and_absolute_values(self):
        self.assertEqual("config/marks.json", MODULE.Api._update_safe_rel("config\\marks.json"))
        self.assertEqual("", MODULE.Api._update_safe_rel("../craft_web_v1.0.py"))
        self.assertEqual("", MODULE.Api._update_safe_rel("C:/temp/unsafe.py"))
        self.assertEqual("", MODULE.Api._update_safe_rel("/tmp/unsafe.py"))

    def test_startup_defers_installed_game_metadata_scan(self):
        self.assertEqual({}, MODULE.GAME_RESOURCE_TRANSLATIONS)
        self.assertEqual(set(), MODULE.GAME_RESOURCE_IDS)
        self.assertEqual({}, MODULE.CREATURE_DEFINITION_HEALTH)

    def test_api_instances_do_not_share_runtime_locks_or_caches(self):
        first = MODULE.Api()
        second = MODULE.Api()

        first.locks["gold"] = True
        first._timer_locks["countdown"]["enabled"] = True
        first._gold_economy_events.append({"source": "test"})

        self.assertFalse(second.locks["gold"])
        self.assertFalse(second._timer_locks["countdown"]["enabled"])
        self.assertEqual([], second._gold_economy_events)


if __name__ == "__main__":
    unittest.main()
