#!/usr/bin/env python3
"""
Unit tests for Instructabot Engineering Notebook CLI & Evaluator
"""

import unittest
import tempfile
import shutil
from pathlib import Path
from agent.notebook.cli import get_lab_file, parse_notebook_status, init_lab, verify_lab, NOTEBOOKS_DIR

class TestNotebookCLI(unittest.TestCase):

    def test_get_lab_file(self):
        file_0 = get_lab_file(0)
        self.assertIsNotNone(file_0)
        self.assertEqual(file_0.name, "lab-00-systems-decomposition-log.md")

        file_1 = get_lab_file(1)
        self.assertIsNotNone(file_1)
        self.assertEqual(file_1.name, "lab-01-nightlight-log.md")

        file_str = get_lab_file("lab-02")
        self.assertIsNotNone(file_str)
        self.assertEqual(file_str.name, "lab-02-intersection-controller-log.md")

    def test_parse_status_template(self):
        file_1 = get_lab_file(1)
        status = parse_notebook_status(file_1)
        self.assertTrue(status["exists"])
        self.assertEqual(status["status"], "Not Started")
        self.assertGreater(status["checks_total"], 0)

    def test_init_and_verify_cycle(self):
        # Create a temp copy of lab-01
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir) / "lab-01-test-log.md"
            shutil.copy2(get_lab_file(1), tmppath)

            # Test init_lab on temp file
            init_res = init_lab(tmppath, "Test Engineer")
            self.assertEqual(init_res, 0)
            content = tmppath.read_text(encoding="utf-8")
            self.assertIn("**Author**: Test Engineer", content)
            self.assertNotIn("**Author**: [Your Full Name]", content)

            # Fill in test fields to simulate completed student entry
            completed_content = content.replace("[Record Ω]", "1000 Ω")
            completed_content = completed_content.replace("[Record V]", "0.35 V")
            completed_content = completed_content.replace("[Record mA]", "0.0 mA")
            completed_content = completed_content.replace("[Enter your measured mA]", "20.4 mA")
            completed_content = completed_content.replace("[e.g., LED remained permanently on regardless of light level / LED did not illuminate in the dark]", "LED flickered intermittently on breadboard.")
            completed_content = completed_content.replace("[e.g., Checked voltage divider junction with DMM; measured 8.8V at base under all conditions]", "Wiggled jumper wires while probing with multimeter.")
            completed_content = completed_content.replace("[e.g., Photoresistor ground leg was plugged into breadboard column 17 instead of ground column 16, leaving circuit open]", "Loose spring clip in breadboard tie point.")
            completed_content = completed_content.replace("[e.g., Re-seated ground jumper wire into Row 16; base voltage dropped to 0.35V under room light; switching verified]", "Moved jumper wire to fresh tie point row; connection stable.")
            completed_content = completed_content.replace("[Explain how the physical properties of the PN junction execute decision-making without software.]", "The PN junction requires 0.7V threshold to conduct, naturally executing boolean IF/THEN logic via physics.")
            completed_content = completed_content.replace("[Analyze the impact on base current, battery drain, and switching sensitivity.]", "A 100 ohm resistor would draw excessive quiescent current and shift switching sensitivity toward blinding light.")
            completed_content = completed_content.replace("[Explain how software GPIO pins will replace analog divider thresholds with ADC sampling and programmable logic.]", "MicroPython reads ADC values and executes programmable if/else thresholds in code.")
            completed_content = completed_content.replace("- [ ]", "- [x]")
            tmppath.write_text(completed_content, encoding="utf-8")

            # Verify completed entry passes
            verify_res = verify_lab(tmppath)
            self.assertEqual(verify_res, 0)

if __name__ == "__main__":
    unittest.main()
