# Test Case 01 — Beginner Bass Player

## 🎯 Test Objective

Evaluate whether the Bass Guitar Instructor AI Skill can generate a
practical and appropriately simplified practice plan for a complete
beginner.

---

## 👤 User Context

| Variable | Value |
|---|---|
| Skill Level | Complete Beginner |
| Instrument | 4-string bass |
| Genre | Gospel |
| Practice Time | 20 minutes per day |
| Primary Challenges | Timing and fretboard knowledge |
| Goal | Begin playing simple gospel bass lines |
| Requested Output | 7-day practice plan |

---

## 📝 Test Prompt

> I'm a complete beginner learning bass guitar.
>
> I have a 4-string bass and I can practice for about 20 minutes a day.
> I like gospel music, but I don't know the fretboard yet and I'm having
> trouble keeping a steady rhythm.
>
> Create a simple 7-day practice plan that will help me improve my timing,
> learn the basic notes on the bass, and start playing simple gospel bass lines.

---

## 🤖 Actual Output

| Day | 5 min | 5 min | 10 min |
|---|---|---|---|
| **Day 1** | Open-string rhythm | Learn open-string notes | Simple groove on one note |
| **Day 2** | Quarter-note timing | Learn frets 1–5 on E string | Two-note gospel groove |
| **Day 3** | Eighth-note timing | Learn frets 1–5 on A string | Root–5th groove |
| **Day 4** | Rhythm review | Find repeated notes | C major gospel pattern |
| **Day 5** | Rhythm with rests | Learn C, D, E, F, G | Walking between chords |
| **Day 6** | Groove with backing track | Fretboard review | I–IV–V gospel progression |
| **Day 7** | Timing test | Note-finding test | Play a complete simple groove |

---

## ✅ Validation Results

| Criterion | Result | Observation |
|---|---|---|
| Appropriate for player level | PASS | Exercises begin with basic open strings and simple rhythm concepts. |
| Respects available practice time | PASS | Each day totals exactly 20 minutes. |
| Addresses timing goal | PASS | Timing is practiced throughout the seven days. |
| Addresses fretboard goal | PASS | Note learning progresses from open strings to fretted notes. |
| Relevant to requested genre | PASS | Gospel-oriented grooves and progressions are incorporated. |
| Provides progression | PASS | Exercises increase gradually in complexity. |
| Clear enough for a complete beginner | PARTIAL | Some terminology may require additional explanation. |
| Provides measurable tempo targets | NEEDS IMPROVEMENT | Specific metronome/BPM targets are not included. |

---

## 🔍 Issues Identified

The test revealed several opportunities to improve the AI-generated
instruction:

1. Some terminology may be too advanced for a complete beginner,
   including "root–5th," "I–IV–V," and "walking between chords."

2. Timing exercises would be more measurable if the AI provided
   suggested metronome BPM ranges.

3. Several exercises describe what to practice but do not explain
   exactly how the learner should perform the exercise.

4. The plan could provide clearer success criteria before progressing
   to the next exercise.

---

## 💡 Recommended Skill Improvements

Future versions of the skill should encourage the AI to:

- Define unfamiliar musical terminology for beginners.
- Provide starting metronome tempos.
- Include step-by-step instructions for exercises.
- Provide measurable success criteria.
- Increase difficulty only after the learner demonstrates consistency.

---

## 📊 Test Conclusion

The skill successfully adapted the practice plan to the user's available
time, beginner skill level, musical interest, and stated learning goals.

The test also identified opportunities to improve instructional clarity
and measurability for complete beginners.

This test demonstrates the importance of evaluating AI-generated
instruction rather than assuming that a plausible response is
automatically an effective response.
