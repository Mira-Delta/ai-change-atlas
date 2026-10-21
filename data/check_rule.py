# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Mira Delta
"""Reproduce the narrow arithmetic claims in the 2026-10-20 pilot. Python 3, stdlib only."""
from pathlib import Path
import csv
from itertools import combinations
BASE = Path(__file__).parent
with (BASE / "three_chat_train.csv").open(newline="", encoding="utf-8") as fh:
    train = list(csv.DictReader(fh))
with (BASE / "three_chat_test.csv").open(newline="", encoding="utf-8") as fh:
    test = list(csv.DictReader(fh))
assert len(train) == 32 and len(test) == 16

def original_rule(s):
    group = set("AC")
    return "L" if ((s[1] in group) == (s[3] in group)) else "S"

def control_heuristic(s):
    return "S" if (s[2] == "D" or s[3] == "B") else "L"

assert all(original_rule(r["string"]) == r["original_label"] for r in train)
assert all(original_rule(r["string"]) == r["truth_original"] for r in test)
assert sum(r["chat1_initial"] == r["truth_original"] for r in test) == 11
assert sum(r["chat2_after_rule"] == r["truth_original"] for r in test) == 16
assert sum(control_heuristic(r["string"]) == r["control_label"] for r in train) == 25

# Test exactly the 140 hypotheses described in the private record:
# 10 unordered pairs of positions x 7 nontrivial A-containing letter subsets x 2 label orientations.
partitions = []
letters = 'ABCD'
for r in range(1,4):
    for subset in combinations(letters, r):
        if 'A' in subset:
            partitions.append(set(subset))
assert len(partitions) == 7
errors = []
for i,j in combinations(range(5),2):
    for subset in partitions:
        for same_label in 'LS':
            opposite = 'S' if same_label == 'L' else 'L'
            predicted = lambda s: same_label if ((s[i] in subset) == (s[j] in subset)) else opposite
            loss = sum(predicted(row['string']) != row['original_label'] for row in train)
            errors.append((loss, i+1,j+1,''.join(sorted(subset)),same_label))
errors.sort()
assert len(errors) == 140 and errors[0][0] == 0 and errors[1][0] == 10
print('Training original rule: 32/32')
print('Chat 1 held-out first pass: 11/16')
print('Chat 2 held-out after rule: 16/16')
print('Control post-hoc heuristic: 25/32 training only')
print('Candidate hypotheses tested: 140, unique zero-error rule, next-best loss 10')
print('All checks passed; this does NOT prove experimental causality.')
